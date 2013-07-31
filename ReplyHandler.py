from Handler import *

class ReplyHandler(Handler):
	def get(self):
		users = ndb.gql("SELECT * FROM User")
		kids = ndb.gql("SELECT * FROM Kid")
		intowns = ndb.gql("SELECT * FROM Intown")
		outoftowns = ndb.gql("SELECT * FROM OutOfTown")
		self.render('reply.html', kids=kids, intowns=intowns, outoftowns=outoftowns, users=users)