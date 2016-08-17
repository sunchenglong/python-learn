import base64
import datetime
import json
import urllib

class TestFishingTank(object):

    _baseurl = 'http://checkurl.phishtank.com'
    _checkurl = '/checkurl/'
    __apikey = '316f948978e2aefdd99cebf937bafb6f71538acdd41adba0bc41c7fee6fd2a60'

    def __init__(self):
        print "init"

    def check(self, url):
        urlencoded = base64.encodestring(url)
        post_data = urllib.urlencode(
            {'url': url,
             'format': 'json',
             'app_key': self.__apikey,
            })
        con = urllib.urlopen(self._baseurl + self._checkurl, post_data)
        data = json.loads(con.read())
        if 'errortext' in data.keys():
            print data['errortext']
        con.close()
        print data

if __name__ == '__main__':
    testFishingTank = TestFishingTank()
    testFishingTank.check("	http://www.adskite.com/anggun-mimpi.php")