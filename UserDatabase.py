from Handler import *

class User(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)	

def addUser(fname, lname, attendings, attendingp):
	user = User(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	user.put()