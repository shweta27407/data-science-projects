import requests
import os 
from PIL import Image
from IPython.display import IFrame

#  make a GET request via the method get to www.ibm.com:
url = "https://www.ibm.com/"
r = requests.get(url)

print(" Response : \n", r)  # response [200] means the request was successful

print(r.status_code)
print(r.request.headers)
print("request body: \n", r.request.body)


# view the HTTP response header using the attribute headers. 
# This returns a python dictionary of HTTP response headers.
header = r.headers
print("\nHeaders : \n", header)
print("\nDate : \n", header['date'])
print("\n Content-Type : \n", header['Content-Type'])
print("\nEncoding : \n", r.encoding)
print("\nText : \n", r.text)

# url of image
image_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
image_r = requests.get(image_url)

# response header
print("\nImage Response header : \n", image_r.headers)

print("\nImage content type : \n", image_r.headers['Content-Type'])
#print("\n content \n", image_r.content)

# An image is a response object that contains the image as a bytes-like object. 
# As a result, we must save it using a file object. 
# First, we specify the file path and name

path = os.path.join(os.getcwd(), 'image_ibm_downloaded.png')

#  in order to access the body of the response we use the attribute content 
# then save it using the open function and write method
with open(path, 'wb') as file:
    file.write(image_r.content)

# Display the image
img = Image.open(path)

#print("img" , img)    # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=400x400 at 0x7F8D3C0D3D90>
#img.show() # opens the image in the default image viewer

'''
Dowload a text file
'''

text_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
text_r = requests.get(text_url)

text_file_path = os.path.join(os.getcwd(), 'text_file_downloaded.txt')
with open(text_file_path, 'wb') as f:
    f.write(text_r.content)

url_get = 'http://httpbin.org/get'
payload = {"name": "Joseph", "ID": "123"}
r = requests.get(url_get, params=payload)

print("\n request text", r.url)
print("\n request text", r.text)
print("\nRequest body: \n", r.request.body)

print("\n status code: \n", r.status_code)
print("\n headers: \n", r.headers)
print("\n content headers: \n", r.headers['Content-Type'])

print("\n json: \n", r.json())
print("\n json args: \n", r.json()['args'])

'''
POST request
'''
url_post = 'http://httpbin.org/post'
r_post = requests.post(url_post, data=payload)

print("\n post request body : \n", r_post.request.body)
print("\n post response text : \n", r_post.text)
