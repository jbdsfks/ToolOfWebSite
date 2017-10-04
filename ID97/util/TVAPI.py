import requests
from bs4 import BeautifulSoup


def get_download_list_by_id(tid):
    url_list = []
    url = "http://www.id97.com/videos/resList/{0}".format(tid)
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'lxml')
    for a in data.find_all('a', mid=tid):
        url_list.append(a.get('href'))
    return url_list


if __name__ == '__main__':
    get_download_list_by_id("618826")
