'''
Created on Mar 18, 2016

@author: syed
'''
import uuid
#import os
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation,sessionmaker
from sqlalchemy import funcfilter
from operator import and_

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
    def write_uuids(self):
        session = Session()
        with open("uuids.txt","w") as fp:
            for x in range(0,1000):
                uid=str(uuid.uuid1())
                fp.write(uid+"\n")
                #writing 100 uuids into db
                if  not x%10:
                    demo=Users(uid)
                    session.add(demo)
            try:           
                session.commit()
            except:
                print "Exception: couldnt write into db"
    
    def uuids_nomatch(self):
        nomatch_uuids=[]
        with open("uuids.txt","r") as fp:
            for one_uuid in fp:
                one_uuid=one_uuid.rstrip('\n')
                session = Session()
                if not list(session.query(select([func.count('*')],(Users.user_id==one_uuid)))[0])[0]:
                    #print "not in db"
                    nomatch_uuids.append(one_uuid)
        return nomatch_uuids

def main():
    obj=Demo()
    obj.write_uuids()
    nomatch_uuids=obj.uuids_nomatch()
    print nomatch_uuids
    print len(nomatch_uuids), "UUID's did not match"
    
if __name__ == "__main__": main()
