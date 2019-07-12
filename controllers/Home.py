import os
from google.appengine.ext.webapp import template
from google.appengine.api import search
from models.Users import Users
from models import Posts
from controllers import Handler


class home(Handler.BaseHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../templates/main.html')
        users = Users().query(Users.Users.email == self.session.get('email')).get()
        self.response.out.write(template.render(path, {'users':users}))




class signup(Handler.BaseHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../templates/signup.html')
        self.response.out.write(template.render(path, {}))
    def post(self):
        new_user = Users.Users()
        new_user.firstName = self.request.get('firstname')
        new_user.lastName = self.request.get('lastname')
        new_user.email = self.request.get('email')
        new_user.password = self.request.get('password')
        new_user.put()
        self.redirect('/')


class details(Handler.BaseHandler):

    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../templates/details.html')
        users = Users.Users().query(Users.Users.email == self.session.get('email')).get()
        template_var = {'users' : users}
        self.response.out.write(template.render(path, template_var))


    def post(self):
        users = Users.Users().query(Users.Users.email == self.session['email']).get()
        users.firstName = self.request.get('firstname')
        users.lastName = self.request.get('lastname')
        users.password = self.request.get('password')
        users.email = self.request.get('email')
        users.put()
        self.redirect('/home')

class EditPost(Handler.BaseHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../templates/editPost.html')
        users = Users.Users().query(Users.Users.email == self.request.get('email')).get()
        templates_var = {'users' : users}
        self.response.out.write(template.render(path, templates_var))

    def post(self):
        Posts.Post.addPost(self.request.get('post'),self.request.get('subject'))
        self.redirect('/home')


class ViewPost(Handler.BaseHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../templates/view.html')
        post_query = Posts.Post().query().order(-Posts.Post.date)
        posts = post_query.fetch()
        template_values = {
            'posts': posts
        }
        self.response.out.write(template.render(path, template_values))

class Search(Handler.BaseHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../templates/search.html')
        self.response.out.write(template.render(path, {}))
    def post(self):
        ##compiled_query = search.Query(json.dumps(self.request.get('query')))
        index = search.Index('mypost')
        results = index.search(self.request.get('query'))
        ##results = results._results[0].fields[0]._value
        path = os.path.join(os.path.dirname(__file__), '../templates/search.html')

        main_dict = {}
        for res in results:
            my_dict = {}
            for fields in res.fields:
                my_dict[fields.name] = fields.value
            main_dict[res._doc_id]=my_dict
        main_dict = main_dict

        template_values = {'results':main_dict}


        self.response.out.write(template.render(path, template_values))


