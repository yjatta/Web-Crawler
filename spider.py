from urllib.request import urlopen
from linkfinderLxml import AppCrawler
from general import *


class Spider:

    # class variables shared among all instances
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    # bugs
    # even upon error homepage still moving to crawled file
    # duplicate links on a page adding to crawled file

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = project_name + '/queue.txt'
        Spider.crawled_file = project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('first spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if Spider.domain_name not in page_url:
            Spider.queue.remove(page_url)

        elif page_url not in Spider.crawled:
            print(thread_name + " now crawling " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled " + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.get_links(page_url))
            Spider.queue.remove(page_url)  # remove crawled page from queue to avoid circular referencing
            Spider.crawled.add(page_url)  # add the remove page above to crawled set
            Spider.update_files()

    @staticmethod
    def get_links(page_url):
        finder = AppCrawler(Spider.base_url, page_url, 3)
        try:

            finder.crawl()

        except:
            print("Error cannot crawl page. Make sure you are connected to the internet")

        return finder.getLinks()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue  # don't add if it is already in the queue
            if url in Spider.crawled:
                continue  # don't add if is already crawled
            if Spider.domain_name not in url:
                continue  # don't add if links belongs to external website
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue_file, Spider.queue)
        set_to_file(Spider.crawled_file, Spider.crawled)



