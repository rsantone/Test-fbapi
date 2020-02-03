from config.enums import *
from config.tools import Tools


class Test:
    api = Tools.get_api()

    def test_create_post(self):
        self.api.put_object("me", 'feed', message=Actions.PostMsg.value)

    def test_like_post(self):
        latest_post = Tools.get_latest_post(self.api)
        self.api.put_like(latest_post)

    def test_add_comment(self):
        latest_post = Tools.get_latest_post(self.api)
        self.api.put_comment(latest_post,message=Actions.CommentMsg.value)
    def test_update_post(self):
        latest_post = Tools.get_latest_post(self.api)
        self.api.request(latest_post + '?message=' + Actions.UpdateMsg.value, method='POST')

    def test_delete_post(self):
        latest_post = Tools.get_latest_post(self.api)
        self.api.delete_object(id=latest_post)
