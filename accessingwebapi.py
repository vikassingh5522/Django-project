import requests

URL = "http://127.0.0.1:8000/student_data"

data = requests.get(url=URL)

result = data.json()

# for x in result:
#   print x 

print(result[1])