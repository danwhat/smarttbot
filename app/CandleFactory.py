import time, decimal, datetime, schedule
from dao.CandleDAO import CandleDAO
from Helper import APIreturnTicker
from CustomCandleFactory import CustomCandleFactory

class CandleFactory():
    
  def __init__(self, currency_Id, currency_code):
    self.currency_Id = currency_Id
    self.currency_code = currency_code
    self.openValue = None
    self.closeValue = None
    self.lowValue = None
    self.highValue = None
    self.dao = CandleDAO()

  def atualizarValores(self):
    data = APIreturnTicker(self.currency_code)

    # Atualizar atributos
    if self.openValue == None:
      self.openValue = decimal.Decimal(data['last'])
      self.lowValue = decimal.Decimal(data['lowestAsk'])
      self.highValue = decimal.Decimal(data['highestBid'])
    else:
      self.closeValue = decimal.Decimal(data['last'])
      if self.lowValue > decimal.Decimal(data['lowestAsk']):
        self.lowValue = decimal.Decimal(data['lowestAsk'])
      if self.highValue < decimal.Decimal(data['highestBid']):
        self.highValue = decimal.Decimal(data['highestBid'])

  def OneMinCandleFactory(self):

    print("Criando candle de 1min")
    self.dao.addCandle(
      currencyId = self.currency_Id,
      frequency = 1,
      openValue = self.openValue,
      closeValue = self.closeValue,
      lowValue = self.openValue,
      highValue = self.highValue
    )

    self.openValue = None
    self.lowValue = None
    self.highValue = None 
  def FiveMinCandleFactory(self):
    CustomCandleFactory(self.currency_Id,5)
  def TenMinCandleFactory(self):
    CustomCandleFactory(self.currency_Id,10)

  def run(self):
    schedule.every(1).seconds.do(self.atualizarValores)
    schedule.every(6).seconds.do(self.OneMinCandleFactory)
    schedule.every(30).seconds.do(self.FiveMinCandleFactory)
    schedule.every(60).seconds.do(self.TenMinCandleFactory)

    while True:
      schedule.run_pending()
      time.sleep(1)