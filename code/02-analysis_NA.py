import pandas as pd
import constants as cs
import numpy as np
import matplotlib.pyplot as plt
import zipfile
from scipy import stats as st
from sklearn.preprocessing import MinMaxScaler
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm
import os

def load_data(filename: str) -> pd.DataFrame:
    with zipfile.ZipFile(f"../{filename}.zip") as data_zip:
        with data_zip.open(f"{filename}.csv") as developer_data:
            return pd.read_csv(developer_data)
        
def plotLinearRegression(x_data, y_data, x_label: str, y_label: str, graph_name: str, title: str): 
    reg = st.linregress(x_data, y_data)
    prediction = reg.slope * x_data + reg.intercept
    print(reg)
    residuals = y_data - prediction
    plt.figure(figsize=(8, 5))
    plt.title(title)
    plt.scatter(x_data, y_data, marker='.', color='blue', label='Compensation')
    plt.plot(x_data, prediction, 'r-', label='Regression Line (predictions)')
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{graph_name}.png")
    plt.close()

    # Plot residuals
    plt.hist(residuals, bins=30, density=True, color='blue', alpha=0.7, label='y_true - prediction')
    plt.legend()
    plt.xlabel(cs.COMPENSATION_LABEL)
    plt.ylabel('Residuals')
    plt.title(f'Residual Histogram')
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{graph_name}_residuals.png")
    plt.close()
    print(f"normality test on residuals{st.normaltest(residuals)}")

def plotHistogram(data, x_label: str, y_label, title: str, graph_name: str):
    plt.hist(data, bins=12, label='Compensation Frequency')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.title(title)
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{graph_name}.png")
    plt.close()

def plotAnovaAverageSalary(dataset, graph_name: str, feature_compared: str): 
    plt.figure(figsize=(12, 5))
    tukey_result = pairwise_tukeyhsd(dataset[cs.COMPENSATION] ** 0.5, dataset[feature_compared])
    plt.tight_layout()
    plt.xlabel(cs.COMPENSATION_AVERAGE_LABEL)
    tukey_result.plot_simultaneous()
    plt.subplots_adjust(left=0.35, right=0.95, top=0.9, bottom=0.1)
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{graph_name}.png")
    plt.close()

def createGroupByCountryBarGraphs(usa_data, canada_data, groupBy, graph_name): 
    grouped_usa_data = usa_data.groupby(by=groupBy).agg({cs.COMPENSATION: "mean"}).reset_index()
    grouped_canada_data = canada_data.groupby(by=groupBy).agg({cs.COMPENSATION: "mean"}).reset_index()
    merged_usa_canada = pd.merge(grouped_usa_data, grouped_canada_data, on=groupBy, how='inner')
    plt.figure(figsize=(10, 6))
    plt.barh( merged_usa_canada[groupBy], merged_usa_canada[cs.COMPENSATION + "_x"], label=cs.USA)
    plt.barh( merged_usa_canada[groupBy], merged_usa_canada[cs.COMPENSATION + "_y"], color='green', alpha=0.5, label=cs.CANADA)
    plt.xlabel(cs.COMPENSATION_AVERAGE_LABEL)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{graph_name}.png")
    plt.close()

def anovaTestIterator(value_list: list, usa_data, canada_data, X_data: str, Y_data: str):
    american_compensations = []
    canadian_compensations = []
    for value in value_list:
        american_jobs = usa_data[usa_data[X_data] == value].copy()
        canadian_jobs = canada_data[canada_data[X_data] == value].copy()
        
        american_compensations.append(american_jobs[Y_data] ** 0.5)
        canadian_compensations.append(canadian_jobs[Y_data] ** 0.5)
    
    # Showing one example of Levene's test for the first two groups
    print(f"Levene Test America {st.levene(american_compensations[0], american_compensations[1])}")
    print(f"Levene Test Canada {st.levene(canadian_compensations[0], canadian_compensations[1])}")

    plotHistogram(american_compensations[1], f"{Y_data} ({value_list[1]})", X_data, f"{X_data}_VS._{Y_data}", f"{X_data}_VS._{Y_data}")

    american_anova = st.f_oneway(*american_compensations)
    canadian_anova = st.f_oneway(*canadian_compensations)
    print(f"ANOVA of job compensations for {X_data}: \nUSA: {american_anova}\nCanada: {canadian_anova}")
    # usa_data = usa_data.dropna(subset=[X_data, cs.COMPENSATION])
    # tukey_result = pairwise_tukeyhsd(usa_data[cs.COMPENSATION] ** 0.5, usa_data[X_data])
    # print(tukey_result)


def main():
    na_data = load_data(cs.NORTH_AMERICA_DATA)
    # rof_data = load_data(cs.NORTH_AMERICA_DATA)

    #Graph raw data vs Comparison
    plt.scatter(na_data[cs.YEARS_CODE_PRO], na_data[cs.COMPENSATION], marker='.', color='blue', label='Compensation')
    plt.title('Work Experience vs Compensation')
    plt.legend()
    plt.xlabel(cs.WORK_EXPERIENCE_LABEL)
    plt.ylabel(cs.COMPENSATION_LABEL)
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{cs.EXP_VS_COMP_OUTLIER}.png")
    plt.close()
    
    # Eliminate outliers
    na_data = na_data[(na_data[cs.COMPENSATION] < cs.INCOME_THRESHOLD)]      

    #Convert to Numeric Data
    na_data[cs.YEARS_CODE_PRO] = pd.to_numeric(na_data[cs.YEARS_CODE_PRO], errors='coerce')
    na_data[cs.COMPENSATION] = pd.to_numeric(na_data[cs.COMPENSATION], errors='coerce')

    #Drop Null Columns
    regression_data = na_data.dropna(subset=[cs.COMPENSATION, cs.YEARS_CODE_PRO, cs.INDUSTRY, cs.EDUCATION])

    #Beginning Analysis
    # Question 1: Does years of experience correlate to a developer's total compensation in NA and Canada 
    # in the North American job market?

    # Tests used: Linear Regression.
    plotLinearRegression(regression_data[cs.YEARS_CODE_PRO], regression_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP, cs.REGRESSION_ALL_DATA)

    # Question 2: Are US employees paid more than Canadian employees
    canada_data = regression_data[(regression_data[cs.COUNTRY] == cs.CANADA)]
    usa_data = regression_data[(regression_data[cs.COUNTRY] == cs.USA)]
    plotLinearRegression(canada_data[cs.YEARS_CODE_PRO], canada_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP_CAN, cs.REGRESSION_CANADA_DATA)
    plotLinearRegression(usa_data[cs.YEARS_CODE_PRO], usa_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP_USA, cs.REGRESSION_USA_DATA)

    print(f"Normality test for Canada Compensation: {st.normaltest(canada_data[cs.COMPENSATION])}")
    print(f"Normality test for USA Compensation: {st.normaltest(usa_data[cs.COMPENSATION])}")

    # As the normality test failed: we are doing mannwhitneyu
    statistic, p_value = st.mannwhitneyu(canada_data[cs.COMPENSATION], usa_data[cs.COMPENSATION], alternative='two-sided')
    print(f"p value for mannwhitneyu on Canada and usa Compensation: {p_value}") # Different so compensation groups are different 

    # plotLinearRegression(regression_data[cs.WORK_EXPERIENCE], regression_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP_CAN)

    # No results... What about years of experience in relation to role/job title?
    createGroupByCountryBarGraphs(usa_data, canada_data, cs.JOB_TITLE, cs.CAN_US_COMP_AVERAGE)
    job_titles = cs.CHOSEN_JOB_TITLES
    anovaTestIterator(job_titles, usa_data, canada_data, cs.JOB_TITLE, cs.COMPENSATION)

    usa_data_chosen = usa_data[usa_data[cs.JOB_TITLE].isin(cs.CHOSEN_JOB_TITLES)]
    canada_data_chosen = canada_data[canada_data[cs.JOB_TITLE].isin(cs.CHOSEN_JOB_TITLES)]
    plotAnovaAverageSalary(usa_data_chosen, cs.USA_TUKEY_COMP, cs.JOB_TITLE)
    plotAnovaAverageSalary(canada_data_chosen, cs.CAN_TUKEY_COMP, cs.JOB_TITLE)
    
    # Plot graphs for various job compensations
    # Does the years of experience of employees have a significant impact on a developers compensation, and does this relationship vary across different job titles?
    
    # Question 3: A persons favour of AI + years of experience and comparing to salary ?
    #   
    # Tests used: This is for salary same could be done for work experience, it also had same results
    ai_data = na_data.dropna(subset=[cs.AISENT, cs.COMPENSATION])
    outcomes = ai_data[cs.AISENT].unique()
    outcome_transformed_list = []
    outcome_list = []

    for outcome in outcomes:
        outcome_df = ai_data[ai_data[cs.AISENT] == outcome].copy()
        outcome_df = outcome_df[[cs.COMPENSATION]] # transform as it was skewed towards left and this fixes it
        outcome_list.append(outcome_df)
        outcome_transformed_df = outcome_df[cs.COMPENSATION] ** 0.5
        outcome_transformed_list.append(outcome_transformed_df)

    # These graphs are normal therefore could be shown to say data is normal and has many values so we decided to do Anova as mentioned in lecture
    print(st.normaltest(outcome_list[1]))  # this fails so we will say we continuted as a lot of data
    print(st.normaltest(outcome_transformed_list[1])) 
    plotHistogram(outcome_list[1], cs.COMPENSATION_LABEL, cs.FREQUENCY_LABEL, cs.UNFAVOURABLE_LABEL, cs.AI_FAV_VS_COMP)
    plotHistogram(outcome_transformed_list[1], cs.COMPENSATION_TRANSFORMED_LABEL, cs.FREQUENCY_LABEL, cs.UNFAVOURABLE_LABEL, cs.AI_FAV_VS_COMP_TRANSFORMED)
    
    anova = st.f_oneway(*outcome_transformed_list).pvalue
    # This was [0.00233371]
    print(anova)
    # Therefore some relationship between compensation and favourability to AI, so post-hoc analysis
    # Perform Tukey's post hoc analysis i.e label values and their labels (favourability and compensation)
    tukey_result = pairwise_tukeyhsd(ai_data[cs.COMPENSATION], ai_data[cs.AISENT])
    print(tukey_result)

    # This gave us a relationship between unsure and very favourable therefore we can say we got nothing in regards to compensation
    # therefore we will remove 
    # Question: For NA does a person know two kind of languages i.e if a person knows Java do they know JavaScript? (KNN or some kind of T-Test) 

    createGroupByCountryBarGraphs(usa_data, canada_data, cs.INDUSTRY, cs.CAN_US_INDUS_AVERAGE)
    createGroupByCountryBarGraphs(usa_data, canada_data, cs.ORG_SIZE, cs.CAN_US_ORG_AVG)

    #Anova test b/w industry vs Compensation: 
    ind_comp_data = na_data.dropna(subset=[cs.INDUSTRY, cs.COMPENSATION])
    industries = ind_comp_data[cs.INDUSTRY].unique()

    anovaTestIterator(industries, usa_data, canada_data, cs.INDUSTRY, cs.COMPENSATION)
   
    plotAnovaAverageSalary(usa_data, cs.USA_TUKEY_COMP_INDUS, cs.INDUSTRY)
    plotAnovaAverageSalary(canada_data, cs.CAN_TUKEY_COMP_INDUS, cs.INDUSTRY)

    #Anova test b/w Education vs Compensation: 
    educ_comp_data = na_data.dropna(subset=[cs.EDUCATION, cs.COMPENSATION])
    education = educ_comp_data[cs.EDUCATION].unique()
    
    anovaTestIterator(education, usa_data, canada_data, cs.EDUCATION, cs.COMPENSATION)
    plotAnovaAverageSalary(usa_data, cs.USA_TUKEY_COMP_EDU, cs.EDUCATION)
    plotAnovaAverageSalary(canada_data, cs.CAN_TUKEY_COMP_EDU, cs.EDUCATION)
    
    # Organization size
    grouped_usa_data = usa_data.groupby(by=cs.ORG_SIZE).size().reset_index(name=cs.FREQUENCY_LABEL)
    grouped_canada_data = canada_data.groupby(by=cs.ORG_SIZE).size().reset_index(name=cs.FREQUENCY_LABEL)
    merged_usa_canada = pd.merge(grouped_usa_data, grouped_canada_data, on=cs.ORG_SIZE, how='inner')
    plt.figure(figsize=(10, 6))
    plt.barh( merged_usa_canada[cs.ORG_SIZE], merged_usa_canada[f"{cs.FREQUENCY_LABEL}"+ "_x"], label=cs.USA)
    plt.barh( merged_usa_canada[cs.ORG_SIZE], merged_usa_canada[f"{cs.FREQUENCY_LABEL}"+ "_y"], color='green', alpha=0.5, label=cs.CANADA)
    plt.xlabel(cs.FREQUENCY_LABEL)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{cs.CAN_US_ORG_FREQ}.png")
    plt.close()

    #chi-square tests
    contingency_table = pd.crosstab(index=na_data[cs.COUNTRY], columns=na_data[cs.ORG_SIZE])
    _, p_con_org, _, _ = st.chi2_contingency(contingency_table)
    print(f"Chi-Square test on Country and orgSize : {p_con_org}")
    
if __name__ == "__main__":
    main()
