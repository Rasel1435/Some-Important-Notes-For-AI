# DATA_SOURCE = 'online'
DATA_SOURCE = '../data/Bengaluru_House_Data.csv'
PROCESSED_DATA_PATH = '../data/Final_Pipelines_Data.csv'
FEATURE_GROUP_NAME = 'Students_Performance_in_Exams'
FEATURE_GROUP_DESCRIPTION = "Students Performance in Exams"
FEATURE_DESCRIPTIONS = [
    {"name": "Gender", "description": "Total Gender will be here it's str type"},
    {"name": "race", "description": "Total race group will be here"},
    {"name": "parental_level_of_education", "description": "parental_level_of_education"},
    {"name": "lunch", "description": "Total lunch"},
    {"name": "math_score", "description": "math_score will be here"},
    {"name": "reading_score", "description": "reading_score will be here"},
    {"name": "writing_score", "description": "writing_score will be here"},
]

TABLE_NAME = 'Students-Performance-in-Exams'
# AWS credentials
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
MODEL_NAME = 'Students-Performance-in-Exams'
DOCKER = ''