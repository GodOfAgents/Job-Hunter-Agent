import requests

url = 'http://127.0.0.1:5000/submit'
data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'phone': '123-456-7890',
    'location': 'San Francisco',
    'frequency': 'daily'
}
files = {
    'resume': open('dummy_resume.txt', 'rb')
}

response = requests.post(url, data=data, files=files)

print(response.status_code)
print(response.json())