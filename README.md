How to run project

Open 3 terminals and type
1 : python manage.py runserver
2 : scrapy crawl valentino
3 : celery -A scraping_project.celery_app.app worker --loglevel=INFO