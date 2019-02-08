Granite Octopus Site
====================

This project is a personal site for my blog. Currently running Wagtail 2.4.

Developing
----------

1. Clone this repo
2. `docker-compose up`
3. `docker-compose exec web python manage.py migrate`

Deploying
---------

Currently deployed to a VPS. To deploy:

`./deploy.sh`

You'll need to do manual re-loading on the web server. Script doesnt do it atm.

`source /opt/webapps/goctopus/env/bin/activate`
`pip install -r /opt/webapps/goctopus/site/requirements.txt`
`python /opt/webapps/goctopus/site/manage.py migrate`
`sudo supervisorctl restart graniteoctopus`
