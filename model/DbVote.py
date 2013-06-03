from DbBase import Base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Text, Integer

class DbVote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    vote = Column(Text)
    poll_id = Column(Integer, ForeignKey("polls.id"))    
    creation = Column(Text)
    