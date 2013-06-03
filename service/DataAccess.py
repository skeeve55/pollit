from DbPoll import DbPoll
from DbUserVote import DbUserVote
from DbUser import DbUser
from DbVote import DbVote

class DataAccess:      
    def __init__(self, db):
        self.db = db
     
    def get_all_polls(self):
        polls = []
        
        for response in self.db.session.query(DbPoll):
            pollData = {}
            pollData['id'] = response.id
            pollData['topic'] = response.topic
            pollData['creation'] = response.creation.strftime('%d.%m.%Y')
            pollData['user'] = response.user.username
            
            pollData['votes'] = []
            for vote in response.votes:
                pollData['votes'].append((vote.id, vote.vote, self.get_user_votes_for_vote(vote.id)))        
            
            polls.append(pollData)
        return polls

    def get_user_votes_for_vote(self, vote_id):
        result = self.db.session.query(DbUserVote).filter(DbUserVote.vote_id == vote_id).count()                
        return result
    
    def insert_user_vote(self, user_id, vote_id):
        new_user_vote = DbUserVote()
        new_user_vote.user_id = user_id
        new_user_vote.vote_id = vote_id
        self.db.session.add(new_user_vote)
        self.db.session.commit()
