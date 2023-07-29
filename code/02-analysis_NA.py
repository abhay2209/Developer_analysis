import pandas as pd
import constants as cs
import matplotlib.pyplot as plt
import zipfile
from scipy import stats as st
from sklearn.preprocessing import MinMaxScaler
from statsmodels.stats.multicomp import pairwise_tukeyhsd

import os

def load_data(filename: str) -> pd.DataFrame:
    with zipfile.ZipFile(f"../{filename}.zip") as data_zip:
        with data_zip.open(f"{filename}.csv") as developer_data:
            return pd.read_csv(developer_data)
        
def plotLinearRegression(x_data, y_data, x_label: str, y_label: str, graph_name: str): 
    reg = st.linregress(x_data, y_data)
    #residuals = y - (reg.slope*x + reg.intercept)
    prediction = reg.slope * x_data + reg.intercept
    print(reg)
    
    plt.scatter(x_data, y_data, marker='.', color='blue')
    plt.plot(x_data, prediction, 'r-')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.savefig(f"{cs.DIAGRAM_OUTPUT_FOLDER}/{graph_name}.png")
    plt.close()
        
def main():
    na_data = load_data(cs.NORTH_AMERICA_DATA)
    # rof_data = load_data(cs.NORTH_AMERICA_DATA)
    na_data = na_data[(na_data[cs.COMPENSATION] < cs.INCOME_THRESHOLD)]

    na_data[cs.YEARS_CODE_PRO] = pd.to_numeric(na_data[cs.YEARS_CODE_PRO], errors='coerce')
    regression_data = na_data.dropna(subset=[cs.WORK_EXPERIENCE, cs.COMPENSATION, cs.YEARS_CODE_PRO])
    regression_data = regression_data[(regression_data[cs.COMPENSATION] < cs.INCOME_THRESHOLD)] # Eliminate outliers

    # Question 1: Does years of experience correlate to a developer's total compensation in NA and Canada 
    # in the North American job market?
    # 
    # Tests used: Linear Regression    

    plotLinearRegression(regression_data[cs.WORK_EXPERIENCE], regression_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP)
    regression_data = regression_data[(regression_data[cs.COUNTRY] == cs.USA)]
    # plotLinearRegression(regression_data[cs.WORK_EXPERIENCE], regression_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP_CAN)

    # No results... What about years of experience in relation to role/job title?
    grouped_regression_data = regression_data.groupby(by=cs.JOB_TITLE).agg({cs.COMPENSATION: "mean"}).reset_index()
    plt.figure(figsize=(10, 6))
    plt.barh(grouped_regression_data[cs.JOB_TITLE], grouped_regression_data[cs.COMPENSATION])
    plt.tight_layout()
    plt.savefig("hist_try")
    plt.close()

    job_titles = cs.CHOSEN_JOB_TITLES
    print(len(job_titles))

    
    for job in job_titles:
        print(job)
        job_df = regression_data[regression_data[cs.JOB_TITLE] == job].copy()
        reg = st.linregress(job_df[cs.WORK_EXPERIENCE], job_df[cs.COMPENSATION])
        print(f"{reg}")
        
    # Data scientist or machine learning specialist
    #Engineering manager
    
    manager_data = regression_data[regression_data[cs.JOB_TITLE] == cs.DEVELOPER_MOBILE]
    fullstack_data = regression_data[regression_data[cs.JOB_TITLE] == cs.DEVELOPER_FULLSTACK]
    plotLinearRegression(manager_data[cs.WORK_EXPERIENCE], manager_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP_US_MOBILE)     
    plotLinearRegression(fullstack_data[cs.WORK_EXPERIENCE], fullstack_data[cs.COMPENSATION], cs.WORK_EXPERIENCE_LABEL, cs.COMPENSATION_LABEL, cs.EXP_VS_COMP_US_FULLSTACK)

    
    
        
    # Does the years of experience of employees have a significant impact on a developers compensation, and does this relationship vary across different job titles?
    
    # grouped_regression_data["cs.WORK_EXPERIENCE"] = (grouped_regression_data[cs.WORK_EXPERIENCE] - grouped_regression_data[cs.WORK_EXPERIENCE].min()) / (grouped_regression_data[cs.WORK_EXPERIENCE].max() - grouped_regression_data[cs.WORK_EXPERIENCE].min())
    
    # plotLinearRegression(regression_data[cs.WORK_EXPERIENCE], regression_data[cs.JOB_TITLE], cs.WORK_EXPERIENCE_LABEL, cs.JOB_TITLE_LABEL, cs.EXP_VS_JOBTITLE)

    # There is also a column for years of coding... How does it correlate to years of experience and income?

    # plotLinearRegression(regression_data[cs.YEARS_CODE], regression_data[cs.COMPENSATION], cs.YEARS_OF_CODE_LABEL)
    
    # Question 2: A persons favour of AI + years of experience and comparing to salary ?
    #   
    # Tests used: This is for salary same could be done for work experience, it also had same results
    ai_data = na_data.dropna(subset=[cs.AISENT, cs.COMPENSATION])
    outcomes = ai_data[cs.AISENT].unique()
    outcome_list = []
    for outcome in outcomes:
        outcome_df = ai_data[ai_data[cs.AISENT] == outcome].copy()
        outcome_df = outcome_df[[cs.COMPENSATION]] ** 0.5 # transform as it was skewed towards left and this fixes it
        outcome_list.append(outcome_df)

    # These graphs are normal therefore could be shown to say data is normal and has many values so we decided to do Anova as mentioned in lecture
    print(st.normaltest(outcome_list[1])) # this fails so we will say we continuted as a lot of data 
    plt.hist(outcome_list[1], bins=10)
    plt.show()
    
    anova = st.f_oneway(*outcome_list).pvalue
    # This was [0.00233371]
    print(anova)
    # Therefore some relationship between compensation and favourability to AI, so post-hoc analysis
    # Perform Tukey's post hoc analysis i.e label values and their labels (favourability and compensation)
    tukey_result = pairwise_tukeyhsd(ai_data[cs.COMPENSATION], ai_data[cs.AISENT])
    print(tukey_result)

    # This gave us a relationship between unsure and very favourable therefore we can say we got nothing in regards to compensation
    # therefore we will remove it

    # Do the exact same for Q3
    
        
    # Question 3: How likely will the user adopt AI technologies? And if so, which tools?
    
    # Question 4: For NA does a person know two kind of languages i.e if a person knows Java do they know JavaScript? (KNN or some kind of T-Test) 
    
    #Question 5: If anything comes up, think more in terms of where t-test or Anova is possible
if __name__ == "__main__":
    main()