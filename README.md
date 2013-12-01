reverse_gcode
=============
1. открытие файла g-кода в Linuxcnc  добавляет в ~/.srcngc  его интерпретацию (rs274)
    import subprocess
    nst = ['rs274','-g',f,'-t', tooltable, '>' , '~/.srcngc' ]
    st =' '.join(nst)
    r = subprocess.Popen([st], shell=True)
    r.wait()
