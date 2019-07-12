import webapp2
import wsgiref.handlers
from controllers import Home


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}


app = webapp2.WSGIApplication([

    (r'/',Home.SignIn),
    ('/signup',Home.signup),
    ('/home',Home.home),
    ('/editDetails',Home.details),
    ('/editpost',Home.EditPost),
    ('/viewpost',Home.ViewPost),
    ('/search',Home.Search)

], debug=True, config = config)


