#!/bin/bash -e

echo "Copying up files..."
rsync -az --force --delete --progress --exclude-from=deploy-exclude.txt \
./blog \
./microblog \
./personal \
./graniteoctopus \
./home \
./manage.py \
./requirements.txt \
./search \
./static \
graniteoctopus:/opt/webapps/goctopus/site

echo "Updating packages..."
ssh graniteoctopus /opt/webapps/goctopus/env/bin/pip install -r /opt/webapps/goctopus/site/requirements.txt

echo "Running migrations..."
ssh graniteoctopus /opt/webapps/goctopus/env/bin/python /opt/webapps/goctopus/site/manage.py migrate

echo "Restart app server..."
ssh -t graniteoctopus sudo supervisorctl restart goctopus