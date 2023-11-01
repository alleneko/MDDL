import json
import os
from pprint import pprint
import random
import requests
import time
import sys

from chapter import Chapter

# Config
chapter_id = "edda7db0-7dbe-41fc-ae49-5d8860b1beea"
manga = "The World God Only Knows"
data_mode = "data"







def progress_bar():
	seconds = random.randint(5, 10)
	for second in range(0, seconds):
		print("\r{}".format(str(int((second + 1) / seconds * 100))), end="%")
		sys.stdout.flush()
		time.sleep(1)
	print()

chapter = Chapter(chapter_id, data_mode)


chapter.get_chapter()

# print(chapter.download_page)

time.sleep(5)
for num, page in enumerate(chapter.pages):
	chapter.download(page, manga, num + 1)
	print("Page {} downloaded.".format(str(num + 1)))
	progress_bar()

