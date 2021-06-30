from db.Connection import MySqlConnection

class CandleDAO:
  
  __db = None

  def __init__(self):
    self.__db = MySqlConnection()
  
  def addCandle(self, currencyId, frequency, openValue, closeValue, lowValue, highValue):
    query = f"insert into candles(currency_id, frequency, open_value, close_value, low_value, high_value) values ({currencyId},{frequency},{openValue},{closeValue},{lowValue},{highValue});"
    self.__db.query(query)

  def getAll(self):
    query = "select * from candles"
    result = self.__db.query(query)
    return result