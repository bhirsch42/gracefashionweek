from Handler import *

class ReplyHandler(Handler):
	def get(self):
		users = ndb.gql("SELECT * FROM User")
		self.render('reply.html', users=users)