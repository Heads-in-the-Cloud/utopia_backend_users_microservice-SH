# ######################################################################################################################
# ########################################                               ###############################################
# ########################################      SQLAlchemy Database      ###############################################
# ########################################           Creation            ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = os.getenv('DB_ACCESS_URI') or "mysql+pymysql://root:root@127.0.0.1:6603/utopia"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
