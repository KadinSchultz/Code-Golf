# Problem: Fibonacci
# Link: https://code.golf/fibonacci#python
# Solutions characters: 52

# s = output sequence

s=(0,1)
while s[-1]<2e6:print(s[-2]);s+=s[-2]+s[-1],
