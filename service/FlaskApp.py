import flask  # @UnresolvedImport
from flask.ext.sqlalchemy import SQLAlchemy  # @UnresolvedImport

from Config import Config
from DataAccess import DataAccess

class FlaskApp:
    def __init__(self):
        # Config
        self.config = Config()
        
        # Create Flask Application
        self.app = flask.Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.config.get_db_connection_string()       
        self.app.debug = True
        
        # Create Database with Alchemy, Session and our DataAccess
        self.db = SQLAlchemy(self.app)
        self.dataAccess = DataAccess(self.db)
        
        # Create Url routing
        self.app.add_url_rule('/', 'get_all_polls_as_html', self.get_all_polls_as_html)
        self.app.add_url_rule('/polls', 'get_all_polls_as_jason', self.get_all_polls_as_jason)
        self.app.add_url_rule('/test', 'get_test', self.get_test)
        
    # Html
    def get_all_polls_as_html(self):
        return flask.render_template('index.html', polls=self.dataAccess.get_all_polls())
    
    # Service  
    def get_test(self):
        try:
            self.dataAccess.insert_user_vote(1, 2);
        except: 
            self.db.session.rollback()
        finally:    
            return flask.jsonify({"count" : self.dataAccess.get_user_votes_for_vote(2)})
          
    def get_all_polls_as_jason(self):
        return flask.jsonify({"polls" : self.dataAccess.get_all_polls()})
    
    # Run
    def run(self):
        self.app.run(host=self.config.get_flask_host(), port=self.config.get_flask_port())
