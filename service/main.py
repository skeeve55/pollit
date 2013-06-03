import flask  # @UnresolvedImport
from flask.ext.sqlalchemy import SQLAlchemy  # @UnresolvedImport

from Config import Config
from DataAccess import DataAccess
from FlaskApp import FlaskApp

config = Config()
flaskApp = FlaskApp(config.get_db_connection_string(), config.get_flask_host())
app = flaskApp.get_app()
db = flaskApp.get_db()
dataAccess = DataAccess(db)

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
    flaskApp.run()
