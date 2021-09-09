from bs4 import BeautifulSoup
import requests
req = requests.get("https://www.imdb.com/chart/top/")
# print(req)

soup = BeautifulSoup(req.content,"html.parser")
# print(soup.prettify()) #it pretify the html on output window
print(soup.title) #get the title

# print(soup.title.name) # get the title html tag

# print(soup.title.parent.name) # get the html tag

# print(soup.p) #to get the p tag

# print(soup.a) #get the a tag

# print(soup.findAll())
# print(soup.findAll())

print(soup.get_text()) #all the text from page