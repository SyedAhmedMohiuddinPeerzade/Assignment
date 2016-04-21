'''
Created on Mar 19, 2016

@author: Syed
'''
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
import os

Base = declarative_base()

class Users(Base):
    __tablename__="users"
    user_id=Column(String(36),nullable=False,primary_key=True)
    def __init__(self,uuid):
        self.user_id=uuid

#engine = create_engine("sqlite:///:memory:",echo=True)
'''above commented line is for using in memory DB for faster access,
for persistent DB we can use the below line. We should comment any one of them as per requirement
'''
engine = create_engine("sqlite:///DEMO.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class Demo:
    
    def __init__(self):
        pass
       
    def uuids_nomatch(self):
        session = Session()
        nomatch_uuids=[]
        with open(sys.argv[1],'r') as fp:
            for one_uuid in fp:
                one_uuid=one_uuid.rstrip('\n')
                if not list(session.query(select([func.count('*')],(Users.user_id==one_uuid)))[0])[0]:
                    nomatch_uuids.append(one_uuid)
        return nomatch_uuids
                
    def check_path(self):
        try:
            arg1=sys.argv[1]
        except IndexError:
            print "path to uuids.txt file not provided as argument\n....exiting..."
            exit()
        if not os.path.exists(sys.argv[1]):
            print "Invalid path or uuids.txt file does not exist"
            exit()

def main():        
    obj=Demo()
    obj.check_path()
    nomatch_uuids=obj.uuids_nomatch()
    print nomatch_uuids
    print len(nomatch_uuids), "UUID's did not match"

if __name__ == "__main__": main()
