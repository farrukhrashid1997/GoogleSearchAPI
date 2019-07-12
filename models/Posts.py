from google.appengine.ext import ndb
from google.appengine.api import search
class Post(ndb.Model):
    post = ndb.StringProperty()
    subject = ndb.StringProperty()
    user_key = ndb.KeyProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create_document(cls,post,subject):
        document = search.Document(
            fields=[search.TextField(name='subject',value=subject),
            search.TextField(name='post',value=post)])
        return document

    @classmethod
    def add_document_to_index(cls,document):
        index = search.Index('mypost')
        index.put(document)

    @classmethod
    def addPost(cls,post,subject):
        new = Post()
        new.post = post
        new.subject = subject
        new.put()
        document = cls.create_document(post,subject)
        cls.add_document_to_index(document)





