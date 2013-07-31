from Handler import *

class KidsHandler(Handler):
	def get(self):
		self.render('kids.html')

	def post(self):
		first_name = self.request.get('first_name')
		last_name = self.request.get('last_name')
		attending_service = self.request.get('attending_service')
		attending_party = self.request.get('attending_party')
		shirt_size = self.request.get('shirt_size')
		# error check form
		if first_name == '' or last_name == '' or attending_service == '' or attending_party == '' or shirt_size == '':
			self.render('kids.html', error=True)
		else:
			UserDatabase.addKid(first_name, last_name, attending_service, attending_party, shirt_size)
			self.render('submitted.html')

class IntownHandler(Handler):
	def get(self):
		self.render('intown.html')

	def post(self):
		first_name = self.request.get('first_name')
		last_name = self.request.get('last_name')
		attending_service = self.request.get('attending_service')
		attending_party = self.request.get('attending_party')
		# error check form
		if first_name == '' or last_name == '' or attending_service == '' or attending_party == '':
			self.render('intown.html', error=True)
		else:
			UserDatabase.addIntown(first_name, last_name, attending_service, attending_party)
			self.render('submitted.html')


class OutoftownHandler(Handler):
	def get(self):
		self.render('outoftown.html')

	def post(self):
		first_name = self.request.get('first_name')
		last_name = self.request.get('last_name')
		attending_service = self.request.get('attending_service')
		attending_party = self.request.get('attending_party')
		attending_dinner = self.request.get('attending_dinner')
		attending_brunch = self.request.get('attending_brunch')
		# error check form
		if first_name == '' or last_name == '' or attending_service == '' or attending_party == '' or attending_dinner == '' or attending_brunch == '':
			self.render('outoftown.html', error=True)
		else:
			UserDatabase.addOutOfTown(first_name, last_name, attending_service, attending_party, attending_dinner, attending_brunch)
			self.render('submitted.html')