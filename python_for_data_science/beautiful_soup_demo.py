import requests
from bs4 import BeautifulSoup

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')

print(soup.prettify())

tag_object = soup.title
print("\ntag object: \n", tag_object)
print("\n tag object type: \n", type(tag_object))

tag_object_h3 = soup.h3
print("\ntag object h3: \n", tag_object_h3)

# child
tag_child = tag_object_h3.b
print("\ntag child: \n", tag_child)

# parent
tag_parent = tag_child.parent
print("\ntag parent: \n", tag_parent)
print("\n tag object : \n", tag_object_h3)

print("\n tag object parent: \n", tag_object_h3.parent)

#siblings
sibling_1 = tag_object_h3.next_sibling
print("\n sibling 1: \n", sibling_1)

sibling_2 = sibling_1.next_sibling
print("\n sibling 2: \n", sibling_2)

print("\n sibling 2 salary : \n", sibling_2.next_sibling)

# HTML attributes

tag_child_id = tag_child['id']
print("\n tag child id : \n", tag_child_id)

print("\n Attributes :\n", tag_child.attrs)
print("\n attributes using get method:\n", tag_child.get('id'))


