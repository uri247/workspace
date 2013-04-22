import urllib
import jinja2
import os
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from utils import ReqHandler

jinja_environment = jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)) )


class Greeting(db.Model):
    """model an individual guest book entry with an author, content and date
    """
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
def guestbook_key(guestbook_name=None):
    """Constructs a datastore key for Guestbook entity
    """
    return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class MainPage(ReqHandler):
    def get(self):
        gbname = self.request.get('guestbook_name')
        query = Greeting.all().ancestor(guestbook_key(gbname)).order('-date')
        greetings = query.fetch(10)

        if users.get_current_user():
            url = users.create_login_url(self.request.uri)
            label = 'Logout'
        else:
            url = users.create_logout_url(self.request.uri)
            label = 'Login'
        
        d = {
            'greetings': greetings,
            'url': url,
            'label': label
            }
        
        template = jinja_environment.get_template('j.html')
        self.w( template.render(d) )


class Guestbook(ReqHandler):
    def post(self):
        gbname = self.request.get('guestbook_name')
        greet = Greeting(parent=guestbook_key(gbname))
        if users.get_current_user():
            greet.author = users.get_current_user()
        greet.content = self.request.get('content')
        greet.put()
        self.redirect('/j?' + urllib.urlencode( {'guestbook_name': gbname } ) )
    pass


routes = [
    ('/j', MainPage ),
    ('/jsi', Guestbook )
    ]
          

application = webapp.WSGIApplication( routes, debug=True )
     

