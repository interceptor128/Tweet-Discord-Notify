import sys
import os
from dotenv import load_dotenv

# Generate setting command file from environment variable of .env file

# read .env file
load_dotenv()

heroku_command = 'heroku config:set '

# set application name
app_name = ' -a ' + os.environ['APP_NAME'] + '\n'

# set Config Vars
line1 = heroku_command + 'API_KEY=' + os.environ['API_KEY'] + app_name
line2 = heroku_command + 'API_SECRET=' + os.environ['API_SECRET'] + app_name
line3 = heroku_command + 'ACCESS_TOKEN=' + \
    os.environ['ACCESS_TOKEN'] + app_name
line4 = heroku_command + 'ACCESS_TOKEN_SECRET=' + \
    os.environ['ACCESS_TOKEN_SECRET'] + app_name
line5 = heroku_command + 'SEARCH_WORD="' + \
    os.environ['SEARCH_WORD'] + '"' + app_name
line6 = heroku_command + 'COUNT_NUMBER=' + \
    os.environ['COUNT_NUMBER'] + app_name
line7 = heroku_command + 'WEBHOOK_URL=' + os.environ['WEBHOOK_URL'] + app_name

# create command text
output_text = line1 + line2 + line3 + line4 + line5 + line6 + line7

# output file
path = 'set_config_vars.' + sys.argv[1]
f = open(path, 'w', encoding='utf-8')
f.write(output_text)
f.close
