"""#import json

# Python dictionary
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}

# Convert Python dictionary to JSON string
json_string = json.dumps(student)
print(json_string)
print(type(json_string))

# Write dictionary to JSON file
with open("student.json", "w") as f:
    json.dump(student, f)

print("JSON file created") """


import requests

# Free fake api

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

print (f"Name: {data[0]['name']}")
print (f"Email: {data[0]['email']}")
print (f"City: {data[0]['address']['city']}")