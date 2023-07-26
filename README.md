# Steps to run


# Development Diary

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