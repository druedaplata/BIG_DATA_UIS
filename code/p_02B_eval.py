# coding=utf-8

import numpy as np
input_1="""\
["001", "the car is nice"]
["002", "that car is mine"]
["003", "that shirt is nice"]  
["004", "the car is the best"]
"""

output_1="""\
"best"	["004"]
"car"	["001", "002", "004"]
"is"	["001", "002", "003", "004"]
"mine"	["002"]
"nice"	["001", "003"]
"shirt"	["003"]
"that"	["002", "003"]
"the"	["001", "004"]
"""

input_2="""\
["juan", "pepe"]
["juan", "sebastian"]
["raul", "pepe"]
["juan", "ana"]
["ana", "pepe"]
["pepe", "ana"]
["juan", "ana"]
["ana", "pedro"]
"""

output_2="""\
"ana"	"pedro"
"juan"	"pepe"
"juan"	"sebastian"
"pedro"	"ana"
"pepe"	"juan"
"pepe"	"raul"
"raul"	"pepe"
"sebastian"	"juan"
"""

input_3="""\
["a", 0, 0, 63]
["a", 1, 1, 32]
["b", 0, 0, 69]
["b", 0, 1, 18]
["b", 1, 1, 28]
"""

output_3="""\
[0, 0]	4347
[0, 1]	1134
[1, 1]	896
"""

from checks import *
from os import path

f1 = "files/p_02B_01_InvertedIndex.py"
f2 = "files/p_02B_02_FriendsAsimetric.py"
f3 = "files/p_02B_03_Matmult.py" 

max_score = 3
score     = 0
score += check_script(f1, input_1, output_1) if path.exists(f1) else 0
score += check_script(f2, input_2, output_2) if path.exists(f2) else 0
score += check_script(f3, input_3, output_3) if path.exists(f3) else 0

print "---"
print "calificacion: %d/%d (%.0f"%(score, max_score, score*100/max_score)+"%)"
