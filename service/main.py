import flask
import DataAccess

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

dataAccess = DataAccess.DataAccess(db)

@app.route('/test/')
def return_test():
    try:
        dataAccess.insert_user_vote(1, 2);
    except: 
        db.session.rollback()
    finally:    
        return flask.jsonify({"count" : dataAccess.get_user_votes_for_vote(2)})
        
@app.route("/")
def return_all_polls_as_html():
    return flask.render_template('index.html', polls = dataAccess.get_all_polls() )

@app.route("/polls")
def return_all_polls_as_jason():
    return flask.jsonify({"polls" : dataAccess.get_all_polls()})

if __name__ == "__main__":
    app.run(host="localhost")

