#!/usr/bin/env python3
import requests
import json
import time
import datetime
import platform
import os
import argparse
# ----------------------------------------------------------------------------------------

def parser():
    parser = argparse.ArgumentParser(description="Get bitcoin price")
    parser.add_argument("--time", type=int, default="30", help="Give me time to re-get new price. Ex: 10")
    return parser.parse_args()

# ----------------------------------------------------------------------------------------
if(platform.system() == 'Linux'):
    os.system('clear')
if(platform.system() == 'Windows'):
    os.system('cls')

Api = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

i = 0
args = parser()

print("This script gets new BTC-USDT price in every {} seconds".format(args.time))
print("\n" * 2)

while True:
    try:
        url = requests.get(Api)
        data = url.json()
        Price = float(data['price'])
        CurrentTime = str(datetime.datetime.now())

        if(i%10 == 0):
            print("{:0<.2f} <== BTC price -- Time: {}".format(Price, CurrentTime[:-7] ))
        else:
            print(Price)
    except:
        print("An exception occurred")

    
    

    i += 1
    time.sleep(args.time)