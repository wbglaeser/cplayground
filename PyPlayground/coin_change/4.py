amount = 4
coins = [1,2,3]

dp = [1] + [0]*amount
for coin in coins:
    print("new coin")
    for i in range(coin, amount+1):
        dp[i] += dp[i-coin]
        print(dp)
print(dp)
print(dp[amount])
