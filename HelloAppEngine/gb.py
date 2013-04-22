"""Guest book application
"""

import webapp2
import cgi

class RH(webapp2.RequestHandler):
    def w(self,st):
        self.response.out.write(st)
    

class MainPage(RH):
    def get(self):
        self.w("""
            <html>
                <body>
                    <form action="/sign" method="post">
                        <div><textarea name="content" rows="3" cols="60"></textarea></div>
                        <div><input type="submit" value="Sign Guestbook"></div>
                    </form>
                </body>
            </html>
            """)

class Guestbook(RH):
    def post(self):
        self.w('<html><body>You wrote:</pre>')
        self.w(cgi.escape(self.request.get('content')))
        self.w('</pre></body></html>')


routes = [
    ('/gb', MainPage ),
    ('/sign', Guestbook )
    ]
          

application = webapp2.WSGIApplication( routes, debug=True )

