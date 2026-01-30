import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class Settings:
    APP_ENV = os.getenv("APP_ENV", "local")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))

    DB_URL = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")

settings = Settings()




# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Settings:
#     APP_ENV = os.getenv("APP_ENV")

#     DB_URL = (
#         f"mysql+pymysql://{os.getenv('DB_USER')}:"
#         f"{os.getenv('DB_PASSWORD')}@"
#         f"{os.getenv('DB_HOST')}:"
#         f"{os.getenv('DB_PORT')}/"
#         f"{os.getenv('DB_NAME')}"
#     )

#     EMAIL_SENDER = os.getenv("EMAIL_SENDER")
#     EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
#     EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

#     ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")

# settings = Settings()