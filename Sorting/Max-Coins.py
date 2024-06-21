# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
def max_coins(piles):
    piles.sort()
    max = 0
    base = len(piles) // 3
    while base < len(piles):
        max += piles[base]
        print(piles[base])
        base += 2
    return max
