# RPI-Zero Twitter's Top Trends

This is a Python script that uses the Raspberry Pi Hat for Waveshare 2.13 inch e-Paper display to show the latest trending topics on Twitter for different countries. It also posts updates to Twitter using the Tweepy library.

### Here's a brief overview of the code:

    Importing required libraries and modules
    The code imports the following modules:
        sys
        os
        PIL (Python Imaging Library)
        datetime
        tweepy
        traceback
        waveshare_epd
        logging
        time

    Setting up Twitter API Keys and Tokens
    The code defines the following variables to store Twitter API keys and tokens:
        consumer_key
        consumer_secret
        access_token
        access_token_secret

    Authorization and Authentication
    The code uses the tweepy library to authenticate and authorize access to the Twitter API using the above-mentioned API keys and tokens.

    Initializing the e-Paper Display
    The code initializes the Waveshare 2.13 inch e-Paper display and clears any existing content from the display.

    Drawing on the image
    The code creates an empty image of size (epd.height, epd.width) and draws text on it using the PIL ImageDraw module. It then displays the image on the e-Paper display.

    Getting Trends for Different Countries
    The code uses the Twitter API to get the latest trends for different countries. It first gets the closest location to a specific set of coordinates (latitude and longitude) for a country using the api.closest_trends() function. It then uses the woeid (Where On Earth ID) for that location to get the latest trends using the api.get_place_trends() function.

    Updating the Display
    The code updates the display with the latest trends for a specific country. It first clears the existing content from the display and then draws the date, time and country name at the top of the display. It then draws the latest trends, one below the other, in a list format.

    Posting Updates to Twitter
    The code posts updates to Twitter using the Tweepy API. It formats the latest trends as a string and posts it to the user's Twitter account.

    Handling Exceptions
    The code uses try-catch blocks to handle any exceptions that may occur during execution. If an IOError or KeyboardInterrupt occurs, the code exits gracefully.
