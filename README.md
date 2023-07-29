# Steps to run

# Development Diary

### Questions 

We focused on full-time developers working in NA 

1) Preprocessing (convert currency)

2) Q1: NA vs rest of world 
- clean
- analyze
- train

1) Q2: Unemployed vs Employed
- clean
- analyze
- train

### 01 - Data cleaning

We began by separating respondents into their separate regions. This meant that we kept a set of results for North Americans (Canada, United States). 

While inspecting the data set afterwards, we found a number of non-permissible values that we needed to remove from the dataset. These include:

1) Respondents with no **currency** listed
2) Respondents with no **compensation** listed
3) Respondents that are unemployed ()
4) Respondents that are not developers/software engineers

Once these values were cleaned, we then This meant that we kept a set of results for North Americans (Canada, United States), and another set for the rest of the world.

that some respondents were freelancing alongside their part-time or full-time job. However, the recorded salary did not differentiate the individual incomes for each source. 

Another issue we encountered was with the diverse types of currencies. We attempted to convert all compensation amounts to canadian using forex_python, a library that returns real-time conversion rates for currencies. In the North American data set, there were only two currencies that the library could not convert; We resolved this by recording all supporting currencies and their conversion rates to CAD, and then manually adding the last two. 

However, the data for the rest of the world returned many currencies (>40) that were not supported. Manually adding each currency would be too tedious of a task, so we opted to drop those rows for now, resulting in a loss of ~3000 rows in total, from 28k to 25k 

We looked at 6 different things that developers worked with, i.e Databases, Languages etc and extracted the top 10 for each, where 0-1 represents if a developer has worked with it

AISent # How much a person favours AI
AISelect # How likely will the user adopt AI technologies? And if so, which tools?

# Analysis for NA
1. A linear regression between years of experience and income for North America 

Initially, we ran a linear regression test to see the correlation between years of experience and income in North America. In the data, there were two outliers, so we quickly removed those. (less than 5 years of exp with salary above 600k)

We expected the p-value to be significant enough to indicate a correlation, but we were very wrong. Looking at the scatter plot, the data was extremely varied and the test could not provide any conclusive findings. Why?

After some thought, we realized that there are many more factors involved in determining salary. It is not secret in the industry that cost of living often impacts a developer's salary. For example, an engineer working at Amazon in Silicon Valley would make drastically different amounts of money compared to a developer in Seattle. This is because Silicon Valley is considered a **High-cost of living (HCOL)** area, whereas Seattle is a relatively **Low-cost of living (LCOL)** area. Companies intentionally base their offers around office location, but we are unable to account for this, since the location based data for developers is only scoped to countries, not specific cities, states, or provinces.

Different countries appear to provide different level of wages on average. For example, the average software engineer in Canada makes X, while in the USA they would make Y on average (TODO find reference). When scoping the data set to individual countries, we found that the p-value of the linear regression was substantially more significant, though still far from achieving confidence in the hypothesis at a value of (6.89e^-10).

LinregressResult(slope=1239.9329389884454, intercept=109657.85728526238, rvalue=0.19213921278650048, pvalue=2.6730296506951482e-71, stderr=68.79297443820633, intercept_stderr=1141.8697238042785)
This articles says country matters
https://nicholaspalichuk.medium.com/the-salary-differences-between-canada-and-usa-for-software-engineers-40b1a91ac4de

We thought that salary changes based on years of experience but other aspects like country and job title matters significantly. 
To look more deeply into our analysis,  we divided our data based on country and job title. Then we selected 15 out of 30 job titles that we wanted to look into and did a linear regression on compensation and work experience
We found a relationship between the two thus concluding that years of experience does matter for compensation. 

Nevertheless, we decided to look for other indicators of income. How does years of experience correlate to a developer's seniority/job title? And of course, how significant is the correlation between role and income?

2. A persons favour of AI + years of experience and comparing to salary 
3. How likely will the user adopt AI technologies? And if so, which tools?
4. For NA does a person know two kind of languages i.e if a person knows Java do they know JavaScript? (KNN) 

# Analysis for all
1. Salary differences between different countries (converted to CAD)
2. Chi-square test for technologies in NA and rest of the world 

<!-- stackoverflow ->  -->
clean data -> questions

stackoverflow -> clean data _. cleaning _> question



