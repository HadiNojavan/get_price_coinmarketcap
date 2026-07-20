import requests
import json

def get_multiple_coins(symbols):
    try:
        key = "YOUR_API_KEY_HERE"
        url = "https://pro-api.coinmarketcap.com/v3/cryptocurrency/quotes/latest"
        
        # we cant say "symbol":["btc","Eth"] 
        #we must sent it like a string but separete it
        params = {"symbol": ",".join(symbols), "convert": "USDT"}
        headers = {
            "X-CMC_PRO_API_KEY": key,
            "Accepts": "application/json"
        }

        response = requests.get(url, headers=headers, params=params)
        full_list = response.json()['data'] 

        final_results = []

        for coin in full_list:
            
            if coin['symbol'] in symbols:
                clean_output = {
                    "name": coin['name'],
                    "symbol": coin['symbol'],
                    "rank": coin['cmc_rank'],
                    "price": coin['quote'][0]['price'],
                    "market_cap": coin['quote'][0]['market_cap']
                }

                final_results.append(clean_output)

                if len(final_results)==len(symbols):
                    return final_results

    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    # Get your favorite tokens' prices
    my_favorite_coins = ["BTC", "ETH", "TRX", "KDA"]
    res=get_multiple_coins(my_favorite_coins)
    print(json.dumps(res, indent=4))
