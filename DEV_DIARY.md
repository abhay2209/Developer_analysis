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

# 02 - Analysis for NA
1. A linear regression between years of experience and income for North America 

Initially, we ran a linear regression test to see the correlation between years of experience and income in North America. In the data, there were two outliers with salaries over $600,000, so we quickly removed those from the data set. (less than 5 years of exp with salary above 600k)

We expected the p-value to be significant enough to indicate a correlation, but we were very wrong. Looking at the scatter plot, the data was extremely varied and the test could not provide any conclusive findings. Why?

After some thought, we realized that there are many more factors involved in determining salary. It is no secret in the industry that cost of living often impacts a developer's salary. For example, an engineer working at Amazon in Silicon Valley would make drastically different amounts of money compared to a developer in Seattle. This is because Silicon Valley is considered a **High-cost of living (HCOL)** area, whereas Seattle is a relatively **Low-cost of living (LCOL)** area [FIND REFERENCE]. Companies also intentionally base their offers around office location, but we are unable to account for this as our location data is scoped to the country levels, based data for developers is only scoped to countries, not specific cities, states, or provinces.

Different countries appear to provide different level of wages on average. For example, the average software engineer in Canada makes X, while in the USA they would make Y on average (TODO find reference). When scoping the data set to individual countries, we found that the p-value of the linear regression was substantially more significant, though still far from achieving confidence in the hypothesis at a value of (6.89e^-10).

```
LinregressResult(slope=1239.9329389884454, intercept=109657.85728526238, rvalue=0.19213921278650048, pvalue=2.6730296506951482e-71, stderr=68.79297443820633, intercept_stderr=1141.8697238042785)
```

This articles says country matters
https://nicholaspalichuk.medium.com/the-salary-differences-between-canada-and-usa-for-software-engineers-40b1a91ac4de

Another hypothesis we wanted to test was: The years of experience that a developer has positively correlates with their total compensation. We expected our hypothesis to be proved correct, but could not achieve certainty in the results of our tests. We believe that this was most likely due to the presence of other factors that we did not initially account for, such as the location and region of participants, and the job title/seniority level of a participant.

To look more deeply into our analysis,  we divided our data based on country and job title. Then we selected 15 out of 30 job titles that we wanted to look into and did a linear regression on the compensation and work experience of each individual job title to determine whether or not there was a relationship. For each and every job, our results indicated that there was a relationship, providing evidence that years of experience does indeed have a positive correlation with compensation. 

To expand on our analysis, we also took a look into the variances between difference job titles. Does a certain role pay more on average than others? And if so, what is the degree of variance? Does this remain true between both the USA and Canada? For each job title, we extracted the compensation data and added it as a sample to an ANOVA test, once for the USA and once for Canada. Since we have hundreds to thousands of data points for each role, we decided to assume that the data is normal enough based on the Central Limit Theorem, enabling us to use ANOVA one-way test while meeting the assumptions. The results we obtained were: 

USA: F_onewayResult(statistic=25.88190380272185, pvalue=2.5353730116198245e-57)
Canada: F_onewayResult(statistic=5.193699588570149, pvalue=1.8942943356605458e-08)

Both ANOVA tests failed significance, which let us know that there is most definitely a difference between the compensations of different jobs for both Canada and USA. It is also notable that the p-value of the ANOVA on Canada was substantially higher than the USA. The Canadian sub-sample has much fewer data points, which may be a cause of this. But otherwise, it could be indicative that the variance in salary between different job titles is larger in the USA than it is in Canada. To visualize this, we conducted a post-hoc analysis using Tukey's HSD test, and visualized a graph that summarized results based on 12 job positions that we found were most impactful:

[INSERT BAR CHART HERE]

The median, means, and ranges of each job's salary were too similar to provide anything conclusive, thus we could not prove there was a difference. 

Canadian developers were paid more all across the board, but the [data](https://nicholaspalichuk.medium.com/the-salary-differences-between-canada-and-usa-for-software-engineers-40b1a91ac4de) says otherwise! We have 7,169, rows of data for USA, and 1,260 for Canada. This discrepancy of salary may be due to the difference in organization sizes. According to the diagram below, larger companies pay out higher salaries on average. 

We conducted a Chi-square test on organization sizes between the Canadian and American data set, and found that it indicates that there is a significant association between organization size and country. This would imply that there is a difference in the distribution of people from different organization sizes between the two countries, suggesting that more people from larger organizations might have filled in the data in Canada compared to the USA.

1. Now that we have a good idea of how years of experience and job title influence a developer's income, the next question we begged to ask was: "Do different skills/toolsets impact a developer's salary?". How would the breadth and/or depth of a developer's technical knowledge affect their income? Evidently, different job titles require different skillsets, so we expected the tools, skillset, and job title to be closely related in correlation to their impact on income.

Firstly, we attempted to find a correlation between languages and income. Running a PCA test returned a bad value, as there was not much variance and the degree of information loss was too high to consider the result. Conducting a linear regression also returned non-sensical values; .Languages could not find correlation, PCA and linear regression both failed. PCA did not have a lot of variance and had information loss, linear regression returned non-sensible values.

For NA does a person know two kind of languages i.e if a person knows Java do they know JavaScript? (KNN) 
Cannot do KNN here I think,
    1. Do Chi-Squared test between two languages to see if a person knows one do they another 
    2. Anova test to see compensation differs with language known 
    3. Ols.fit to see if their is relationship between language and compensation 



# Analysis for all
1. Salary differences between different countries (converted to CAD)
2. Chi-square test for technologies in NA and rest of the world 

<!-- stackoverflow ->  -->
Plan 
1. outlier detection (high compensations -> removed) add the graph here
2. Years of experience and compensation relationship -> There is one
3. Differentiate data for US and Canada and do a man-whittney test on compensation (should probably have different means)
4. For US as take job titles, do Anova test, should fail, then select some specific jobs and plot mean graphs (maybe 10 titles)(or just show graph (overlay USA on Canada))
5. Show AI comparison to salary (which shows no relation already)
6. Relationship between framework and compensation (still have to think how)
7. Chi-Square test between three languages for example (C++ - JavaScript) 

Start working on training models and predicting. 