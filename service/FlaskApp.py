import flask  # @UnresolvedImport
from flask.ext.sqlalchemy import SQLAlchemy  # @UnresolvedImport

from Config import Config
from DataAccess import DataAccess

class FlaskApp:
    def __init__(self):
        self.config = Config()
        
        self.app = flask.Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.config.get_db_connection_string()       
        self.app.config['POLLIT_SERVER_NAME'] = self.config.get_flask_host()
        self.app.debug = True
        
        self.db = SQLAlchemy(self.app)
        self.dataAccess = DataAccess(self.db)
        
        self.app.add_url_rule('/', 'return_all_polls_as_html', self.return_all_polls_as_html)
        self.app.add_url_rule('/polls', 'return_all_polls_as_jason', self.return_all_polls_as_jason)
        self.app.add_url_rule('/test', 'return_test', self.return_test)
        
    def run(self):
        self.app.run(host=self.app.config['POLLIT_SERVER_NAME'])
        
    def get_db(self):
        return self.db
    
    def get_app(self):
        return self.app    
    
    def return_all_polls_as_html(self):
        return flask.render_template('index.html', polls = self.dataAccess.get_all_polls() )
    
    def return_test(self):
        try:
            self.dataAccess.insert_user_vote(1, 2);
        except: 
            self.db.session.rollback()
        finally:    
            return flask.jsonify({"count" : self.dataAccess.get_user_votes_for_vote(2)})
            
    def return_all_polls_as_jason(self):
        return flask.jsonify({"polls" : self.dataAccess.get_all_polls()})