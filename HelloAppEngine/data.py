import cgi
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users
from utils import ReqHandler

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
        self.w('<html><head><title>Using data</title></head><body>')
        gbname = self.request.get('guestbook_name')
        greetings = db.GqlQuery(
            "SELECT * "
            "FROM Greeting "
            "WHERE ANCESTOR IS :1 "
            "ORDER BY date DESC LIMIT 10",
            guestbook_key(gbname)
            )
        for greet in greetings:
            if greet.author:
                self.w( '<b>%s</b> wrote: ' % greet.author.nickname() )
            else:
                self.w( 'Anonymous person wrote: ' )
            self.w( '<blockquote>%s</blockquote>' % cgi.escape(greet.content) )
        
        self.w( """
              <form action="/si?%s" method="post">
                  <div><textarea name="content" rows="3" cols="60"></textarea></div>
                  <div><input type="submit" value="Sign Guestbook"></div>
              </form>
              <hr>
              <form>
                  Guestbook name: <input value="%s" name="guestbook_name">
                  <input type="submit" value="switch">
              </form>
            </body></html>
            """ % ( urllib.urlencode( {'guestbook_name': gbname} ), cgi.escape(gbname) )
            )

class Guestbook(ReqHandler):
    def post(self):
        gbname = self.request.get('guestbook_name')
        greet = Greeting(parent=guestbook_key(gbname))
        if users.get_current_user():
            greet.author = users.get_current_user()
        greet.content = self.request.get('content')
        greet.put()
        self.redirect('/data?' + urllib.urlencode( {'guestbook_name': gbname } ) )
    pass


routes = [
    ('/data', MainPage ),
    ('/si', Guestbook )
    ]
          

application = webapp2.WSGIApplication( routes, debug=True )
     

