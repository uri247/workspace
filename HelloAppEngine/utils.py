from google.appengine.ext import webapp

class ReqHandler(webapp.RequestHandler):
    def w(self,msg):
        self.response.out.write(msg)        

