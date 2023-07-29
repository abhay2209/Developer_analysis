DATA_PATH: str = "data_compressed.zip"
FILENAME: str = "survey_results_public.csv"

NORTH_AMERICA_DATA: str = "north_america"
REST_OF_THE_WORLD_DATA: str = "rest_of_the_world"

# Keep Columns
KEEP_COLUMNS: list = [
    'MainBranch', 'Age', 'Employment', 'RemoteWork', 
    'EdLevel', 'LearnCodeCoursesCert', 'YearsCode', 
    'YearsCodePro', 'DevType', 'OrgSize', 'Country',
    'Currency', 'CompTotal', 'LanguageHaveWorkedWith',
    'DatabaseHaveWorkedWith','PlatformHaveWorkedWith',
    'WebframeHaveWorkedWith', 'MiscTechHaveWorkedWith','ToolsTechHaveWorkedWith', 
    'AISent','AISelect', 'AIToolCurrently Using','WorkExp', 'ProfessionalTech', 
    'Industry'
]

# Columns
MAIN_BRANCH: str = 'MainBranch'
COUNTRY: str = 'Country'
EMPLOYMENT_TYPE: str = 'Employment'
CURRENCY: str = 'Currency'
COMPENSATION: str = 'CompTotal'
WORK_EXPERIENCE: str = 'WorkExp'
YEARS_CODE_PRO: str = 'YearsCodePro'
LANGUAGES: str = 'LanguageHaveWorkedWith'
DATABASES: str = 'DatabaseHaveWorkedWith'
PLATFORMS: str = 'PlatformHaveWorkedWith'
FRAMEWORKS: str = 'WebframeHaveWorkedWith'
TOOLS: str = 'ToolsTechHaveWorkedWith'
OTHER_TECH: str = 'MiscTechHaveWorkedWith'
AISENT: str = 'AISent'
USING_AI: str = 'AIToolCurrently Using'
JOB_TITLE: str = 'DevType'

DROP_TECHNOLOGIES_LIST: list = [LANGUAGES, DATABASES, FRAMEWORKS, PLATFORMS, TOOLS, OTHER_TECH, USING_AI]

# Data
EMPLOYED_FULL_TIME: str = 'Employed, full-time' 
EMPLOYED_PART_TIME: str = 'Employed, part-time'
DEVELOPERS: str = 'I am a developer by profession'
USA: str = 'United States of America'
CANADA: str = 'Canada'
CANADA_CURRENCY: str = "CAD"
TOP_10_LANG: int = 10
TOP_10_DATABASE: int = 10
TOP_10_PLATFORM: int = 10
TOP_10_FRAMEWORKS: int = 10
TOP_10_TOOLS: int = 10
TOP_10_OTHER_TECH: int = 10
INCOME_THRESHOLD: int = 400000
DEVELOPER_MOBILE: str = 'Developer, mobile'
DEVELOPER_FULLSTACK: str = 'Developer, full-stack'

CHOSEN_JOB_TITLES: int = ['Research & Development role', 'Data scientist or machine learning specialist', 'Developer, full-stack', 'Data or business analyst', 
                          'Developer, front-end', 'Engineering manager', 'Engineer, data', 'Developer, game or graphics', 'Developer, embedded applications or devices',
                          'Developer, mobile', 'Database administrator']

# Canadian currency rates
CURRENCY_CONVERSION_RATE: dict = {'EUR': 0.6962818548948615, 'USD': 0.7505918395766608, 'JPY': 104.609385879404,
  'BGN': 1.36178805180337, 'CZK': 16.47820637794179, 'DKK': 5.187647959894165, 
  'GBP': 0.5973750174070463, 'HUF': 256.74000835538226, 'PLN': 3.1057652137585294,
  'RON': 3.4511906419718703, 'SEK': 8.127698092187718, 'CHF': 0.6765074502158475, 
  'ISK': 104.09413730678179, 'NOK': 8.085224899039131, 'TRY': 17.493663835120458, 
  'AUD': 1.1156524160980366, 'BRL': 3.687856844450634, 'CNY': 5.350160144826626, 
  'HKD': 5.883094276563153, 'IDR': 11138.225873833728, 'INR': 61.892494081604234, 
  'KRW': 968.6046511627907, 'MXN': 13.045258320568168, 'MYR': 3.463236318061552, 
  'NZD': 1.2273360256231722, 'PHP': 42.0735273638769, 'SGD': 1.0082161258877593, 
  'THB': 25.95529870491575, 'ZAR': 14.05138560089124, 'UAH': 0.36, 'CAD': 1, 
  'AED': 0.36, 'ILS': 0.35, 'PKR': 0.0046
}

REST_OF_WORLD_CURRENCY_NA = ['AZN', 'JMD', 'KHR', 'TWD', 'MRU', 'BTN', 'MWK', 'FJD', 'MKD', 'MVR', 'TND', 'QAR', 'COP', 'AWG', 'GIP', 'NPR', 
                             'BHD', 'MDL', 'SYP', 'GYD', 'MZN', 'XOF', 'AMD', 'BND', 'MUR', 'CDF', 'MMK', 'CRC', 'NAD', 'BDT', 'LBP', 'PEN', 
                             'TMT', 'LSL', 'TZS', 'VES', 'RWF', 'EGP', 'JOD', 'SLL', 'PYG', 'KWD', 'LKR', 'KES', 'RUB', 'UZS', 'MNT', 'BOB', 
                             'BZD', 'TTD', 'ALL', 'XAF', 'MOP', 'SRD', 'BBD', 'SAR', 'SSP', 'ARS', 'LAK', 'HRK', 'VND', 'MAD', 'AOA', 'IQD', 
                             'CUP', 'PKR', 'CVE', 'GTQ', 'UGX', 'YER', 'IRR', 'CLP', 'ZMW', 'DZD', 'GHS', 'KGS', 'BAM', 'GEL', 'UYU', 'HNL', 
                             'NGN', 'IMP', 'AFN', 'NIO', 'BYN', 'OMR', 'MGA', 'RSD', 'KZT', 'ETB', 'DOP']

CHOSEN_JOB_GRAPHS: list = ['Data scientist or machine learning specialist', 'Engineering manager']

# Plot labels
COMPENSATION_LABEL: str = 'Compensation'
WORK_EXPERIENCE_LABEL: str = 'Work Experience'
YEARS_OF_CODE_LABEL:str = "Years of Coding"
AI_SENT_LABEL: str = "AI Sentiment"
JOB_TITLE_LABEL: str = 'Job title'

# Output filenames
EXP_VS_COMP: str = "01-yoe-income"
# EXP_VS_COMP_CAN: str = "01-yoe-income-can"
EXP_VS_JOBTITLE: str = "02-yoe-vs job"
EXP_VS_COMP_US_MOBILE: str = "01-yoe-income-us-mobile"
EXP_VS_COMP_US_FULLSTACK: str = "01-yoe-income-us-fullstack"

# Output folders
DIAGRAM_OUTPUT_FOLDER: str = "./diagrams"