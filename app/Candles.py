import datetime, time, decimal
from Helper import APIreturnTicker
from db.Connection import CandleDao

class OneMinCandles:
  
  candlesArray = []
  __nextCandle = datetime.datetime.now() + datetime.timedelta(seconds=10)

  #Atributos
  openValue = None
  lowValue = None
  highValue = None

  count = 0  
  true = True
  while true:
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

    if __nextCandle <= now :
      print("Hora do Candle de 1min")
      __nextCandle += datetime.timedelta(seconds=10)
      candle = {
        'currencyId': 1,
        'frequency': 1,
        'openValue': openValue,
        'closeValue': decimal.Decimal(data['last']),
        'lowValue': openValue,
        'highValue': highValue
      }
      candlesArray.append(candle)

      openValue = None
      lowValue = []
      highValue = []

# class CustomCandle:
#   data = None
#   def __init__(self, OneMinCandlesInstance, period):
#     self.data = OneMinCandlesInstance.candlesArray




if __name__ == "__main__":
  candlesDe1minuto = OneMinCandles(CandleDao);
  print("oi")