#!/usr/bin/env python3
import requests
import json
import time
import datetime
import platform
import os
import argparse
# ----------------------------------------------------------------------------------------
Api = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
# ApiUsdt = 'https://api.binance.com/api/v3/ticker/price?symbol=USDTBVND'
# ----------------------------------------------------------------------------------------
BuyPrice = 69500
TargetPercent = 1
# ----------------------------------------------------------------------------------------

def parser():
    parser = argparse.ArgumentParser(description="Get bitcoin price")
    parser.add_argument("--time", type=int, default="60", help="Give me time to re-get new price. Ex: --time 60")
    return parser.parse_args()

# ----------------------------------------------------------------------------------------
def GetPriceFromApi(symbol):
    Api = 'https://api.binance.com/api/v3/ticker/price?symbol='
    output = requests.get(Api+symbol)
    data = output.json()
    Price = float(data['price'])
    return Price
# ----------------------------------------------------------------------------------------
def main():
    if(platform.system() == 'Linux'):
        os.system('clear')
    if(platform.system() == 'Windows'):
        os.system('cls')



    i = 0
    args = parser()

    print("This script gets new BTC-USDT price in every {} seconds".format(args.time))
    print("\n" * 2)

    while True:
        try:
            Price = GetPriceFromApi('BTCUSDT')
            # PriceUsdt = GetPriceFromApi('USDTBVND')
            PriceUsdt = 0
            CurrentTime = str(datetime.datetime.now())

            Percent = (Price - BuyPrice) / BuyPrice
            Percent = Percent * 100

            if(i%10 == 0):
                print("\nBTC: {:0<.2f}, USDT: {:0<.2f} price -- Time: {}".format(Price, PriceUsdt, CurrentTime[:-7] ))
            else:
                print("BTC: {:0<.2f}, USDT: {:0<.2f}  \t\t\t Profit: {:0<.2f}%".format(Price, PriceUsdt, Percent))
            
            CheckPriceJump(Percent)
            

        except:
            print("An exception occurred")

        
        

        i += 1
        time.sleep(args.time)


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
def CheckPriceJump(Percent):
    
    if(Percent>TargetPercent):
        print("Chien debug play sound now")
        for x in range(5):
            os.system('spd-say "Bitcoin is going new higher price!"')
            time.sleep(3)
        


# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

