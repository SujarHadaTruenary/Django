import requests

headers = {}
headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2MjIxMTkxLCJpYXQiOjE2OTYyMjA4OTEsImp0aSI6ImI3NjE5YTFjZDE0MTQ5YTViODI3NzYwYWVkYTAzY2VmIiwidXNlcl9pZCI6MX0.gS3ZT2NwGB-8vfhhdOxTwL4GozeFppfW0a1hU-yNPOg'
r = requests.get('http://127.0.0.1:8000/paradigm', headers=headers)

print(r.text)
