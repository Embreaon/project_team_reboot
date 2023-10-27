from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from env import *

DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USER, PASSWORD, HOST, PORT, DBNAME)

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)
    
    def session_maker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn
    