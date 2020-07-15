
from database.DataBase import Temperature

class Query(object):
    def __init__(self, session):
        self.session = session
        self.data_frame = None

    def query(self):
        # self.data_frame = self.session.query(Temperature).filter_by(item='item_A').all() #方式一
        self.data_frame = None #方式二:pandas

        print(self.data_frame)
