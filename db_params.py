from dotenv import load_dotenv
import os
load_dotenv()

class params:
    def __init__(self, user):
        self.user = user
        self.password = os.environ.get('password')
        self.host = os.environ.get('host')
        self.port = os.environ.get('port')
        self.database = os.environ.get('database')