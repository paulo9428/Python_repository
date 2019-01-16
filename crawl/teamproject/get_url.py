from bs4 import BeautifulSoup
import requests
import makeurl
import time
import random
import datetime


none_count = 0
with open ("crawl_site.csv", "r", encoding='utf8') as file:
	with open ("crawl_iframe.csv", "w", encoding='utf8') as file2:
		file2.write("{},{},{},{},{},{}".format("ID","Company_name", "URL", "iFrame_URL", "Time", "\n"))
		for line in file:
			now = datetime.datetime.now()  
			result = makeurl.request_url(line.split(",")[1], '#gib_frame')
			if result == "none":
				none_count += 1
				print ("ERROR!!!!", none_count)
				if none_count == 20:
					print ("ERRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRR")
					exit()
				continue
			else:
				file2.write("{},{},{},{},{},{}".format(line.split(",")[0],line.split(",")[2],line.split(",")[1], result,now.strftime('%Y-%m-%d %H:%M:%S'), "\n"))
				print (line.split(",")[1],"=======================>",line.split(",")[0], "\n\n")
				time.sleep(random.randrange(2, 14))
				none_count = 0