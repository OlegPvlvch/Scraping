<h1>How to run project</h1>

Open 3 terminals and type <br>
1 : python manage.py runserver <br>
2 : scrapy crawl valentino <br>
3 : celery -A scraping_project.celery_app.app worker --loglevel=INFO
