from config.enums import *
from config.tools import Tools

class Test():
    api = Tools.get_api()
    latest_post = None


    def test_create_post(self):
        self.api.put_object("me", 'feed', message=Actions.PostMsg.value)
        Test.latest_post = Tools.get_latest_post(Test.api)

    def test_like_post(self):
        self.api.put_like(Test.latest_post)

    def test_add_comment(self):
        self.api.put_comment(Test.latest_post,message=Actions.CommentMsg.value)
    def test_update_post(self):
        self.api.request(Test.latest_post + '?message=' + Actions.UpdateMsg.value, method='POST')

    def test_delete_post(self):
        self.api.delete_object(id=Test.latest_post)
