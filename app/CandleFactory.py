import time
import decimal
import datetime
import schedule

from dao.CandleDAO import CandleDAO
from Helper import APIreturnTicker
from CustomCandleFactory import custom_candle_factory


class CandleFactory():

    def __init__(self, currency_Id, currency_code):
        self.currency_Id = currency_Id
        self.currency_code = currency_code
        self.openValue = None
        self.closeValue = None
        self.lowValue = None
        self.highValue = None
        self.dao = CandleDAO()

    def atualizar_valores(self):
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

    def one_minute_candle_factory(self):

        print("Criando candle de 1min")
        self.dao.add_candle(
            currencyId=self.currency_Id,
            frequency=1,
            openValue=self.openValue,
            closeValue=self.closeValue,
            lowValue=self.openValue,
            highValue=self.highValue
        )

        self.openValue = None
        self.lowValue = None
        self.highValue = None

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
