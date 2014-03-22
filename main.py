import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('[TODO: run Java sample]')

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
