from bs4 import BeautifulSoup
import requests
import time
import datetime
import os
import random

count = 0 
number = []
e = 0

if os.path.exists("./count_num.csv") == True:
    with open ("count_num.csv", "r", encoding='utf-8') as count_num:
        for j in count_num:
            cnt = j
    count = int((cnt.split(",")[0]))
    print ( "========== You've Downloaded  \t" + str(count) + "\t URLs ========== \n\n")
    time.sleep(5)    
else :
    count = 0

# yes file
if os.path.exists('./yes.csv') == False:
    with open("yes.csv", "w", encoding = 'utf-8') as yes_file:
        yes_file.write("{},{},{},{},{}".format("ID", "Company", "iframe_URL", "Time","\n"))

if os.path.exists('./no.csv') == False:
    # no_file
    with open("no.csv", "w", encoding = 'utf-8') as no_file:
        no_file.write("{},{},{},{},{}".format("ID", "Company", "iframe_URL", "Time","\n"))

if os.path.exists('./img.csv') == False:
    # no_file
    with open("img.csv", "w", encoding = 'utf-8') as img_file:
        img_file.write("{},{},{},{},{}".format("ID", "Company", "iframe_URL", "Time","\n"))

with open ("crawl_iframe.csv", "r", encoding='utf-8') as file_0:
    with open ("count_num.csv", "a", encoding='utf-8') as cnt_file:
        for line in file_0:
            now = datetime.datetime.now()
            if line.split(",")[3] == "iFrame_URL" or int(line.split(",")[0]) <= count :
                continue
            else:
                url = line.split(",")[3]
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                a = soup.select('div.artTplInner table')

                if len(a) == 0 :
                    b = soup.select('td.detailTable table')
                    if len(b) != 0:
                        with open("no.csv", "a", encoding = 'utf-8') as no_append_file:
                            no_append_file.write("{},{},{},{},{}".format(line.split(",")[0], line.split(",")[1], line.split(",")[3], now.strftime('%Y-%m-%d %H:%M:%S'),"\n")) 
                            cnt_file.write("{},{},{},{}".format(line.split(",")[0], line.split(",")[1], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                          
                            print ("============>>>>",line.split(",")[0],"<<<<<========== NO.csv =================================", b , "b","\n", "================================ NO.csv ===========>>>>",line.split(",")[0],"<<<<<====================== \n",)
                            
                            time.sleep((random.randrange(4, 12)))
                        

                    else :
                        c = soup.select('td.detailTable p')
                        d = soup.select('td.detailTable img')
                        if len(c) != 0 or len(d) != 0:
                            c.append(d)
                            with open("img.csv", "a", encoding = 'utf-8') as img_append_file:
                                img_append_file.write("{},{},{},{},{}".format(line.split(",")[0], line.split(",")[1],line.split(",")[3],now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                                cnt_file.write("{},{},{},{}".format(line.split(",")[0], line.split(",")[1], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                                print ("=========>>>>", line.split(",")[0],"<<<<<============= IMG.csv =================================", c,"c", "\n", "================================ IMG.csv ========>>>>",line.split(",")[0],"<<<<<============ \n")
                                
                                time.sleep((random.randrange(4, 12)))
                            continue
                        else :  
                            print ("ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            exit()
                        
                    continue

                k = a[0]

                heads = k.select('thead tr th')
                data = k.select('tbody tr td')
                with open("yes.csv", "a", encoding = 'utf-8') as yes_add_file:
                    yes_add_file.write("{},{},{},{},{}".format(line.split(",")[0], line.split(",")[1], line.split(",")[3], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                    cnt_file.write("{},{},{},{}".format(line.split(",")[0], line.split(",")[1], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                        
                    
                print ("===========>>>>",line.split(",")[0],"<<<<<========== YES.csv ==============================" , heads , data , "\n", "=========================== YES.csv ========>>>>",line.split(",")[0],"<<<<<============== \n" )
                
                time.sleep((random.randrange(4, 12)))