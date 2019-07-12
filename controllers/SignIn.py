



class SignIn(Handler.BaseHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), '../templates/login.html')
        self.response.out.write(template.render(path, {}))
    def post(self):
        users = Users.Users().query(Users.Users.email == self.request.get('email')).get()
        if users.password == self.request.get('password'):
            self.session['email'] = self.request.get('email')
            self.session['password'] = self.request.get('password')
            self.redirect('/home')
        else:
            self.redirect('/wrong')