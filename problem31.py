coins = [200, 100, 50, 20, 10, 5, 2, 1]
goal = 200

def chase(coins, goal):
    total = 0
    x = goal / coins[0]
    
    new_coins = coins[1:]
    
    if len(new_coins):
        for i in range(x, -1, -1):
            new_goal = goal - (i * coins[0])
            if new_goal == 0:
                total += 1
            else:
                total += chase(new_coins, new_goal)
    else:
        total = 1
    return total

print chase(coins, goal)
