import sys
import os
from dotenv import load_dotenv

# Generate setting command file from environment variable of .env file

# read .env file
load_dotenv()

# constants
heroku = 'heroku '
create_app = 'apps:create '
create_addon = 'addons:create '
set_config = 'config:set '
space = ' '
hypA = '-a '
EOF = '\n'
amp = ' && '

# set application name
app_name = os.environ['APP_NAME']
paraApp = space + hypA + app_name

# check sys.argv
if len(sys.argv) <= 2:
    print('Error: Please enter both the extension and the character encoding.')
    sys.exit()

# check if it exceeds 30 bytes
if len(app_name) > 30:
    print('Error: APP_NAME is more than 30 bytes.')
    sys.exit()

encode_type = ['utf-8', 'shift_jis', 'euc_jp']
for encode_out in encode_type:
    if sys.argv[2] == encode_out:
        result_encode = sys.argv[2]
        break
    else:
        result_encode = ''

# check encode
if not result_encode:
    print('Error: Please enter the correct character code. (For example, utf-8, shift_jis, euc_jp.)')
    sys.exit()

# add Application
command_apps_create = heroku + create_app + app_name

# set Config Vars
command_config_set = heroku + set_config + \
    'API_KEY=' + os.environ['API_KEY'] + space + \
    'API_SECRET=' + os.environ['API_SECRET'] + space + \
    'ACCESS_TOKEN=' + os.environ['ACCESS_TOKEN'] + space + \
    'ACCESS_TOKEN_SECRET=' + os.environ['ACCESS_TOKEN_SECRET'] + space + \
    'SEARCH_WORD="' + os.environ['SEARCH_WORD'] + '"' + space + \
    'COUNT_NUMBER=' + os.environ['COUNT_NUMBER'] + space + \
    'WEBHOOK_URL=' + os.environ['WEBHOOK_URL'] + paraApp

# set Add-on
command_addons_create_postgres = heroku + create_addon + \
    'heroku-postgresql' + paraApp
command_addons_create_scheduler = heroku + create_addon + \
    'scheduler:standard' + paraApp

# set command text of create app and setting config vars
command1 = command_apps_create + amp + \
    command_config_set + amp + \
    command_addons_create_postgres + amp + \
    command_addons_create_scheduler + EOF

# set command text of clock
command2 = heroku + 'ps:scale web=0 clock=1' + paraApp + EOF

# output file
path = 'create_heroku_app.' + sys.argv[1]
f = open(path, 'w', encoding=result_encode)
f.write(command1)
f.close

path = 'set_heroku_ps.' + sys.argv[1]
f = open(path, 'w', encoding=result_encode)
f.write(command2)
f.close
