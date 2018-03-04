Granite Octopus Site
====================

This project is a personal site for my blog. Currently running Wagtail 2.0.

Developing
----------

1. Clone this repo
2. Install a virtual env with something like:

   > mkproject -p . -r ./requirements.txt --python=python3.6 ~/.virtualenvs/goctopus

3. `workon goctopus`
4. `python manage.py migrate`
5. `python manage.py runserver`
6. Do a happy dance

Deploying
---------

Currently deployed to a VPS. To deploy:

`./deploy.sh`

You'll need to do manual re-loading on the web server. Script doesnt do it atm.
