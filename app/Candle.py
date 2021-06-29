import datetime

class Candle:
  
  currencyId = None
  frequency = None
  regDate = None
  openValue = None
  lowValue = None
  highValue = None
  closeValue = None

  def __init__(self, currencyId, frequency, openValue, lowValue, highValue, closeValue):
    self.currencyId = currencyId
    self.frequency = frequency
    self.openValue = openValue
    self.lowValue = lowValue
    self.highValue = highValue
    self.closeValue = closeValue
    self.regDate = datetime.datetime.now()

if __name__ == "__main__":
  print("teste")
  vela = Candle(1,1,1,1,1,1)
  print(vela.regDate)