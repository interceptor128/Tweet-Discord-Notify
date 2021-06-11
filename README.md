# TWEET-DISCORD-NOTIFY

Search for tweets with a specific hashtag and post the post date and time + Twitter link to a specific Discord server channel.

## How to use?

### Preparation

1. Create Heroku account

2. Create Developer twiiter account and twitter app

3. Get api key, api secret key, access token and access token secret

4. Create Discord server, category and channel

5. Get webhook url of created channel

6. Login heroku cli (command prompt or bash)

### Main task

1. Fork this repository and clone your repository

2. Create the .env file by referring to the section .env file

3. Execute "generate_heroku_commands.py bat shift_jis"

4. Execute create_heroku_app.bat

5. Create table 'twitter' in created application by referring to the section DDL  
  (After execute heroku cli of Database Credentials)

6. Select your repository and connect to GitHub

7. Deploy

8. Execute set_heroku_ps.bat

9. Create job of scheduler

## Config Vars

You can use generate_heroku_command.py and .env to generate commands to set environment variables.  
The extension (bat or sh) is required as an argument to run this script.  
If your OS is Windows, use bat. If your OS is Linux-based, use sh.  
If you are using a Linux system, be careful about execution permissions.  

1. APP_NAME ... set application name (It is not required for the heroku app itself, but it is needed to generate the heroku commands.)

2. API_KEY ... set api key of twitter

3. API_SECRET ... set api secret key of twitter

4. ACCESS_TOKEN ... set access token of twitter

5. ACCESS_TOKEN_SECRET ... set access secret token of twitter

6. SEARCH_WORD ... set search word

7. COUNT_NUMBER ... set tweet number of acquisitions

8. WEBHOOK_URL ... set webhook url

9. DATABASE_URL ... set automatly when add Heroku Postgres

### .env file

APP_NAME is max 30 byte.

```.env
APP_NAME=collection-vtuber-isekaijoucho
API_KEY=XXXXXXXXXXXXXXXXXXXXXX
API_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
SEARCH_WORD="#ヰ世界情緒美術部 filter:images exclude:retweets -from:@isekaijoucho"
COUNT_NUMBER=30
WEBHOOK_URL=https://discord.com/api/webhooks/999999999999999999/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## DDL

```sql
create table twitter (
  screen_name varchar(15) not null
  , tweet_id varchar(19) not null
  , primary key (screen_name, tweet_id)
);
```
