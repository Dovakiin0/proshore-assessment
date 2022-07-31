# Scraper Service

This service is only responsible for scraping the blogs from the [Proshore website](https://proshore.eu/resources/) and storing it in the database. The technology used in this services are:

- Python with Selenium
- Flask
- Numpy

This service first scrapes the blogs from the website and stores it in a list. Then it converts the list into a numpy array and duplicates to 1000 times and sends request to backend service to store the data in the database.
However, it does provide a single endpoint using flask to let the user scrape the site from the frontend.

By default, the app is running on port `5000`.
The entrypoint is `app.py`

### Endpoint

| endpoint       | method | description             |
| -------------- | ------ | ----------------------- |
| /api/v1/scrape | POST   | Starts Scraping process |
