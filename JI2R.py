#!/usr/bin/python
# -*- coding: utf-8 -*-
#преобразование G-кода перемещений по дугам из вида с I и J 
#к виду с R,пример:
#исходная строка G2 F40 X62.996 Y40.000 I63.246 J-29.998
#результат       G2 F40 X62.996 Y40.000 R70
import math
f = open('/home/nkp/emc2-dev-80db2a2/configs/EDM/processing/2.ngc','r')
lines = f.readlines()
f.close()
s=2
#----------------------------------------------------------------------------- выделяем X,Y,I,J  текущей строки
l = lines[s]
x1=l.split('X')
x2=x1[1].split(' ')
x=float(x2[0])
print 'X=',x

y1=l.split('Y')
y2=y1[1].split(' ')
y=float(y2[0])
print 'Y=',y

i1=l.split('I')
i2=i1[1].split(' ')
i=float(i2[0])
print 'I=',i

j1=l.split('J')
j2=j1[1].split(' ')
j=float(j2[0])
print 'J=',j
#------------------------------------------------------------------------------выделяем X,Y  предыдущей  строки
l = lines[s-1]
x_old1=l.split('X')
x_old2=x_old1[1].split(' ')
x_old=float(x_old2[0])
print 'X_old=',x_old

y_old1=l.split('Y')
y_old2=y_old1[1].split(' ')
y_old=float(y_old2[0])
print 'Y_old=',y_old

i=x_old +i
j=y_old +j
c = '%.4f' %  math.sqrt(i*i + j*j)
print c

