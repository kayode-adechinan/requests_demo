import requests

# http://docs.python-requests.org/en/master/

# request_with_authentication = requests.get('https://api.github.com/user', auth=('user', 'pass'))

get_request = requests.get('http://httpbin.org/ip')

print(get_request.json())

post_request = requests.post('http://httpbin.org/post', data={'movie': 'mystic river'})

print(post_request.json())

put_request = requests.put('http://httpbin.org/put', data={'movie': 'million dolar baby'})

print(put_request.json())

delete_request = requests.delete('http://httpbin.org/delete')
print(delete_request.json())

explore_get_request = requests.get('https://jsonplaceholder.typicode.com/albums')

print(explore_get_request.json())

explore_response = explore_get_request.json()
print(explore_response[1])
print(explore_response[1].keys())
