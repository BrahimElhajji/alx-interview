#!/usr/bin/python3
""" making changes"""


def makeChange(coins, total):
    """MakeChange Funtion"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    return num_coins if total == 0 else -1
