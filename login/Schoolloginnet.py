import urllib
import urllib2
import re
import cookielib

def gethtml(htmlpage):
	page = urllib.urlopen(htmlpage)
	return page.read()
def post():
	postdata = urllib.urlencode({
		"user_login_name":"test",
		"user_password":"test",
		"x":"0",
		"y":"0"

			})
	return postdata

req = urllib2.Request(
		url = "http://1.2.3.4/login.php?url=",data = post(),)
respose = urllib2.urlopen(req)
cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
gethtml("http://1.2.3.4/login.php?")
print respose.read()
