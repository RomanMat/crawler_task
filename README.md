## Python Developer – Web Crawling Position Task


### About 

It's not the ultimate solution that definitely needs editing but I really invested in it. In fact, it turned out pretty cool.
Hope you will get into it with my readme.


### Data collection

The part of data scraping in this task is based on `Scrapy`, that is awesome tool, that let you to interact with js.
This time we do not need to use any selectors or smth, cause we will make API requests. But how it exactly works?

1. The written spider `TenderSpider` uses pre-prepared headers and a JSON query body, that will contain information about
what information we need as we make a `POST` requests.

2. Spider make request to `http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/` endpoint. This API edpoint allows only `POST` method requests, so we will use our headers and JSON query to get a access.

3. After spider gets response it parse data into `Scrapy Items` (converted Djnago-model), that will be yielded into pipelines.

4. `TenderPipeline` - it's like data flow. First thing first, our pipeline validate data with 
JSON schema and then makes some fields transformation.

5. Saving data to database. 


### API 

This part is made on `Django REST framework`. This is part, where we will use 
scraped data.

1. List of endpoints that was described in urls:

**custom endpoints**
* `api/v1/tenders/list/` - returns full list of tenders. (requires authentication) 
* `api/v1/tenders/<id>/` - returns specific item list of tenders. (requires authentication) 
* `api/v1/tenders/search/<year-month-day>` - returns list of records for specified date. (requires authentication)
    
**frameworks endpoints**
* `api-token-auth/` - returns token for mentioned username
* `admin/` - gives admin panel access

2. After requests to this endpoint, Django will call *appropriate Django-view*.
At this step it will also serialize data from database and return those thing, that you need.

3. All custom endopints requires token authentication, so first thing first you need to create superuser.

## How to use?

1. Install python [here](https://www.python.org/downloads/) (python 3.8 recommended)

2. Install requirements.txt file with `pip install -r requirements.txt`

3. Move to `scraper` dir and run scraper with `scrapy crawl tender`

4. Drink some tea while scrapy works. Check results by looking at database.

5. Go to file where `manage.py` file located.

6. Run command `python3 manage.py createsuperuser`. Create your user.

7. Run command `python3 manage.py drf_create_token <your username>`. Save your token.

8. Run server by using this command: `python3 manage.py runserver`

9. Make some test requests with your token in headers.

Example with `curl` command: </br>`curl http://127.0.0.1:8000/api/v1/tenders/list -H 'Authorization: Token <your token>'`.


## TIPS AND TESTING

* Forgot your token? </br> 
Use `http post http://127.0.0.1:8000/api-token-auth/ username=<username> password=<password>` command.

* `curl http://127.0.0.1:8000/api/v1/tenders/list -H 'Authorization: Token <your token>'`
returns full list of tenders.

* `curl http://127.0.0.1:8000/api/v1/tenders/<id> -H 'Authorization: Token <your token>'`
returns one tender, which primary key in database will be associated with mentioned id.

* `curl http://127.0.0.1:8000/api/v1/tenders/search/<year-month-date> -H 'Authorization: Token <your token>'`
returns all tenders, which date field in database will be associated with mentioned date.

* `curl http://127.0.0.1:8000/admin -H 'Authorization: Token <your token>'`
will provide access to admin panel.

Waiting for your response and have a nice day!
