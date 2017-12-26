import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class DownloadAll():
    def __init__(self, path):
        self.db = MySQLdb.connect("localhost", "root", "root", "sse", charset='utf8')
        self.cursor = self.db.cursor()
        self.download(path)

    def __del__(self):
        self.cursor.close()
        self.db.close()

    def download(self, path):
        sql = "select * from sse.crawl_result"
        self.cursor.execute(sql)
        table = self.cursor.fetchall()
        with open(path, 'w') as fp:
            for row in table:
                fp.write(",".join(map(lambda x: str(x), row)).encode('gb18030') + "\n")


if __name__ == '__main__':
    downloadAll = DownloadAll('crawl_result.csv')
