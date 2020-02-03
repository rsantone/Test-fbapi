from config.enums import *
import pytest
import facebook

class Tools:

    @staticmethod
    def get_api():
        page_id = Data.PageId.value
        token = Data.Token.value
        graph = facebook.GraphAPI(token)
        my_pages = graph.get_object('me/accounts')
        page_access_token = None
        for page in my_pages['data']:
            if page['id'] == page_id:
                page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
        return graph

    @staticmethod
    def get_latest_post(api):
        latest_post = api.request('me' + '/posts?limit=1')
        return latest_post['data'][0]['id']