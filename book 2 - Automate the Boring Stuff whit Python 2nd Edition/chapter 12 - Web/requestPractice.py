# Chapter 12
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
'''
# status_code is one of attributes in Response object.
# if status_code == requests.codes.ok then means everything is normal.
# ok == 200, not_find == 404
print(res.status_code == requests.codes.ok)

# length of text
len(res.text)
print(res.text[:250])

# page is not be found.
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
#res.raise_for_status()
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
'''
# check  if download is success or not
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt','wb')
# inter_content() is to make sure requests will not
# spend too much memory on downloading a big file.
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
