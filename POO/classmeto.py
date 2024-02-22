class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user , password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

p1 = Connection.create_with_auth('sergio' , 1234)

print(p1.user , p1.password)