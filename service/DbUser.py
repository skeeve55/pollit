from service.DbBase import Base
from sqlalchemy.schema import Column
from sqlalchemy.types import Text, Integer

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text)  