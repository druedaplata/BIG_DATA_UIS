# coding=utf-8

import numpy as np
input_1="""\
Ancient influences have helped spawn variant interpretations 
of the nature of history which have evolved over the centuries 
and continue to change today. The modern study of history is 
wide-ranging, and includes the study of specific regions and 
the study of certain topical or thematical elements of 
historical investigation. Often history is taught as part of 
primary and secondary education, and the academic study of 
history is a major discipline in University studies
"""

output_1="""\
"chars"	472
"lines"	8
"words"	73
"""

input_2="""\
Ancient influences have helped spawn variant interpretations 
of the nature of history which have evolved over the centuries 
and continue to change today. The modern study of history is 
wide-ranging, and includes the study of specific regions and 
the study of certain topical or thematical elements of 
historical investigation. Often history is taught as part of 
primary and secondary education, and the academic study of 
history is a major discipline in University studies
"""

output_2="""\
"Ancient"	1
"Often"	1
"The"	1
"University"	1
"a"	1
"academic"	1
"and"	5
"as"	1
"centuries"	1
"certain"	1
"change"	1
"continue"	1
"discipline"	1
"education,"	1
"elements"	1
"evolved"	1
"have"	2
"helped"	1
"historical"	1
"history"	4
"in"	1
"includes"	1
"influences"	1
"interpretations"	1
"investigation."	1
"is"	3
"major"	1
"modern"	1
"nature"	1
"of"	8
"or"	1
"over"	1
"part"	1
"primary"	1
"regions"	1
"secondary"	1
"spawn"	1
"specific"	1
"studies"	1
"study"	4
"taught"	1
"the"	5
"thematical"	1
"to"	1
"today."	1
"topical"	1
"variant"	1
"which"	1
"wide-ranging,"	1
"""

input_3="""\
Ancient influences have helped spawn variant interpretations 
of the nature of history which have evolved over the centuries 
and continue to change today. The modern study of history is 
wide-ranging, and includes the study of specific regions and 
the study of certain topical or thematical elements of 
historical investigation. Often history is taught as part of 
primary and secondary education, and the academic study of 
history is a major discipline in University studies
"""

output_3="""\
"avg"	9.125
"""

from checks import *
from os import path

f1 = "files/p_02A_01_TextStats.py"
f2 = "files/p_02A_02_WordCount.py"
f3 = "files/p_02A_03_LineAverage.py" 

max_score = 3
score     = 0
score += check_script(f1, input_1, output_1) if path.exists(f1) else 0
score += check_script(f2, input_2, output_2) if path.exists(f2) else 0
score += check_script(f3, input_3, output_3) if path.exists(f3) else 0

print "---"
print "calificacion: %d/%d (%.0f"%(score, max_score, score*100/max_score)+"%)"
