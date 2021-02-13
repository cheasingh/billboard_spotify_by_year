# Weekly Billboard 100 to Spotify playlist

Search for billboard top 100 by year and create spotify playlist, data is taking from https://www.billboard.com/charts/hot-100 using beautifulsoup.

to use:
1. clone this directory
2. install dependency `install -r requirements.txt`
3. register and generate app_id and app_secret from spotify https://developer.spotify.com/dashboard/applications/
4. create .env file in root directory, with key value of
    `SPOT_ID=[your_id]`
    `SPOT_SEC=[your_sec]`
5. run the application by `py main.py`
