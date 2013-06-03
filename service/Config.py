class Config:
    config = {}
    config['db_schema'] = "mysql" 
    config['db_user'] = "root" 
    config['db_password'] = ""
    config['db_host'] = "127.0.0.1"
    config['db_port'] = "3306"
    config['db_database'] = "pollit"
        
    config['flask_host'] = "localhost"

    def get_db_connection_string(self):
        if self.config['db_password'] == "":
            return "%s://%s@%s:%s/%s" % (self.config['db_schema'], self.config['db_user'], self.config['db_host'], self.config['db_port'], self.config['db_database'])
        else :
            return "%s://%s:%s@%s:%s/%s" % (self.config['schema'], self.config['user'], self.config['password'], self.config['host'], self.config['port'], self.config['database'])
        
    def get_flask_host(self):
        return self.config['flask_host'] 