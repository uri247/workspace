"""Fall Rectangle (fallrec) - a storage for files, using the google blobstore
"""
import os
import jinja2
from google.appengine.ext import blobstore
from google.appengine.ext import webapp
from utils import ReqHandler

jinja_environment = jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)) )

class MainPage(ReqHandler):
    def get(self):
        up_url = blobstore.create_upload_url('/fallrec/upload')
        template = jinja_environment.get_template('fallrec.html')
        context = {
            'up_url': up_url,
            'title': 'Fall Rectangle',
        }
        self.w( template.render(context))


class UploadHandler(ReqHandler):
    def get(self):
        pass
    
    def post(self):
        pass
    

routes = [
    ('/fallrec', MainPage ),
    ('/fallrec/upload', UploadHandler ),
    ]
  

application = webapp.WSGIApplication( routes, debug=True )

