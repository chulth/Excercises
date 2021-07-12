
def max_coins(piles):
    piles = sorted(piles, reverse=True)
    print(piles)
    count = 1
    result = 0
    for i,coins in enumerate(piles):
        if i == count:
            result += coins
            count += 3
    return result

        
def example_max_coins(piles):
    return sum(sorted(piles, reverse=True)[1::3])
    

