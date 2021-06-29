import datetime, time, requests, numpy, decimal
from Candle import Candle

if __name__ == '__main__':
  
  min1 = datetime.timedelta(minutes=1)
  min5 = datetime.timedelta(minutes=5)
  min10 = datetime.timedelta(minutes=10)

  NextCandle1 = datetime.datetime.now() + min1
  NextCandle5 = datetime.datetime.now() + min5
  NextCandle10 = datetime.datetime.now() + min10

  #Arrays de Candles
  candles1minArray = []
  candles5minArray = []

  #Atributos
  openValue = None
  lowValue = None
  highValue = None

  # Primeiro Request
  url = "https://poloniex.com/public?command=returnTicker"
  response = requests.get(url)
  responsejson = response.json()['BTC_BTS']

  count = 0
  while True:
    time.sleep(1)
    print(f"loop numero {count}")
    count += 1 

    # Requests
    response = requests.get(url)
    responsejson = response.json()['BTC_BTS']

    # Atualizar atributos
    if openValue == None:
      openValue = decimal.Decimal(responsejson['last'])
      lowValue = decimal.Decimal(responsejson['lowestAsk'])
      highValue = decimal.Decimal(responsejson['highestBid'])
    else:
      if lowValue > decimal.Decimal(responsejson['lowestAsk']):
        lowValue = decimal.Decimal(responsejson['lowestAsk'])
      if highValue < decimal.Decimal(responsejson['highestBid']):
        highValue = decimal.Decimal(responsejson['highestBid'])


    # Criar candles
    now = datetime.datetime.now()

    if NextCandle1 <= now :
    # Adiciona ao banco de dados
    # Adiciona no array de candles
    # Reseta Atributos
      print("Hora do Candle de 1min")
      NextCandle1 += min1
      vela = Candle(
          currencyId = 1,
          frequency = 1,
          openValue = openValue,
          lowValue = openValue,
          highValue = highValue,
          closeValue = decimal.Decimal(responsejson['last']),
      )

      candles1minArray.append(vela)

      print(vela.regDate)
      print(vela.openValue)
      print(vela.closeValue)
      print(vela.lowValue)
      print(vela.highValue)

      openValue = None
      lowValue = []
      highValue = []









    # if NextCandle5 <= now :
    #   print("Hora do Candle de 5min")
    #   NextCandle5 += min5
    # if NextCandle10 <= now :
    #   print("Hora do Candle de 10min")
    #   NextCandle10 += min10




# Ideia inicial:

# Candles1minArray []

# NextCandle1
# NextCandle5
# NextCandle10

# currency_id
# open_value [1x]
# low_value [60x]
# high_value [60x]
# close_value [1x]

# Whilezão:
  # A cada segundo: 
    # Fazer Requests
    # Append Valores Array

  # if TimeCandle1:
    # TimeCandle1 += 1min
    # Pega o max de cada atributo e cria o OBJ Candle
    # Adiciona ao banco de dados
    # Adiciona no array de candles
    # Reseta Atributos

  # if TimeCandle5:
    # TimeCandle5 += 5min
    # Cria o OBJ Candle5 com o array de Candles1
    # Adiciona ao banco de dados
    # Adiciona no array de candles5
  
  # if TimeCandle10:
    # TimeCandle10 += 10min
    # Cria o OBJ Candle10 com o array de Candles1 + array de Candles5
    # Adiciona ao banco de dados

