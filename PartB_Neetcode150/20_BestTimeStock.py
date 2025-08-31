# ====== Best time to buy a stock
""" Question:
1. Given an array prices where prices[i] is the prices of a given stock on the ith day.
Max profix, is choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.

"""

prices = [7, 1, 5, 3, 6, 4]
# output = 5
# return max profix you can achieve from this


def bestStock(prices):
    minPrice = float('inf')  # incase it's empty
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        # profit = sellingPrice (curPrice) - costPrice (curMIn seen)
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice

    return maxProfit


print("Max profit = ", bestStock([]))
