import flask

from flask.ext.sqlalchemy import SQLAlchemy  # @UnresolvedImport
import data


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
        pollData['creation'] = response.creation.strftime('%d.%m.%Y %H:%M:%S')
        pollData['user'] = response.user.username
        polls.append(pollData)
    return polls
     
@app.route("/")
@app.route('/test')
def return_all_polls_as_html():
    return flask.render_template('index.html', polls = get_all_polls() )

@app.route("/polls")
def return_all_polls_as_jason():
    return flask.jsonify({"polls" : get_all_polls()})



if __name__ == "__main__":
    app.run()

