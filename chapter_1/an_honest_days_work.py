# https://dmoj.ca/problem/wc18c3j1

paint = int(input())
paint_per_cap = int(input())
price_per_cap = int(input())

cap_profit = (paint // paint_per_cap) * price_per_cap
leftover_paint = (paint % paint_per_cap)
total_profit = cap_profit + leftover_paint

print(total_profit)
