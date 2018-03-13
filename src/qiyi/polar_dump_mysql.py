import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class PolarDumpMysql():
    def __init__(self, input_file):
        self.db = MySQLdb.connect("10.153.74.168", "qiyu", "qiyu.asd", "kitty", charset='utf8')
        self.cursor = self.db.cursor()
        self.dump_to_mysql(input_file=input_file)

    def dump_to_mysql(self, input_file):
        with open(input_file, 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                feedid, content = line.rstrip().split("\t")
                sql = "INSERT INTO kitty.polar_raw_sample (feed_id, content) VALUES ('%s', '%s')" % (feedid, content)
                print sql

if __name__ == '__main__':
    polarDumpMysql = PolarDumpMysql('kitty.data')
