import requests

URL = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def get_post(self):
        r = requests.get(url=URL).json()
        return r
