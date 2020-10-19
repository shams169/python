def profit(vals):

    min_buy = vals[0]
    max_sell = vals[1]
    max_profit = max_sell - min_buy

    for i in range(1, len(vals)):
        if vals[i] < min_buy:
            min_buy = vals[i]
        if vals[i] > max_sell:
            max_sell = vals[i]
        max_profit = max(max_profit, (max_sell - min_buy))

    print(max_profit, min_buy, max_sell)


profit([1, 2, 3, 4, 3, 2, 1, 2, 5])
