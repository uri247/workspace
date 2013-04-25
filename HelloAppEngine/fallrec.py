"""Fall Rectangle (fallrec) - a storage for files, using the google blobstore
"""
import os
import jinja2
import urllib
from google.appengine.ext import blobstore
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
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


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):
        pass
    
    def post(self):
        files = self.get_uploads('thefile')
        info = files[0]
        template = jinja_environment.get_template('fallrec-details.html')
        context = {
            'key': info.key(),
            'content_type': info.content_type,
            'filename': info.filename,
            'size': info.size,
            'textline': self.request.get('textline'),
            'link': '/fallrec/srv/%s' % info.key(),            
        }
        self.response.out.write( template.render(context))
        
    

class SrvHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)


routes = [
    ('/fallrec/?', MainPage ),
    ('/fallrec/upload', UploadHandler ),
    ('/fallrec/srv/([^/]+)?', SrvHandler ),

    ]
  

application = webapp.WSGIApplication( routes, debug=True )

