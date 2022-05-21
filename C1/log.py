import datetime


def Log(key, comment):
    with open('D021_1.log', 'a') as f:
        f.write(" {0} --- {1} --- {2}\n".format(key, datetime.datetime.now(), comment))
        
