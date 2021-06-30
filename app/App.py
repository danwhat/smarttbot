import datetime, time, decimal

from Helper import APIreturnTicker
from Connection import CandleDao

if __name__ == '__main__':
  
  CandleDaoWorking = CandleDao()

  NextCandle1 = datetime.datetime.now() + datetime.timedelta(seconds=10)
  NextCandle5 = datetime.datetime.now() + datetime.timedelta(minutes=5)
  NextCandle10 = datetime.datetime.now() + datetime.timedelta(minutes=10)

  #Atributos
  openValue = None
  lowValue = None
  highValue = None

  count = 0
  while True:
    print(f"loop {count}")
    count += 1
    time.sleep(1)
    data = APIreturnTicker()

    # Atualizar atributos
    if openValue == None:
      openValue = decimal.Decimal(data['last'])
      lowValue = decimal.Decimal(data['lowestAsk'])
      highValue = decimal.Decimal(data['highestBid'])
    else:
      if lowValue > decimal.Decimal(data['lowestAsk']):
        lowValue = decimal.Decimal(data['lowestAsk'])
      if highValue < decimal.Decimal(data['highestBid']):
        highValue = decimal.Decimal(data['highestBid'])

    # Criar candles
    now = datetime.datetime.now()

    if NextCandle1 <= now :
      print("Hora do Candle de 1min")
      NextCandle1 += datetime.timedelta(minutes=1)
      CandleDaoWorking.addCandle(
        currencyId = 1,
        frequency = 1,
        openValue = openValue,
        closeValue = decimal.Decimal(data['last']),
        lowValue = openValue,
        highValue = highValue
      )
      # candles1minArray.append(vela)

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

