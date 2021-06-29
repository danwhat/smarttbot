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


# testes:
if __name__ == "__main__":
  banco = MySqlConnection()
  reult = banco.query("select * from currencies;")
  for x in reult:
    print(x)