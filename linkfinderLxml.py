from lxml import html
import requests
from urllib import parse


class AppCrawler:
    def __init__(self, start_url, depth):
        self.start_url = start_url
        self.depth = depth
        self.links = set()

    def crawl(self):
        self.get_links(self.start_url)
        return

    def get_links(self, url):
        start_page = requests.get(url)
        tree = html.fromstring(start_page.text)
        name = tree.xpath('//a/@href')
        for link in name:
            join = parse.urljoin(url, link).strip()
            # print ("##########" + join.strip() + "###########")

            if join[-1] == '/':  # to remove trailing backslash '/'
                join = join[:-1]  # to avoid duplicate hompage links
            if join in self.links:
                continue
            self.links.add(join)
        for l in self.links:
            print(l)
        print('\n')


crawler = AppCrawler("https://www.mkyong.com", 3)

crawler.crawl()