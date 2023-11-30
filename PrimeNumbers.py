# Problem: Prime Numbers
# Link: https://code.golf/prime-numbers#python
# Solutions characters: 62

r=range(2,99)
for x in r: sum([x%d==0 for d in r])<2==print(x)
