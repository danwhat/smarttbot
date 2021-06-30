import requests

def APIreturnTicker():
    url = "https://poloniex.com/public?command=returnTicker"
    response = requests.get(url)
    responsejson = response.json()['BTC_BTS']
    return responsejson