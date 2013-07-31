from Handler import *

class User(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)	

class Kid(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)
	shirt_size=ndb.StringProperty(required=True)

class Intown(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)

class OutOfTown(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)	
	attending_dinner = ndb.StringProperty(required=True)
	attending_brunch = ndb.StringProperty(required=True)

def addKid(fname, lname, attendings, attendingp, shirt):
	kid = Kid(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp, shirt_size=shirt)
	kid.put()
	user = User(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	user.put()

def addIntown(fname, lname, attendings, attendingp):
	intown = Intown(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	intown.put()
	user = User(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	user.put()

def addOutOfTown(fname, lname, attendings, attendingp, attendingd, attendingb):
	outoftown = OutOfTown(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp, attending_dinner=attendingd, attending_brunch=attendingb)
	outoftown.put()
	user = User(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	user.put()