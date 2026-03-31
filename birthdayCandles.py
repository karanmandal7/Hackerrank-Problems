def Candles(candles):
    return candles.count(max(candles))

my_candles = [ 1, 4, 6, 3, 8, 9, 9]

result = Candles(my_candles)
print(result)