import cookielib
import urllib
import urllib2


loginBaiduUrl = "http://www.cosos.cn/community/forum.php?mod=post&action=reply&fid=93&tid=2068&extra=&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"
para = {
    'message': 'dadsadaada',
    'seccodehash': 'cSG5PtpQ',
    'seccodemodid': 'forum::viewthread',
    'seccodeverify': 'dsaa',
    'posttime': '1476456501',
    'formhash': 'f6a77d48',
    'usesig': '1',
    'subject': ''
}

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
postData = urllib.urlencode(para)
req = urllib2.Request(loginBaiduUrl, postData)
req.add_header('Cache-Control', 'no-store, private, post-check=0, pre-check=0, max-age=0')
req.add_header('Content-Type', 'text/xml; charset=utf-8')
req.add_header('Connection', 'Keep-Alive')
req.add_header('Set-Cookie','tjpctrl=1476460028175; ljN2_2132_saltkey=XNDUKIHQ; ljN2_2132_lastvisit=1476436479; ljN2_2132_ulastactivity=7949gxQrhp57OEfljplO9sNvwzvxBa2%2F2AP%2FuX3Mni0GTXIPlOrR; ljN2_2132_auth=3aedGRypPzDe%2FIsguePRmTPRoaY5l%2FRaDupy0m%2BVyCoZqK1Xd2csMOb7BbuJfgdUEv4tKcyVmvDXua8ojEbbnXbm8Ig; ljN2_2132_lastcheckfeed=193871%7C1476440312; uchome_loginuser=iscasKitty; grouptitle=%E6%96%B0%E6%89%8B%E4%B8%8A%E8%B7%AF; os_nn=7lpmJLpvG26gs7IhYPHSPg%253D%253D; os_tt=htds%252B41X%252Br2ybEdCg7lrF0TMxFtRAI45neeWkhIWIfZivov5r%252Btqb7KYqPuM64to; os_ll=3CGWtLFmZ91UthTrE6RGSrSOrJXpfvWs5SoMp3cSe8Oa9l2eHr9i9ozjRmpFOQ7%252B; ljN2_2132_nofavfid=1; ljN2_2132_visitedfid=93; ljN2_2132_editormode_e=1; ljN2_2132_forum_lastvisit=D_93_1476456716; ljN2_2132_lip=159.226.5.129%2C1476456151; ljN2_2132_st_p=193871%7C1476458100%7C69d5a8c57ad091669c8a865906a50975; ljN2_2132_viewid=tid_2068; ljN2_2132_smile=1D1; ljN2_2132_seccode=630.0dc2cb8c4e4d92b945; ljN2_2132_dcaptchasig=h0115f7e6cc3b03b9afed4cde3ae0afeb048fb694c730f07b8d6d2d552f93d7e2520adacb16b5e5fe8df0d6d2ba77d47fa3d8d89c90cbd54f63c303cc0643474f9d; ljN2_2132_security_cookiereport=5de0KZBZzz8TDgIKIwoUdjjCtxF9POQD5X2Gs9bgmxrxpkId1brT; ljN2_2132_home_diymode=1; ljN2_2132_sendmail=1; ljN2_2132_onlineusernum=14; ljN2_2132_sid=G5PtpQ; _pk_id.1.c507=cd0240f0c2a60ecb.1476436998.2.1476458956.1476456279.; _pk_ses.1.c507=*; ljN2_2132_checkpm=1; ljN2_2132_lastact=1476458829%09misc.php%09patch')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
resp = opener.open(req)
print resp.read()
