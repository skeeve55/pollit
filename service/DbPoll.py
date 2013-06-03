from service.DbBase import Base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Text
from sqlalchemy.orm import relationship

class DbPoll(Base):
    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    topic = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser")  
    votes = relationship("DbVote")
    creation = Column(Text)  