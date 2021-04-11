import databases
from sqlalchemy import MetaData, create_engine

from utils.config import settings


metadata = MetaData()
url = "postgresql://{user}:{password}@{host}/{name}".format(**settings.database)
database = databases.Database(url=url)


async def get_database():
    return database


async def get_test_database():
    """
    Bypass the main database when running Python tests
    This method gets called by FastAPI Depends()
    It is called at the top of every test file to override the default `get_database`
    """
    test_url = "postgresql://{user}:{password}@{host}/test_{name}".format(**settings.database)
    test_database = databases.Database(url=test_url)
    engine = create_engine(test_url)
    try:
        metadata.create_all(engine)
        await test_database.connect()
        yield test_database
    finally:
        await test_database.disconnect()
        metadata.drop_all(engine)
