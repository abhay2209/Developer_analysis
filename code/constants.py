from enum import Enum
import numpy as np

DATA_PATH: str = "data_compressed.zip"
FILENAME: str = "survey_results_public.csv"

NORTH_AMERICA_DATA: str = "north_america"
REST_OF_THE_WORLD_DATA: str = "rest_of_the_world"

NA_TRAIN_DATA: str = "north_america_train"
X_VALID: str = 'X_valid_data'
Y_VALID: str = 'y_valid_data'

# Keep Columns
KEEP_COLUMNS: list = [
    'MainBranch', 'Age', 'Employment', 'RemoteWork', 'Currency',
    'EdLevel', 'YearsCode', 'YearsCodePro', 'DevType', 'OrgSize', 'Country', 'CompTotal', 
    'LanguageHaveWorkedWith','DatabaseHaveWorkedWith','PlatformHaveWorkedWith',
    'WebframeHaveWorkedWith', 'MiscTechHaveWorkedWith','ToolsTechHaveWorkedWith', 
    'AISent', 'Industry'
]

# Columns
INDEX: str = "index"
MAIN_BRANCH: str = 'MainBranch'
COUNTRY: str = 'Country'
EMPLOYMENT_TYPE: str = 'Employment'
EDUCATION: str = 'EdLevel'
CURRENCY: str = 'Currency'
COMPENSATION: str = 'CompTotal'
WORK_EXPERIENCE: str = 'WorkExp'
YEARS_CODE: str = 'YearsCode'
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
INDUSTRY: str = 'Industry'
ORG_SIZE: str = 'OrgSize'
AGE: str = 'Age'
REMOTE: str = 'RemoteWork'

DROP_TECHNOLOGIES_LIST: list = [LANGUAGES, DATABASES, FRAMEWORKS, PLATFORMS, TOOLS, OTHER_TECH]

# Data
EMPLOYED_FULL_TIME: str = 'Employed, full-time' 
EMPLOYED_PART_TIME: str = 'Employed, part-time'
DEVELOPERS: str = 'I am a developer by profession'
USA: str = 'United States of America'
CANADA: str = 'Canada'
CANADA_CURRENCY: str = "CAD"
TOP_10_LANG: int = 5
TOP_10_DATABASE: int = 5
TOP_10_PLATFORM: int = 5
TOP_10_FRAMEWORKS: int = 5
TOP_10_TOOLS: int = 5
TOP_10_OTHER_TECH: int = 5
INCOME_THRESHOLD: int = 400000

CHOSEN_JOB_TITLES: int = ['Research & Development role', 'Data scientist or machine learning specialist', 'Developer, full-stack', 'Data or business analyst', 
                          'Developer, front-end', 'Engineering manager', 'Engineer, data', 'Developer, game or graphics', 'Developer, embedded applications or devices',
                          'Developer, mobile', 'Database administrator','DevOps specialist', 'Cloud infrastructure engineer']


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
LANGUAGES_LIST: list = ['JavaScript', 'SQL', 'HTML/CSS', 'Python', 'TypeScript', 'Bash/Shell (all shells)', 'C#', 'Java', 'C++', 'PowerShell']
FRAMEWORK_LIST: list = ['React', 'Node.js', 'jQuery', 'ASP.NET CORE',
       'Angular', 'Express', 'ASP.NET', 'Next.js', 'Vue.js', 'Flask']
ALL_FRAMEWORK = ['JavaScript', 'SQL', 'HTML/CSS', 'Python', 'TypeScript',
       'Bash/Shell (all shells)', 'C#', 'Java', 'C++', 'PowerShell',
       'PostgreSQL', 'MySQL', 'Microsoft SQL Server', 'SQLite', 'Redis',
       'MongoDB', 'Elasticsearch', 'Dynamodb', 'MariaDB', 'Oracle', 'Docker',
       'npm', 'Homebrew', 'Pip', 'Webpack', 'Kubernetes', 'Yarn', 'Make',
       'NuGet', 'Terraform', 'React', 'Node.js', 'jQuery', 'ASP.NET CORE',
       'Angular', 'Express', 'ASP.NET', 'Next.js', 'Vue.js', 'Flask',
       'Amazon Web Services (AWS)', 'Microsoft Azure', 'Google Cloud',
       'Cloudflare', 'Digital Ocean', 'Heroku', 'Firebase', 'Vercel',
       'Netlify', 'VMware', '.NET (5+) ', '.NET Framework (1.0 - 4.8)',
       'Pandas', 'NumPy', 'Apache Kafka', 'Spring Framework', 'RabbitMQ',
       'React Native', 'Scikit-Learn', 'Torch/PyTorch']

# Plot labels
COMPENSATION_LABEL: str = 'Compensation'
COMPENSATION_TRANSFORMED_LABEL: str = 'Compensation Transformed'
COMPENSATION_AVERAGE_LABEL: str = 'Average Compensation'
WORK_EXPERIENCE_LABEL: str = 'Work Experience'
YEARS_OF_CODE_LABEL:str = "Years of Coding"
AI_SENT_LABEL: str = "AI Sentiment"
JOB_TITLE_LABEL: str = 'Job title'
UNFAVOURABLE_LABEL: str = 'Unfavourable'
FREQUENCY_LABEL: str = 'Frequency'

# Output filenames
EXP_VS_COMP_OUTLIER: str = 'yoe_vs_income_outliers'
EXP_VS_COMP: str = "01-yoe-income"
EXP_VS_COMP_CAN: str = "01-yoe-income-can"
EXP_VS_COMP_USA: str = "01-yoe-income-usa"
EXP_VS_COMP_US_MOBILE: str = "01-yoe-income-us-mobile"
EXP_VS_COMP_US_FULLSTACK: str = "01-yoe-income-us-fullstack"
AI_FAV_VS_COMP: str = "02-aifav-vs-comp"
AI_FAV_VS_COMP_TRANSFORMED: str = "02-aifav-vs-comp-tran"
CAN_US_COMP_AVERAGE: str = '04-can_vs_us_comp'
CAN_US_INDUS_AVERAGE: str = '04-can_vs_us_indus'
CAN_US_ORG_AVG: str = '04-can_vs_us_org_avg'
CAN_US_ORG_FREQ: str = '04-can_vs_us_org_freq'
CAN_TUKEY_COMP: str = '04-can_tukey_comp'
USA_TUKEY_COMP: str = '04-usa_tukey_comp'
CAN_TUKEY_COMP_INDUS: str = '04-can_tukey_comp_indus'
USA_TUKEY_COMP_INDUS: str = '04-usa_tukey_comp_indus'
CAN_TUKEY_COMP_EDU: str = '04-can_tukey_comp_edu'
USA_TUKEY_COMP_EDU: str = '04-usa_tukey_comp_edu'

# Output folders
DIAGRAM_OUTPUT_FOLDER: str = "./diagrams"
ML_MODELS_FOLDER: str = "./ml_models"

# ML encodings to convert to numeric for training
AGE_GROUP_MAPPING: dict = {
    'Under 18 years old': 1,
    '18-24 years old': 2,
    '25-34 years old': 3,
    '35-44 years old': 4,
    '45-54 years old': 5,
    '55-64 years old': 6,
    '65 years or older': 7,
    'Prefer not to say': 8
}

YEARS_CODE_MAPPING: dict = {
    "More than 50 years": 55,
    "Less than 1 years": 0.5,
    "Less than 1 year": 0.5
}

EDUCATION_LEVEL_MAPPING: dict = {
    'Bachelor’s degree (B.A., B.S., B.Eng., etc.)': 0,
    'Some college/university study without earning a degree': 1,
    'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)': 2,
    'Something else': 3,
    'Professional degree (JD, MD, Ph.D, Ed.D, etc.)': 4,
    'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 5,
    'Associate degree (A.A., A.S., etc.)': 6,
    'Primary/elementary school': 7,
    np.nan: - 1,
}

INDUSTRY_MAPPING: dict = {
    'Information Services, IT, Software Development, or other Technology': 0,
    'Financial Services': 1,
    'Other': 2,
    'Manufacturing, Transportation, or Supply Chain': 3,
    'Oil & Gas': 4,
    'Healthcare': 5,
    'Insurance': 6,
    'Higher Education': 7,
    'Retail and Consumer Services': 8,
    'Advertising Services': 9,
    'Legal Services': 10,
    'Wholesale': 11,
    np.nan: - 1,
}

COUNTRY_MAPPING = {
    'United States of America': 0,
    'Canada': 1
}

TRAINING_SCORE: str = "train_score"
VALIDATION_SCORE: str = "valid_score"

RANDOM_FOREST_MODELS: str = "Random_forest_models"
SVR_MODELS: str = "SVR_models"
GB_MODELS: str = "Random_forest_models"
XGBOOST_MODELS: str = "XGBoost_models"

BEST_RF_MODELS: str = 'best_rf_models'
BEST_SVR_MODELS: str = 'best_svr_models'
BEST_GB_MODELS: str = 'best_gb_models'
BEST_XGBOOST_MODELS: str = 'best_xgboost_models'








