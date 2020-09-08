from bs4 import BeautifulSoup
import requests

#html_file = open("C:/Users/TAHIR/Desktop/univelcity/beautiful soup/index.html","r")
#html_data = html_file.read()

#soup = BeautifulSoup(html_data,features="html.parser")
#print(soup)


#filter = soup.find("h3")
#print(filter.text)

# USING BEAUTIFUL SOUP WITH RESOURCES ON THE INTERNET
# jumia_url = "https://www.jumia.com.ng/smartphones/"
# jumia_request = requests.get(jumia_url)

# jumia_html = jumia_request.content
# #print(jumia_html)

# jumia_soup = BeautifulSoup(jumia_html,"html.parser")
# h3_filter = jumia_soup.find_all("h3")

# for product in h3_filter:
#     print(product.text)
#     print()


wikipedia_url = "https://www.google.com/search?q=wikipedia+nigeria&oq=wiki&aqs=chrome.2.69i59l3j69i57j0l4.8173j0j15&sourceid=chrome&ie=UTF-8"

wikipedia_request = requests.get(wikipedia_url)

wikipedia_html = wikipedia_request.content

# print(wikipedia_html

wikipedia_soup = BeautifulSoup(wikipedia_html,"html.parser")

h3_filter = wikipedia_soup.find_all("h3")

for content in h3_filter:
    print(content.text)
    print()

