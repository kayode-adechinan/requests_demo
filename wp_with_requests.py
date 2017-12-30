import requests

post_requests = requests.post('http://cryts.mapridge.com/wp-json/wp/v2/users',
                              auth=('cryts', 'cryts'),
                              data={'username': 'thakib',
                                    'email': 'thakib@gmail.com',
                                    'password': 'thakib'})

print(post_requests.json())
