import mongoengine


class Database:

    def __init__(self):
        try:
            self.db = mongoengine.connect('walletSys', host='fpl_mongodb_1:27017')
            print('db connected')
        except Exception as e:
            print('something went wrong' + e)

    def db_client(self):
        return self.db
