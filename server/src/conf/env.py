from dotenv import load_dotenv
from os import getenv

load_dotenv()

AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY") 
AWS_REGION_NAME = getenv("AWS_REGION_NAME")
AWS_S3_BUCKET = getenv("AWS_S3_BUCKET")
AWS_SES_SOURCE = getenv("AWS_SES_SOURCE")
DB_HOST=getenv("DB_HOST")
DB_PORT=getenv("DB_PORT")
DB_NAME=getenv("DB_NAME")
DB_USER=getenv("DB_USER")
DB_PASSWORD=getenv("DB_PASSWORD")
DB_ENGINE=getenv("DB_ENGINE")
DB_SCHEME=getenv("DB_SCHEME")
AUTH0_DOMAIN=getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID=getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET=getenv("AUTH0_CLIENT_SECRET")
AUTH0_APP_CLIENT_ID=getenv("AUTH0_APP_CLIENT_ID")
AUTH0_APP_CLIENT_SECRET=getenv("AUTH0_APP_CLIENT_SECRET")
AUTH0_AUDIENCE=getenv("AUTH0_AUDIENCE")
AUTH0_GRANT_TYPE=getenv("AUTH0_GRANT_TYPE")
FAUNA_SECRET=getenv("FAUNA_SECRET")
PULUMI_ORG=getenv("PULUMI_ORG")

