import requests

def APIreturnTicker(coin_code = "USDT_BTC"):
    url = "https://poloniex.com/public?command=returnTicker"
    response = requests.get(url)
    responsejson = response.json()[coin_code]
    return responsejson

# USDT_BTC Bitcoin
# USDT_XMR Monero