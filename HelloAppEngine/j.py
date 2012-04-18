import cgi
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users


class Greeting(db.Model):
    """model an individual guest book entry with an author, content and date
    """
    author = db.UserProperty()
    #content = db.StringListProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
def guestbook_key(guestbook_name=None):
    """Constructs a datastore key for Guestbook entity
    """
    return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class ReqHandler(webapp2.RequestHandler):
    def __init__(self):
        pass
    def w(self,msg):
        self.response.out.write(msg)        

class MainPage(ReqHandler):
    def get(self):
        gbname = self.request.get('guestbook_name')
        query = Greeting.all().ancestor(guestbook_key(gbname)).order('-date')
        greet = query.fetch(10)
        
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {
            'greetings' : greet,
            'url': url,
            'url_linktext': url_linktext,
            }
        remplate = jinja_en
            
            
    
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


class Guestbook(ReqHandler):
    def post(self):
        gbname = self.request.get('guestbook_name')
        greet = Greeting(parent=guestbook_key(gbname))
        if users.get_current_user():
            greet.author = users.get_current_user()
        greet.content = self.request.get('content')
        greet.put()
        self.redirect('/?' + urllib.urlencode( {'guestbook_name': gbname } ) )
    pass


routes = [
    ('/data', MainPage ),
    ('/sign', Guestbook )
    ]
          

application = webapp2.WSGIApplication( routes, debug=True )
     

