from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time


def init_driver(PATH):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=options)
    driver.get("https://proshore.eu/resources/")
    return driver


def scroll_down(driver):
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height



def scrape_data(driver):
    all_blogs = driver.find_elements(By.CLASS_NAME, "playground-item-col")
    blogs_list = []
    for item in all_blogs:
        try:
            title = item.find_element(By.CLASS_NAME,"playground-title").text
            description = item.find_element(By.CLASS_NAME,"playground-excerpt").text
            author_name = item.find_element(By.CLASS_NAME,"playground-author-name").text
            author_description = item.find_element(By.CLASS_NAME,"playground-author-description").text
            image_url = item.find_element(By.CLASS_NAME,"playground-image").find_element(By.TAG_NAME, "img").get_attribute("src")
            try:
                read_time = item.find_element(By.CLASS_NAME,"playground-read-time-text").text
            except NoSuchElementException:
                read_time = "N/A"
            scrapedBlog = {
                "title": title,
                "description": description,
                "author_name" : author_name,
                "author_description": author_description,
                "image_url": image_url,
                "reading_time": read_time
            }
            if title != "":
                blogs_list.append(scrapedBlog)
        except Exception as e:
            print(e)
    return blogs_list
