from google.appengine.ext import db
import os
import random
import cgi
import sys
import json
import logging
import re

class Devlog(db.Model):
    iid = db.IntegerProperty()
    data = db.TextProperty()

def retrieve_id():
    query = Devlog.all()
    query.order("-iid")
    retrieved = 0
    for last_iid in query.run(limit=1):
        retrieved = last_iid.iid
    if retrieved == 0:
        new_iid = 1
    else:
        new_iid = retrieved + 1
    return new_iid
    

method = os.environ['REQUEST_METHOD']
try:
    needed_iid = int(os.environ["QUERY_STRING"])
except ValueError:
    pass

if method == 'GET':
    query = Devlog.all()
    query.order("-iid")
    query.filter("iid =",needed_iid)

    for fid in query.run():
        print("") #doesnt print anything if you dont echo null before starting
        print(fid.data)
        

elif method == 'POST':
    postdata = cgi.FieldStorage()
    filedata = postdata.getvalue('data')
    new_iid = retrieve_id()

    insert = Devlog()
    insert.iid = new_iid
    insert.data = db.Text(filedata)
    insert.put()

    print "wrote " + str(len(filedata)) + " bytes to id number = " + str(new_iid)
