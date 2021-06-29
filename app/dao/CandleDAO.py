import sys
sys.path.append('../db')

from MySqlConnection import MySqlConnection

class CandleDao:
  
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

if __name__ == "__main__":

  testeDao = CandleDao()
  testeDao.addCandle(2,5,10,10,15,50)
  lupito = testeDao.getAll()
  for x in lupito:
    print(x[3])
  # banco = MySqlConnection()
  # reult = banco.query("select * from currencies;")
  # for x in reult:
  #   print(x)