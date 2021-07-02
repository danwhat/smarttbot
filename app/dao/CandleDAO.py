from db.Connection import MySqlConnection

class CandleDAO:

    __db = None

    def __init__(self):
        self.__db = MySqlConnection()

    def add_candle(self, currencyId, frequency, openValue, closeValue, lowValue, highValue):
        query = f"insert into candles(currency_id, frequency, open_value, close_value, low_value, high_value) values ({currencyId},{frequency},{openValue},{closeValue},{lowValue},{highValue});"
        self.__db.query(query)

    def getAll(self):
        query = "select * from candles"
        result = self.__db.query(query)
        return result

    def get_1min_candles_by_currency_id_and_time(self, currency_id, time):
        query = f"select open_value, close_value, high_value, low_value from candles where frequency=1 and currency_id={currency_id} order by id desc limit {time};"
        result = self.__db.query(query)
        return result
