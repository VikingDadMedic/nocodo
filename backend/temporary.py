import databases
from utils.config import settings
from sqlalchemy import create_engine
from utils.database import metadata

from apps.user.models import user, email_verification_token, forgot_password_token


db_url = "postgresql://{user}:{password}@{host}/{name}".format(**settings.database)
database = databases.Database(url=db_url)
engine = create_engine(db_url)
metadata.create_all(engine)
