# Problem: Fizz Buzz  
# Link: https://code.golf/fizz-buzz#python
# Solutions characters: 66

for v in range(1,101):print('Fizz'*(not v%3)+'Buzz'*(not v%5)or v)
