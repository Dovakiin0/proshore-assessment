from gettext import find
from flask import Flask
from flask_cors import CORS
import requests
from BlogScraper.Scraper import scrape_data, scroll_down, init_driver
import numpy as np
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv, find_dotenv
import os

app = Flask(__name__)
CORS(app)

PATH = os.path.dirname(os.path.abspath(__file__)) + "/driver/chromedriver"

@app.route("/api/v1/scrape", methods=["POST"])
def scrape():
    try:
        load_dotenv(find_dotenv())

        driver = init_driver(PATH)
        scroll_down(driver)
        blog_lists = scrape_data(driver)
        npArray = np.repeat(blog_lists, 1000)
        np.random.shuffle(npArray)
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        r = session.post(os.getenv("URI")+"/api/v1/blogs/bulk", json=npArray.tolist())
        driver.quit()
        return r.json(), 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)