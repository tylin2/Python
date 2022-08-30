# Chapter 12
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
nostarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print("type(nostarchSoup): " + str(type(nostarchSoup)))
