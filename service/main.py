import flask
import data
import time
import logging

from werkzeug._internal import _log
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func

config = {}
config['schema'] = "mysql" 
config['user'] = "root" 
config['password'] = ""
config['host'] = "127.0.0.1"
config['port'] = "3306"
config['database'] = "pollit"

dbConnectionString = "%s://%s@%s:%s/%s" % (config['schema'], config['user'], config['host'], config['port'], config['database'])
#dbConnectionString = "%s://%s:%s@%s:%s/%s" % (config['schema'], config['user'], config['password'], config['host'], config['port'], config['database'])

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbConnectionString
app.debug = True

db = SQLAlchemy(app)

def get_all_polls():
    polls = []
    
    for response in db.session.query(data.DbPoll):
        pollData = {}
        pollData['id'] = response.id
        pollData['topic'] = response.topic
        pollData['creation'] = response.creation.strftime('%d.%m.%Y')
        pollData['user'] = response.user.username
        
        pollData['votes'] = []
        for vote in response.votes:
            pollData['votes'].append((vote.id, vote.vote, get_user_votes_for_vote(vote.id)))        
        
        polls.append(pollData)
    return polls

def get_user_votes_for_vote(vote_id):
    result = db.session.query(data.DbUserVote).filter(data.DbUserVote.vote_id == vote_id).count()                
    return result

def insert_user_vote(user_id, vote_id):
    new_user_vote = data.DbUserVote()
    new_user_vote.user_id = user_id
    new_user_vote.vote_id = vote_id
    db.session.add(new_user_vote)
    db.session.commit()

@app.route('/test/')
def return_test():
    try:
        insert_user_vote(1, 2);
    except: 
        db.session.rollback()
    finally:    
        return flask.jsonify({"count" : get_user_votes_for_vote(2)})
        
@app.route("/")
def return_all_polls_as_html():
    return flask.render_template('index.html', polls = get_all_polls() )

@app.route("/polls")
def return_all_polls_as_jason():
    return flask.jsonify({"polls" : get_all_polls()})

if __name__ == "__main__":
    app.run()

