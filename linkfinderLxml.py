from lxml import html
import requests
from urllib import parse


class AppCrawler:
    def __init__(self, start_url, url, depth):
        self.start_url = start_url
        self.url = url
        self.depth = depth
        self.links = set()

    def crawl(self):
        self.get_links(self.start_url, self.url)
        return

    def get_links(self, base_url, url):
        try:
            start_page = requests.get(url)
            tree = html.fromstring(start_page.text)
            name = tree.xpath('//a/@href')
            for link in name:
                join = parse.urljoin(base_url, link).strip()
            # print ("##########" + join.strip() + "###########")

                if join[-1] == '/':  # to remove trailing backslash '/'
                    join = join[:-1]  # to avoid duplicate hompage links
                if join in self.links:
                    continue
                if base_url not in join:
                    continue
                self.links.add(join)
            # for l in self.links:
            #     print(l)
            # print('\n')

        except:
            print("Error Crawling page")

    def getLinks(self):
        return self.links

#
#
# crawler = AppCrawler("https://www.mkyong.com", "https://www.mkyong.com", 3)
#
# crawler.crawl()