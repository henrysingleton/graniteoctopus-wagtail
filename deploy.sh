#!/bin/bash -e
echo "Copying up files"
rsync -az --force --delete --progress --exclude-from=deploy-exclude.txt ./blog ./microblog ./graniteoctopus ./home ./manage.py ./requirements.txt ./search ./static graniteoctopus:/opt/webapps/goctopus/site

