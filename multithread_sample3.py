from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import logging
import time
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [ %(levelname)s ] line %(lineno)d %(message)s')


def find_titles_of_each_page(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text)
    logging.info(url)
    return bs.select("div.title > a")



def main():
    start = time.time()
    with ThreadPoolExecutor(max_workers=50) as executor:
        for page in range(2000, 3300):
            url = "https://www.ptt.cc/bbs/CFantasy/index{}.html".format(page)
            executor.map(find_titles_of_each_page, (url,))
    end = time.time()
    time_diff = end - start
    logging.info("spent time: {} s".format(time_diff))


if __name__ == "__main__":
    main()



