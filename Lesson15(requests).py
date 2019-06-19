# import requests
#
# params = {
#     'key1':1,
#     'key2':2
# }
# r = requests.get
# ('https://httpbin.org/get', params = params)
#
# print(dir(r), type(r))
# print(r.text, r.url)
#
# data = {
#     'key1':1,
#     'key2':2
# }
# file = {"file": open(text.txt, 'rb')}
# r = requests.post
# ('https://httpbin.org/post', json = data)
#
# print(r.text, r.url)

import requests
from PIL import Image
from io import BytesIO

r = requests.get('https://api.github.com/events')

image_url = r.json()[-1]['actor']['avatar_url']

r = requests.get(image_url)

image_bytes = BytesIO(r.content)
image = Image.open(image_bytes)

image.save('avatar.png', 'png')