import datetime, time, decimal

class OneMinCandles:
  
  CandleDaoInstance = None
  APIreturnTicker = None

  def __init__(self, CandleDao, APIreturnTicker):
    self.APIreturnTicker = APIreturnTicker
    self.CandleDaoInstance = CandleDao()

  NextCandle1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
  NextCandle5 = datetime.datetime.now() + datetime.timedelta(minutes=5)
  NextCandle10 = datetime.datetime.now() + datetime.timedelta(minutes=10)

  #Atributos
  openValue = None
  lowValue = None
  highValue = None

  count = 0  


  # while True:
  #   print(f"loop {count}")
  #   count += 1
  #   time.sleep(1)
  #   data = APIreturnTicker()

  #   # Atualizar atributos
  #   if openValue == None:
  #     openValue = decimal.Decimal(data['last'])
  #     lowValue = decimal.Decimal(data['lowestAsk'])
  #     highValue = decimal.Decimal(data['highestBid'])
  #   else:
  #     if lowValue > decimal.Decimal(data['lowestAsk']):
  #       lowValue = decimal.Decimal(data['lowestAsk'])
  #     if highValue < decimal.Decimal(data['highestBid']):
  #       highValue = decimal.Decimal(data['highestBid'])

  #   # Criar candles
  #   now = datetime.datetime.now()

  #   if NextCandle1 <= now :
  #     print("Hora do Candle de 1min")
  #     NextCandle1 += datetime.timedelta(minutes=1)
  #     CandleDaoInstance.addCandle(
  #       currencyId = 1,
  #       frequency = 1,
  #       openValue = openValue,
  #       closeValue = decimal.Decimal(data['last']),
  #       lowValue = openValue,
  #       highValue = highValue
  #     )
  #     # candles1minArray.append(vela)

  #     openValue = None
  #     lowValue = []
  #     highValue = []

if __name__ == "__main__":
  print("oi")