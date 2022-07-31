# Proshore-Assessment

App that scrapes the entire blogs from the [Proshore website](https://proshore.eu/resources/), stores them in a database and displays them in proper paginated table with search and sort features included.

### The technologies used for this project are as follows:

- [Backend Service](https://github.com/Dovakiin0/proshore-assessment/tree/master/Backend#readme) - Python with Flask
- [Scraper Service](https://github.com/Dovakiin0/proshore-assessment/tree/master/Client#readme) - Python with Selenium
- [Client Service](https://github.com/Dovakiin0/proshore-assessment/tree/master/Scraper#readme) - Sveltekit with vite

(Please refer to individual services for individual details)

### How this works:

This app is separated into multiple services. The Scraper service is responsible for scraping the data from the website and storing it in a database. The Backend service is responsible for providing api services to the frontend and the Client service is responsible for displaying the data in a table. Finally Nginx is used as reverse proxy to serve the app. All services works independently and are combined together in a container with docker to work as a single service.

**The app has been deployed here: http://103.195.4.17/**

### Local Development

Easiest way to run the app locally is to use the `docker-compose` utility.  
With this command,

```bash
docker-compose up --build -d
```

You can easily run the app locally. By default the port 3000 is used for the app.

However, to run without docker-compose, you must make sure to install the following requirements:

- Python
- Nodejs
- Google Chrome (for Selenium driver to work)

Then navigate into each of the services and rename .env.example to .env and put in your database details.  
Then use the following command to run the app locally.

```bash
#Backend Service
cd Backend/ && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py

#Scraper Service
cd Scraper/ && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py

#Client Service
cd Client/ && npm install && npm run dev
```

Please replace the command python and pip to python3 and pip3 if you are using linux environment.

### Testing

The tests covers the endpoints of the API. To run the test locally, run the following command from the root folder:

```bash
sh test.sh
```
