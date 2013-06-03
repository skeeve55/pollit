from DbPoll import DbPoll
from DbUserVote import DbUserVote
from DbUser import DbUser  # @UnusedImport
from DbVote import DbVote  # @UnusedImport

class DataAccess:      
    def __init__(self, db):
        self.db = db
     
    def get_all_polls(self):
        result = []
        
        for response in self.db.session.query(DbPoll):
            poll = {}
            poll['id'] = response.id
            poll['topic'] = response.topic
            poll['creation'] = response.creation.strftime('%d.%m.%Y')
            poll['user'] = response.user.username
            
            poll['votes'] = []
            for vote in response.votes:
                poll['votes'].append((vote.id, vote.vote, self.get_user_votes_for_vote(vote.id)))        
            
            result.append(poll)
        return result

    def get_user_votes_for_vote(self, vote_id):
        return self.db.session.query(DbUserVote).filter(DbUserVote.vote_id == vote_id).count()                
    
    def insert_user_vote(self, user_id, vote_id):
        new_user_vote = DbUserVote()
        new_user_vote.user_id = user_id
        new_user_vote.vote_id = vote_id
        self.db.session.add(new_user_vote)
        self.db.session.commit()
