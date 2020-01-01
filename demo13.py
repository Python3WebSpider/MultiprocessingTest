from multiprocessing import Pool
import requests
from requests.exceptions import ConnectionError


def scrape(url):
    try:
        print(requests.get(url))
    except ConnectionError:
        print(f'Error Occurred {url}')
    finally:
        print(f'URL {url} Scraped')


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'http://xxxyxxx.net'
    ]
    pool.map(scrape, urls)
