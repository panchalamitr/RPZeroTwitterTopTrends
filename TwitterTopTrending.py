#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import tweepy
import traceback
from waveshare_epd import epd2in13_V2
import logging
import time

# API Keys and Tokens
consumer_key = 'TWITTER_CONSUMBER_KEY'
consumer_secret = 'TWITTER_CONSUMER_SECRET'
access_token = 'TWITTER_ACCESS_TOKEN'
access_token_secret = 'TWITTER_ACCESS_TOKEN_SECRET'

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V2 Demo")

    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    # Drawing on the image
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)

    logging.info("1.Drawing on the image...")
    image = Image.new('1', (epd.height, epd.width),
                      255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(image))
    epd.init(epd.PART_UPDATE)
    num = 1
    closest_loc = api.closest_trends(22.3511148, 78.6677428)
    country = 0
    country_name = ""
    while(True):
        if country == 0:
            # Inida
            closest_loc = api.closest_trends(22.3511148, 78.6677428)
            country_name = "India"
        elif country == 1:
            # Singapore
            closest_loc = api.closest_trends(1.352083, 103.819839)
            country_name = "SG"
        else:
            # United States
            closest_loc = api.closest_trends(33.788570, -82.893470)
            country_name = "USA"
            country = 0
        country += 1
        trends = api.get_place_trends(closest_loc[0]['woeid'])
        draw.rectangle((0, 0, epd.height, epd.width), fill=255)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S") + " " + country_name
        draw.text((0, 0), dt_string, font=font20, fill=0)
        for trend in trends[0]['trends']:
            # print(trend['name'])
            #draw.rectangle((0, 0, epd.height, epd.width), fill = 255)
            draw.text((0, num*20), trend['name'], font=font20, fill=0)
            epd.displayPartial(epd.getbuffer(image))
            num = num + 1
            if(num > 6):
                break
        time.sleep(5*60)
        num = 1
except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
