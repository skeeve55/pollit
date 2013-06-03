import flask  # @UnresolvedImport
from flask.ext.sqlalchemy import SQLAlchemy  # @UnresolvedImport


class FlaskApp:
    def __init__(self, connectionString, host):
        self.app = flask.Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = connectionString        
        self.app.config['POLLIT_SERVER_NAME'] = host        
        self.app.debug = True
        
        self.db = SQLAlchemy(self.app)
        
    def run(self):
        self.app.run(host=self.app.config['POLLIT_SERVER_NAME'])
        
    def get_db(self):
        return self.db
    
    def get_app(self):
        return self.app
    
    @self.app.route('/test2/')
    def test(self):
        return "hello, world"