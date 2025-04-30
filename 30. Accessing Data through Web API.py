
Accessing data through REST Web API in another Seperate Application:

Create a new .py seperate file at any location as newapplication.py

import requests

# requests module is not in-built module of Python means while installation of Python requests module not added.

# we need to seperately install as:
# pip install requests or 
# pip3 install requests or 
# python -m pip install requests

pip install requests

Collecting requests
  Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)
     |████████████████████████████████| 63 kB 210 kB/s
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
     |████████████████████████████████| 140 kB 731 kB/s
Collecting idna<4,>=2.5
  Downloading idna-3.4-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 10 kB/s
Collecting charset-normalizer~=2.0.0
  Downloading charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2022.9.24-py3-none-any.whl (161 kB)
     |████████████████████████████████| 161 kB 3.3 MB/s
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2022.9.24 charset-normalizer-2.0.12 idna-3.4 requests-2.27.1 urllib3-1.26.12

# and then only through web api output will show in output window


URL = "http://127.0.0.1:8000/student_data"

# to get api details on your new page, you need to run existing project in terminal, then only new .py file can get this above URL.

data = requests.get(url=URL)

result = data.json()

print(result)




