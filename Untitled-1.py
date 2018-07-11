#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250'


def download_page(url):
    data = requests.get(url).content
    return data


def main():
    parse_html(download_page(DOWNLOAD_URL))


def parse_html(html):
    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).string
        print(movie_name)
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        parse_html(download_page(DOWNLOAD_URL + next_page['href']))
    return None


if __name__ == '__main__':
    main()
