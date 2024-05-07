from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_hostname = "localhost"
database_port = "5432"
database_password = "postgres123321"
database_name = "fastapi-todo-app"
database_username = "postgres"

SQLALCHEMY_DATABASE_URL = f"postgresql://{database_username}:{database_password}@{database_hostname}:{database_port}/{database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
