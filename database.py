import os
from pathlib import Path
from dotenv import load_dotenv

# Explicitly load the .env file that lives next to this script
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Now these will be defined:
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{os.environ['DATABASE_USER']}:"
    f"{os.environ['DATABASE_PASSWORD']}@"
    f"{os.environ['DATABASE_HOST']}:"
    f"{os.environ['DATABASE_PORT']}/"
    f"{os.environ['DATABASE_NAME']}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
