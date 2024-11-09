####### this is not working AS WELL #######
import http.client
import urllib.parse

file_path = 'prog.in'

# Чтение содержимого файла
# with open(file_path, 'r') as file:
#     file_content = file.read()
file_content = "gg"
url = "webhook.site"
endpoint = "/2af2666e-4bc1-463a-a66e-ec1e7b0b4992"

conn = http.client.HTTPSConnection(url)

headers = {
    'Content-type': 'text/plain'  
}

conn.request("POST", endpoint, body=file_content, headers=headers)

response = conn.getresponse()
data = response.read()

# print(f'Status Code: {response.status}')
# print(f'Response Text: {data.decode()}')

conn.close()

# this is not working AS WELL
