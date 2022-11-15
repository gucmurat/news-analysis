from scrapy import cmdline
from datetime import date
import os

today = str(date.today())
try:
    os.system(f"rm json_files/news{today}.json")
except:
    pass

cmdline.execute(f"scrapy crawl news -o json_files/news{today}.json".split())