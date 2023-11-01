
import os
import requests
import time


class Chapter:
	def __init__(self, chapter_id, data_mode):
		self.id = chapter_id
		self.data_mode = data_mode

	def get_chapter(self):
		self.data_page = requests.get("https://api.mangadex.org/chapter/" + self.id).json()
		time.sleep(5)
		self.download_page = requests.get("https://api.mangadex.org/at-home/server/" + self.id).json()
		self.hash = self.download_page["chapter"]["hash"]
		self.pages = self.download_page["chapter"]["data"] if self.data_mode == "data" else self.download_page["chapter"]["dataSaver"]
		self.chapter = self.data_page["data"]["attributes"]["chapter"]
		self.manga = self.data_page["data"]["relationships"][1]["id"]
		self.scanlator = self.data_page["data"]["relationships"][0]["id"]

	def download(self, page, manga, page_num):
		page_url = self.download_page["baseUrl"] + "/data/" + self.hash + "/" + page
		page_request = requests.get(page_url)
		page_content = page_request.content
		os.makedirs(manga + "/" + self.chapter, exist_ok=True)
		if page_request.ok:
			with open(manga + "/" + self.chapter + "/" + page, "wb+") as filename:
				filename.write(page_content)



	