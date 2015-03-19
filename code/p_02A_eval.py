# coding=utf-8

import numpy as np
input_1="""\
Llegó Sancho a su amo marchito y desmayado, tanto que no 
podía arrear a su jumento. Cuando así le vió Don Quijote,
le dijo: Ahora acabo de creer, Sancho bueno, que aquel 
castillo o venta es encantado sin duda, porque aquellos 
que tan atrozmente tomaron pasatiempo contigo, ¿qué podían 
ser sino fantasmas y gente del otro mundo? Y confirmo ésto, 
por haber visto que cuando estuve por las bardas del corral 
mirando los actos de tu triste tragedia, no me fue posible 
subir por ellas, ni menos pude apearme de Rocinante, porque 
me debían de tener encantado; que te juro por la fe de quien 
soy, que si pudiera subir o apearme, que yo te hubiera vengado 
de manera que aquellos follones y malandrines se acordaran de 
la burla para siempre.
"""

output_1="""\
"chars"	740
"lines"	13
"words"	131
"""

from checks import *
max_score = 1
score     = 0
score += check_script("files/p_02A_01_TextStats.py", input_1, output_1)

print "---"
print "calificacion: %d/%d (%.0f"%(score, max_score, score*100/max_score)+"%)"
