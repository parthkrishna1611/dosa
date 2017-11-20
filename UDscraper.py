# import urllib3
import requests
from bs4 import BeautifulSoup

i = 0
print("-+-+-+-+-+-+-+-+-Urban Dictionary-+-+-+-+-+-+-+-+-")

# the slang
slang = input('Enter the slang: ')
word1 = slang.split()
b1 = "+"
s1 = ""

for i1 in word1:
	sa = i1
	s1 += sa+b1

slang_final = s1
slang_final = slang_final[:-1]
url = "https://www.urbandictionary.com/define.php?term="+slang_final
print("-+-+-+-+-+-+-+-+-Urban Dictionary-+-+-+-+-+-+-+-+-")
print("The slang is: "+slang)
# print("The artist name is: "+s_artist)
print("The urbandictionary link is: \n"+url)

# scraper
#r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
final_url = requests.get(url)
soup = BeautifulSoup(final_url.content, "lxml")
print("-+-+-+-+-+-+-+-+-Urban Dictionary Meaning-+-+-+-+-+-+-+-+-")
print(soup.find("div",attrs={"class":"meaning"}).text)
print("Example: "+soup.find("div",attrs={"class":"example"}).text)

