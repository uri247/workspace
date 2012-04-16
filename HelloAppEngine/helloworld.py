import webapp2

class MainPage(webapp2.RequestHandler):
    def w(self, s):
        self.response.out.write(s)
            
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.w('Hello, webapp World!\n')
        self.w('\n\n')
        dr = dir(self)
        for m in dr:
            self.w( m + '\n' )


application = webapp2.WSGIApplication( [('/', MainPage), ('/hi', MainPage)], debug=True )

