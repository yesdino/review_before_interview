# coding:utf8
import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parse', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 获取页面中新的url列表
    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        links = soup.find_all('a', href=re.compile(r""))    # TODO
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    # 获取页面中想要的特定数据
    def _get_new_data(self, page_url, soup):
        res_data = {}       # 字典
        res_data['url'] = page_url

        node = soup.find('div', class="WB_text W_f14")
        res_data['first_title'] = node.get_text()

        return res_data

