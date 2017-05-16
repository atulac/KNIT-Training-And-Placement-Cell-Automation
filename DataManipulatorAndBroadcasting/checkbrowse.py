import urllib2

url = 'http://codeforces.com/problemset?order=BY_SOLVED_DESC'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('C:\Users\\atulac\Desktop\\obo-t17800628-33.html', 'w')
f.write(webContent)
f.close