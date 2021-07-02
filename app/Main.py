from multiprocessing import Process
from CandleFactory import CandleFactory
import time

print("Iniciando aplicação.")

bitcoin = CandleFactory(1, "USDT_BTC")
monero = CandleFactory(2, "USDT_XMR")

bitcoinProcess = Process(target=bitcoin.run)
moneroProcess = Process(target=monero.run)

bitcoinProcess.start()
moneroProcess.start()
