import subprocess, StringIO

input="""\
uno
dos
"""

p = subprocess.check_output('python test.py', stdin=StringIO.StringIO(input))
print p
