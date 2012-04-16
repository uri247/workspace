import webapp2
from google.appengine.api import users


class WhoAmI(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write( 'You are ' + user.nickname() )
        else:
            self.redirect( users.create_login_url(self.request.uri) )




routes = [
    ('/whoami', WhoAmI ),
    ]
          

application = webapp2.WSGIApplication( routes, debug=True )

