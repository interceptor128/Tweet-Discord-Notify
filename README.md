# TWEET-DISCORD-NOTIFY

Search for tweets with a specific hashtag and post the post date and time + Twitter link to a specific Discord server channel.

## How to use?

1. Create Heroku account

2. Fork this repository

3. Create Heroku App

4. Connect to GitHub, select forked repository

5. Setting Config Vars

6. Add Heroku Postgres, create Postgres database and create table 'twitter'

7. Deploy using Heroku Git

8. Create Developer twiiter account and  create twitter app

9. Get api key, api secret key, access token and access token secret

10. Create Discord server, category and channel

11. Get webhook url of credated channel

## Config Vars

1. API_KEY ... set api key of twitter

2. API_SECRET ... set api secret key of twitter

3. ACCESS_TOKEN ... set access token of twitter

4. ACCESS_TOKEN_SECRET ... set access secret token of twitter

5. SEARCH_WORD ... set search word

6. COUNT_NUMBER ... set tweet number of acquisitions

7. WEBHOOK_URL ... set webhook url

8. DB_URI ... set URI of database credentials

## DDL

```sql
create table twitter (
  screen_name varchar(15) not null
  , tweet_id varchar(19) not null
  , primary key (screen_name, tweet_id)
);
```
