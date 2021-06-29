import datetime



if __name__ == '__main__':
  
  min1 = datetime.timedelta(seconds=1)
  min5 = datetime.timedelta(seconds=5)
  min10 = datetime.timedelta(seconds=10)

  NextCandle1 = datetime.datetime.now() + min1
  NextCandle5 = datetime.datetime.now() + min5
  NextCandle10 = datetime.datetime.now() + min10

  while True:
    now = datetime.datetime.now()
    if NextCandle1 <= now :
      print("Hora do Candle de 1min")
      NextCandle1 += min1
    if NextCandle5 <= now :
      print("Hora do Candle de 5min")
      NextCandle5 += min5
    if NextCandle10 <= now :
      print("Hora do Candle de 10min")
      NextCandle10 += min10



# import requests, time

# url = "https://poloniex.com/public?command=returnTicker"

# count = 0

# while True:
#   response = requests.get(url) 
#   print(f"status_code: {response.status_code} quantidade de requests: {count}")
#   count += 1
#   time.sleep(1)

#  _______________________________

# Candle1 {}

# Candles1minArray []


# NextCandle1
# NextCandle5
# NextCandle10

# currency_id
# open_value [1x]
# low_value [60x]
# high_value [60x]
# close_value [1x]

# Whilezão:
  # A cada segundo: 
    # Fazer Requests
    # Append Valores Array

  # if TimeCandle1:
    # TimeCandle1 += 1min
    # Pega o max de cada atributo e cria o OBJ Candle
    # Adiciona ao banco de dados
    # Adiciona no array de candles
    # Reseta Atributos

  # if TimeCandle1:

