from service.DbBase import Base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Text, Integer

class DbUserVote(Base):
    __tablename__ = 'user_votes'
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    vote_id = Column(Integer, ForeignKey("votes.id"), primary_key=True)
    creation = Column(Text) 