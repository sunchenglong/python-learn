
class DownloadAll():
    def __init__(self):
        pass
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.db = MySQLdb.connect("localhost", "root", "root", "sse", charset='utf8')
        self.cursor = self.db.cursor()

    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    pass
