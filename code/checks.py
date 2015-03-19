import cStringIO
import numpy as np
import subprocess

def check_function(f, input, output):
    buf = cStringIO.StringIO()

    for i in input.split("\n"):
        if len(i.rstrip())!=0:
            print >> buf, f(**eval(i))

    r = buf.getvalue()==output
    fname = "funcion '"+f.__name__+"'"
    if r:
       print fname,"correcto!!"
    else:
       print fname,"** INCORRECTO ... VERIFICA TU CODIGO **"
    return r


def check_script(script, input, output):

    s=cStringIO.StringIO(input)

    p = subprocess.Popen(['python', script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    poutput, poutput_err = p.communicate(s.read())
    fname = "script '"+script+"'"
    r = output==poutput
    if r:
       print fname,"correcto!!"
    else:
       print fname,"** INCORRECTO ... VERIFICA TU CODIGO **"
    return r
     

