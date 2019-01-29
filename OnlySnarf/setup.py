#!/usr/bin/python
# 10/21/2018 - Skeetzo

run script: `python3 setup.py`

---------------------------------
script checks for existing
  * settings.yaml
  * config.json

#################################
import json
from yaml import load, dump

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.json')) as config_file:    
    config = json.load(config_file)
#################################

if missing either credentials
  * check for google app json
  * check for google folder id .txt for easy setup

if still missing credentials
  * check for missing or incomplete "config.json"
  * check for missing or incomplete "settings.yaml"

---------------------------------
setup "config.json"
- ask for missing or invalid values
 - ask for username
 - ask for password
 - ask for images_folder id
 - ask for galleries_folder id
 - ask for posted_folder id
 - ask for videos_folder id

- create json object
- save to file "config.json"

{
  "username":"",
  "password":"!",
  "images_folder":"",
  "galleries_folder":"",
  "posted_folder": "",
  "videos_folder":""
}
----------------------------------
setup "settings.yaml"
- ask for google client id
- ask for google client secret

- create yaml string with filled in info
- save to yaml file

client_config_backend: settings
client_config:
  client_id: 440923105277-c5qj86e1031tnfekbdaqk8jn4e6enkh0.apps.googleusercontent.com
  client_secret: MNU_-jKomn0NwfF_AEQ08PET

save_credentials: True
save_credentials_backend: file
save_credentials_file: credentials.json

get_refresh_token: True

oauth_scope:
  - https://www.googleapis.com/auth/drive