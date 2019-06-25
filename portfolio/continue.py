from bs4 import BeautifulSoup
import requests
import makeurl
import time
import random
import datetime


number = []
now = datetime.datetime.now()


with open ("crawl_site.csv", "r", encoding='utf-8') as file: 
    with open("crawl_iframe.csv", mode="r", encoding='utf-8') as file2:
        for i in file2:
            if i.split(",")[0] == "ID":
                continue
            else:
                number.append(int(i.split(",")[0]))
                number.sort(reverse=True)
    with open("crawl_iframe.csv", mode="a", encoding='utf-8') as add_file:
        none_count = 0
        for line in file:
            if int(line.split(",")[0]) <= number[0] :
                continue
            else :  
                now = datetime.datetime.now()  
                result = makeurl.request_url(line.split(",")[1], '#gib_frame')
                if result == "none":
                    none_count += 1
                    time.sleep(4)
                    print ("ERROR!!!!", none_count)
                    if none_count == 20:
                        print ("ERRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRR")
                        exit()
                    continue
                else : 
                    add_file.write("{},{},{},{},{},{}".format(line.split(",")[0],line.split(",")[2],line.split(",")[1], result, now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                    print (line.split(",")[1],"=======================>",line.split(",")[0], "\n\n")
                    time.sleep(random.randrange(4, 12))
                    none_count = 0