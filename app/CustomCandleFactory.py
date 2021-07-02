from dao.CandleDAO import CandleDAO

# Recebe o ida da moeda e o tempo do candle a ser criado, pegas as informações no db e cria um novo candle com o tempo especificado.


def custom_candle_factory(currency_Id, time):
    dao = CandleDAO()

    data = dao.get_1min_candles_by_currency_id_and_time(currency_Id, time)
    open_value = data[0][0]
    close_value = data[-1][1]
    high_value = data[0][2]
    low_value = data[0][3]
    for linha in data:
        if linha[2] > high_value:
            high_value = linha[2]
        if linha[3] < low_value:
            low_value = linha[3]

    print(f'Criando candle de {time}min.')
    dao.add_candle(
        currencyId=currency_Id,
        frequency=time,
        openValue=open_value,
        closeValue=close_value,
        lowValue=high_value,
        highValue=low_value
    )
