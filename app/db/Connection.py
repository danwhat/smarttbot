import mysql.connector

class MySqlConnection:
  
  __con = None
  __cursor = None

  def __init__(self):
    self.__con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smarttbot"
      )

  def query(self, query):
    if self.__cursor == None:
      self.__cursor = self.__con.cursor()
    self.__cursor.execute(query)
    if query.find('insert into') != -1:
      self.__con.commit()
    return self.__cursor.fetchall()

  def close(self):
    self.__con.close()



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

# testes:
# if __name__ == "__main__":
#   banco = MySqlConnection()
#   reult = banco.query("select * from currencies;")
#   for x in reult:
#     print(x)

# if __name__ == "__main__":

#   testeDao = CandleDao()
#   testeDao.addCandle(2,5,10,10,15,50)
#   lupito = testeDao.getAll()
#   for x in lupito:
#     print(x[3])
  # banco = MySqlConnection()
  # reult = banco.query("select * from currencies;")
  # for x in reult:
  #   print(x)