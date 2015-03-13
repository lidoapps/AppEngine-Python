import webapp2
form = """
<form method = "Post" action = "/test">
	<input name="q">
	<input type = "submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

class TestHandle(webapp2.RequestHandler):
	def post(self):
		#q = self.request.get("q")
		#self.response.write(q)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(self.request)

application = webapp2.WSGIApplication([
    ('/', MainPage), 
    ('/test',TestHandle)], debug=True)