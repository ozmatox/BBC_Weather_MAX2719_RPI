#!/usr/bin/env python
#>>>>ozmatox<<<<

import time
import feedparser
from random import randrange
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

#create device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

#get data
python_wiki_rss_url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/3088171"


while True:
        show_message(device, msg="Aktualna Pogoda dla Miasta Poznan BBC Weather - Forecast", fill="white", font=proportional(SINCLAIR_FONT))
        print("Pobieram Dane")
        feed = feedparser.parse( python_wiki_rss_url)

        for repeats in range(10):
                print(repeats)
                for items in feed["items"]:

                        msg = items["title"]
                        msg = msg[0:msg.find(",")]
                        print(msg)
                        show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
                        time.sleep(1)

                        #msg = items["link "]
                        #msg = msg[0:msg.find(",")]
                        #print(msg)
                        #show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
                        #time.sleep(1)

                        msg = items["description"]
                        msg = msg[0:msg.find(",,")]
                        print(msg)
                        show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
                        time.sleep(1)

                        msg = time.asctime()
                        msg= time.strftime("%H:%M")
                        print(msg)
                        show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
                        time.sleep(10)
