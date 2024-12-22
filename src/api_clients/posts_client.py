from src.core.request_handler import RequestHandler
from src.config.config_reader import get_base_url

class PostsClient:
    base_url = f"{get_base_url()}/posts"

    @staticmethod
    def get_posts():
        """Fetch all posts"""
        return RequestHandler.get(PostsClient.base_url)

    @staticmethod
    def get_post(post_id):
        """Fetch a single post by its ID"""
        return RequestHandler.get(f"{PostsClient.base_url}/{post_id}")

    @staticmethod
    def create_post(data):
        """Create a new post"""
        return RequestHandler.post(PostsClient.base_url, data=data)
