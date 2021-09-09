from bs4 import BeautifulSoup
import requests

# find() method is used for single tag
# find_all() method is used for all tag present in html page or inside tag
# select() method is used for tagName.any attribute value or value of any attribute and can take more
# get() method is used for get key in the tags

# THIS TRY AND EXCEPTION FOR WEBSITE IF IS IS WRONG
try:
    req = requests.get("https://www.imdb.com/chart/top/")
    print(req.status_code) #it show status code that means successfull or error
    req.raise_for_status() #this is for capture the error of url is wrong

    soup = BeautifulSoup(req.content, 'html.parser') #html parser which is default by python
    # print(soup)

    # for data in soup.find('tbody').find_all('a'):
    #     print(data.get_text()) #get all the name of top 250 movies

    # src = soup.find('tbody') #/ soup.tbody i can find also from tag name

    # print(src.attrs) # find attribute

    # print(src.attrs['class']) # find value

    # print(soup.find('tbody').find_all('td',class_='posterColumn'))

    # for class_select in soup.find_all(class_ ='posterColumn'):
    #     print(class_select.name) #this prints the tags name where the posterColumn class is used


    # for items in soup.find('tbody').find_all(class_ = "posterColumn"):
    #     print(items.name,items.attrs)

    # for item in soup.find('tbody').select('td.titleColumn'): #td is a tag and titleColumn is value of class
    #     print("it returns the tag name: ",item.name)
    #     print("it returns the content of the tag: ",item.get_text())

    # link = soup.find('tbody').select('td.titleColumn a')
    # print(link[0].get('title')) # want to fetch data single so we can use index value

    # HERE I FETCH NAME, TITLES AND IMAGES
    for link in soup.find('tbody').select('td.titleColumn a'):
        for imgs in soup.select('td.posterColumn img'):
            print("NAMES:", link.get_text())
            print("TITLES:",link.get('title'))
            print("IMAGES:",imgs.get('src'))

    # here i just fetch images
    # images=[]
    # for imgs in soup.select('td.posterColumn img'):
    #     images.append(imgs.get('src'))
    # print(images)

except Exception as e:
    print(e,"This is a wrong URL")

