import jinja2
import os
import socket
from google.appengine.ext import webapp
from utils import ReqHandler

jinja_env = jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)) )



class MainPage(ReqHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.w('Hello, webapp World!\n')
        self.w('\n\n')
        dr = dir(self)
        for m in dr:
            self.w( m + '\n' )


class EnvironPage(ReqHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        dic = {
            'host_name': socket.gethostname(),
            'env_vars': os.environ.items(),
        }
        
        template = jinja_env.get_template('env.html')
        page = template.render(dic)
        self.w(page)


application = webapp.WSGIApplication([
        ('/', MainPage),
        ('/hi', MainPage),
        ('/env', EnvironPage),
    ],
    debug=True )

