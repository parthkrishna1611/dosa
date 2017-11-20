#!/home/parth/anaconda3/bin/python


# import urllib3
import requests
from bs4 import BeautifulSoup
import sys
import os


# the slang
def main(slang):
	i = 0
	# slang = input('Enter the slang: ')
	slang = sys.argv[1]
	word1 = slang.split()
	b1 = "+"
	s1 = ""
	
	for i1 in word1:
		sa = i1
		s1 += sa+b1

	slang_final = s1
	slang_final = slang_final[:-1]
	url = "https://www.urbandictionary.com/define.php?term="+slang_final
	# print("-+-+-+-+-+-+-+-+-Urban Dictionary-+-+-+-+-+-+-+-+-")
	# print("The slang is: "+slang)
	# print("The urbandictionary link is: \n"+url)

	final_url = requests.get(url)
	soup = BeautifulSoup(final_url.content, "lxml")
	# print("-+-+-+-+-+-+-+-+-Urban Dictionary Meaning-+-+-+-+-+-+-+-+-")
	meaning = soup.find("div",attrs={"class":"meaning"}).text
	# print("\nMeaning: "+soup.find("div",attrs={"class":"meaning"}).text)
	print("\n"+meaning)
	example = soup.find("div",attrs={"class":"example"}).text
	# print("\nExample: "+soup.find("div",attrs={"class":"example"}).text)
	print("\n"+example)
	
	

	#if not os.path.isdir("/home/parth/Desktop/proj"):
	#	os.makedirs('/home/parth/Desktop/proj/')
		# os.system('mkdir proj')
	# if not os.path.isdir('mydir'):
   		# print('new directry has been created')
    	# os.system('mkdir mydir')
	# os.makedirs('/home/parth/Desktop/proj/')
	# os.chdir()
	

	# file operations
	
	file = open("/home/parth/Desktop/proj/meaning.txt", "w")
	file.write(meaning)
	file.close()
	
	
	file = open("/home/parth/Desktop/proj/example.txt", "w")
	file.write(example)
	file.close()

if __name__ == '__main__':
	main(sys.argv[1])
