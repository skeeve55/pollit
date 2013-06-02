from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import Integer, Text
from sqlalchemy.orm import relationship


Base = declarative_base()
    
class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text)  
        
class DbVote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    vote = Column(Text)    
    creation = Column(Text)
    
class DbPoll(Base):
    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    topic = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser")    
    creation = Column(Text)  