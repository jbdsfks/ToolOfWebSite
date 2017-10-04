import sys
from ID97 import get_download_list_by_id


def print_url_list(mid):
    url_list = get_download_list_by_id(mid)
    for url in url_list:
        print url


if __name__ == '__main__':
    mid = sys.argv[1]
    print_url_list(mid)

