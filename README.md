# pipeline_back
Data pipeline

Project considerations:  

Add to the project folder level:  

docker-compose.dev.yaml, this file contains a angular service which can be removed.  

Docker's commands to use are:  

docker compose -f docker-compose.dev.yaml build  

docker compose -f docker-compose.dev.yaml up

First configure the database credentials in the .env file  

When starting the project for the first time it is necessary to do first:  

python manage.py migrate  

python manage.py upload_data_access_points_cdmx