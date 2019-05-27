from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

HOMEPAGE = ''
PROJECT_NAME = ''


@app.route("/")
def index():
    return render_template('index.html')


DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()


# create threads (will die when main exits)


def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# do the next job on the queue


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# each link in the queue is a new job

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# check if there links in queue , if so crwal them


def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + ' Links in the queue')
        create_jobs()


@app.route("/crawl", methods=['POST', 'GET'])
def validate():
    if request.method == 'POST':
        global PROJECT_NAME
        PROJECT_NAME = request.form['project_name']
        global HOMEPAGE
        HOMEPAGE = request.form['domain_name']
        global QUEUE_FILE
        global CRAWLED_FILE
        QUEUE_FILE = PROJECT_NAME + '/queue.txt'
        CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

        Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
        create_spiders()
        crawl()

        return send_from_directory(directory=PROJECT_NAME, filename='crawled.txt', as_attachment=True)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
