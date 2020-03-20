# coding:utf8

from baike_spider import url_manager, html_downloader, html_parser,\
     html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()                # self.urls         : url管理器
        self.downloader = html_downloader.HtmlDownloader()  # self.downloader   : 下载器
        self.parser = html_parser.HtmlParser()              # self.parser       : 解析器
        self.outputer = html_outputer.HtmlOutputer()        # self.outputer     : 输出器

    def craw(self, root_url):
        count = 1                                               # 控制爬取数量
        self.urls.add_new_url(root_url)                         # 添加呆爬取的 url 进 url 管理器

        while self.urls.has_new_url():                          # 当 url 管理器有待爬取的 url 时
            # 页面中可能有url无法访问
            try:
                new_url = self.urls.get_new_url()               # 获取下一个待爬取的 url
                print('craw %d : %s' % (count, new_url))        # debug
                html_cont = self.downloader.download(new_url)   # 启动下载器来下载这个url的页面

                # 调用解析器来解析页面数据 得到新的url列表和页面数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)                # 将新的url列表补充进url管理器
                self.outputer.collect_data(new_data)            # 进行页面收集

                if count == 1000:
                    break

                count += 1
            except:
                print('craw failed')

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://weibo.com/u/2482557597?refer_flag=1005055013_&is_all=1"
    obj_spider = SpiderMain()       # 
    obj_spider.craw(root_url)       # 
