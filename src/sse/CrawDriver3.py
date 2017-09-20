import datetime
from SseCraw import SseCraw


def main():
    begin = datetime.date(2016, 7, 1)
    end = datetime.date(2017, 1, 1)
    sse = SseCraw()
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        sse.craw_all_page(str(day))
        print "====>" + str(day) + " have run done"


if __name__ == '__main__':
    main()
