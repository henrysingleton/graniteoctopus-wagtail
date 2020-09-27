Granite Octopus Site
====================

This project is a personal site for my blog. Currently running Wagtail 2.4.

Developing
----------

1. Clone this repo
2. `docker-compose up`
3. `docker-compose exec web python manage.py migrate`
4. `docker-compose exec web python manage.py createsuperuser`
5. `open http://localhost:8000/admin`

Hosting
-------
Currently hosted at Vultr on a VPS.
There is an S3 bucket created but this has not been configured in the
application yet.

Updating
--------

1. `pip-compile --upgrade`  
2. `pip-sync`  
3. `python manage.py migrate`  

Deploying
---------

Currently deployed to a VPS. To deploy:

`./deploy.sh`  

Site is installed in `/opt/webapps/goctopus`

If you add a new app you will need to explicitly add its directory to the
`deploy.sh` file.