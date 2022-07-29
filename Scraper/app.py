from flask import Flask
from flask_cors import CORS
import requests
from BlogScraper.Scraper import scrape_data, scroll_down, init_driver
import numpy as np
import os

app = Flask(__name__)
CORS(app)

PATH = os.path.dirname(os.path.abspath(__file__)) + "/driver/chromedriver"

@app.route("/api/v1/scrape", methods=["POST"])
def scrape():
    try:
        driver = init_driver(PATH)
        scroll_down(driver)
        blog_lists = scrape_data(driver)
        npArray = np.repeat(blog_lists, 1000)
        np.random.shuffle(npArray)
        response = requests.post("http://localhost:5050/api/v1/blogs/bulk", json=npArray.tolist())
        driver.quit()
        return response.json(), 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)