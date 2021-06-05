# TWEET-DISCORD-NOTIFY

Search for tweets with a specific hashtag and post the post date and time + Twitter link to a specific Discord server channel.

## How to use?

### Preparation

1. Create Heroku account

2. Create Developer twiiter account and  create twitter app

3. Get api key, api secret key, access token and access token secret

4. Create Discord server, category and channel

5. Get webhook url of credated channel

### Main task

1. Fork this repository

2. Create Heroku App

3. Connect to GitHub, select forked repository

4. Setting Config Vars

5. Add Heroku Postgres, create Postgres database and create table 'twitter'

6. Deploy using Heroku Git

## Config Vars

1. API_KEY ... set api key of twitter

2. API_SECRET ... set api secret key of twitter

3. ACCESS_TOKEN ... set access token of twitter

4. ACCESS_TOKEN_SECRET ... set access secret token of twitter

5. SEARCH_WORD ... set search word

6. COUNT_NUMBER ... set tweet number of acquisitions

7. WEBHOOK_URL ... set webhook url

8. DATABASE_URL ... set automatly when add Heroku Postgres

## DDL

```sql
create table twitter (
  screen_name varchar(15) not null
  , tweet_id varchar(19) not null
  , primary key (screen_name, tweet_id)
);
```
