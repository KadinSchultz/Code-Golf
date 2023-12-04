# Problem: Farey Sequence
# Link: https://code.golf/farey-sequence#python
# Solutions characters: 104

r=range
print('\n'.join([*zip(*sorted({j/i:f'{j}/{i}'for i in r(50,0,-1)for j in r(i+1)}.items()))][1]))
