import cookielib
import urllib2

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.cosos.cn/community/member.php?mod=logging&action=login")
cookie.save(ignore_discard=True, ignore_expires=True)   