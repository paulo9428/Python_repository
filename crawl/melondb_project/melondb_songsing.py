from bs4 import BeautifulSoup
import requests
import re
import pprint
import pymysql
import time
import json


def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dl014532.',
        port=3306,
        db=db,
        charset='utf8')

