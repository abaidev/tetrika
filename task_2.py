"""
TASK 2
"""
from urllib.parse import unquote
from bs4 import BeautifulSoup
from time import time
import asyncio
import aiohttp


async def task_2_async():
	alphabet = {}
	names = []
	url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

	async with aiohttp.ClientSession() as session:
		while True:
			async with session.get(url) as response:
				page = await response.read()
				soup = BeautifulSoup(page, 'html.parser')
				names += soup.select('.mw-category.mw-category-columns .mw-category-group a')
				print(len(names))  # специально, чтобы видеть рост числа 
				link = soup.find('div', id='mw-pages').find('a', attrs={"title": "Категория:Животные по алфавиту"}, string="Следующая страница")
				if link is None:
					break
				url = 'https://ru.wikipedia.org' + unquote(link.get('href'))

	for name in names:
		if name.text[0] in alphabet:
			alphabet[name.text[0]] += 1
		else:
			alphabet[name.text[0]] = 1

	print(alphabet)
	return alphabet


if __name__ == '__main__':
	start = time()
	asyncio.run(task_2_async())
	print("Total time: ", time()-start)