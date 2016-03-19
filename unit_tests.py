'''
Created on Mar 19, 2016

@author: syed
'''
import unittest
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from assignment_with_argument import Users
from sqlalchemy.ext.declarative import declarative_base

class QueryTest(unittest.TestCase):
    engine = create_engine("sqlite:///DEMO.db")
    Session=sessionmaker(bind=engine)
    session=Session()
    
    def setUp(self):
        Base = declarative_base()
        Base.metadata.create_all(self.engine)
        self.session.query(Users).delete()
        self.session.commit()
        self.session.add(Users('AAAAA-BB-CC-DD-FEEGG'))
        self.session.commit()
        
    def test_query_users(self):
        expected=[Users('AAAAA-BB-CC-DD-FEEGG')]
        result=self.session.query(Users).all()[0]
        self.assertEqual(result.user_id,expected[0].user_id)
    
    def tearDown(self):
        Base = declarative_base()
        Base.metadata.drop_all(self.engine)
     
if __name__=="__main__":
    unittest.main()