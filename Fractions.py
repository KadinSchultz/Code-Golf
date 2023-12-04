# Problem: Fractions
# Link: https://code.golf/fractions#python
# Solutions characters: 103

import sys
from fractions import*
for i in sys.argv[1:]:print('%d/%d'%(Fraction(i).as_integer_ratio()))
