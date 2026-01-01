from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABSE_URL = "postgresql://neondb_owner:npg_JuQciI1Y9eTg@ep-crimson-sound-advvvxil-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(url=DATABSE_URL)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


Base = declarative_base()