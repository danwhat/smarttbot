import time
import decimal
import datetime
import schedule

from dao.CandleDAO import CandleDAO
from Helper import APIreturnTicker
from CustomCandleFactory import custom_candle_factory


class CandleFactory():

    def __init__(self, currency_Id, currency_code):

        self.dao = CandleDAO()
        self.currency_Id = currency_Id
        self.currency_code = currency_code
        self.data_dic = {
          "openValue": None,
          "closeValue": None,
          "lowValue": None,
          "highValue": None,
        }

        # self.openValue = None
        # self.closeValue = None
        # self.lowValue = None
        # self.highValue = None


    def atualizar_valores(self):
        data = APIreturnTicker(self.currency_code)
        new_data_dic = dict(self.data_dic)
        # Atualizar atributos
        if new_data_dic["openValue"] == None:
            new_data_dic["openValue"] = decimal.Decimal(data['last'])
            new_data_dic["lowValue"] = decimal.Decimal(data['lowestAsk'])
            new_data_dic["highValue"] = decimal.Decimal(data['highestBid'])
        else:
            new_data_dic["closeValue"] = decimal.Decimal(data['last'])
            if new_data_dic["lowValue"] > decimal.Decimal(data['lowestAsk']):
                new_data_dic["lowValue"] = decimal.Decimal(data['lowestAsk'])
            if new_data_dic["highValue"] < decimal.Decimal(data['highestBid']):
                new_data_dic["highValue"] = decimal.Decimal(data['highestBid'])

        self.data_dic = new_data_dic
        

    def one_minute_candle_factory(self):

        print("Criando candle de 1min")
        self.dao.add_candle(
            currencyId=self.currency_Id,
            frequency=1,
            openValue=self.data_dic["openValue"],
            closeValue=self.data_dic["closeValue"],
            lowValue=self.data_dic["lowValue"],
            highValue=self.data_dic["highValue"]
        )

        self.data_dic = {
          "openValue": None,
          "closeValue": None,
          "lowValue": None,
          "highValue": None,
        }

    def five_minute_candle_factory(self):
        custom_candle_factory(self.currency_Id, 5)

    def ten_minute_candle_factory(self):
        custom_candle_factory(self.currency_Id, 10)

    def run(self):
        schedule.every(1).seconds.do(self.atualizar_valores)
        schedule.every(60).seconds.do(self.one_minute_candle_factory)
        schedule.every(300).seconds.do(self.five_minute_candle_factory)
        schedule.every(600).seconds.do(self.ten_minute_candle_factory)

        while True:
            schedule.run_pending()
            time.sleep(1)
