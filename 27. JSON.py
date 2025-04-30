
What is JSON : (JavaScript Object Notation)✔️

# JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute-value pairs and arrays. 

# It is a common data format with diverse uses in electronic data interchange, including that of web applications with servers.

# JSON is relatively easy to read and write, while also easy for software to parse and generate. 

# It is often used for "serializing structured data" and exchanging it over a network, typically between a server and web applications.

# JSON syntax { "name": "ramesh", "age": 22, "gender": "male", } In JSON, the data are in key/value pairs separated by a comma , . JSON was derived from JavaScript.

Python JSON:

# Python has a built in package called json, which is used to work with json data, so remember wherener you want to use json, you need to import json module and then json methods we can use.

Using 2 method we can use json as:

1) dumps(data)  ✔️- dumps() used to convert python objects (e.g.dictionary) into simple json string 

2) loads(data)  ✔️- loads() used to parse (convert) json string to again python objects


1) dumps(data): ✔️

import json 💡
# json we take use as package in pyhton therefore we need to import json package before use json methods

python_data = {'name': 'ramesh','degree':'Engineering'}

json_data = json.dumps(python_data)

# Now print and see data is converted into json format, data will show in double quote, it means data is showing as string.

print(json_data)

out put will be :👍

{"name": "ramesh","degree":"Engineering"}

# In output data should be in double quote means data showing as a string, now this is json string data



2) loads(data) : Used to parse json string into python objects.💡

json_data = '{"name": "ramesh","degree":"Engineering"}'

# Remember json data is string so as a string you need to pass data then only it will parse into python object using loads()

parsed_data = json.loads(json_data)
# loads(json_string_data) - s is string

print(parsed_data)

Out put will be:

{'name': 'ramesh', 'degree': 'Engineering'}
# Now above out put is Python Dictionary 

print(parsed_data["name"])
# Now json string is parsed into python dictionary so we can fetch data using key also

Out put will be:
ramesh




Python Object to JSON Data Conversion
|                 Python                 |  JSON  |
|:--------------------------------------:|:------:|
|                  dict                  | object |
|               list, tuple              |  array |
|                   str                  | string |
| int, float, int- & float-derived Enums | number |
|                  True                  |  true  |
|                  False                 |  false |
|                  None                  |  null  |










