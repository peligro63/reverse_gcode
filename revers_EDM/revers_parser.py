f.write("")
f.close()
len_file = len(lines)
f = open('/home/nkp/temp_rev.ngc','w')
f.write("G1 F40 X0 Y0 \n")
f.close()

while x<len_file -1 :
        if lines[x].find('G2')!=-1  and lines[x-1].find('G1')==-1 : # если текущая строка содержит G2 а предыдущая не содержит G1
		f = open('/home/nkp/temp_rev.ngc','a')
		r=lines[x]
		a=r.split('R')
		w=a[1]
		z=lines[x-1].replace('G2','G3')
		a=z.split('R')
		ww=a[0]
		f.write(ww+'R'+w)
		x=x+1
		f.close()

        elif lines[x].find('G3')!=-1  and lines[x-1].find('G1')==-1 :# если текущая строка содержит G3 а предыдущая не содержит G1
		f = open('/home/nkp/temp_rev.ngc','a')
		r=lines[x]
		a=r.split('R')
		w=a[1]
		z=lines[x-1].replace('G3','G2')
		a=z.split('R')
		ww=a[0]
		f.write(ww+'R'+w)
		x=x+1
		f.close()
        elif lines[x].find('G2')!=-1  and lines[x-1].find('G1')!=-1  : # если текущая строка содержит G2 а предыдущая содержит G1
		f = open('/home/nkp/temp_rev.ngc','a')
		a=lines[x].split('R')
		w=a[1]
		r=lines[x-1].replace('G1','G3')
		ww=r.replace ('\n','')
		f.write(ww+'R'+w)
		x=x+1
		f.close()
           
        elif lines[x].find('G3')!=-1 and lines[x-1].find('G1')!=-1 : # если текущая строка содержит G3 а предыдущая содержит G1
		f = open('/home/nkp/temp_rev.ngc','a')       # открываем файл на добавление
		a=lines[x].split('R')   # разделяем строку lines[x] по символу 'R' в список
		w=a[1]                  # берем из разделения второй элемент [1] (нумерация с нуля)
		r=lines[x-1].replace('G1','G2') # меняем G1 на G2 в строке lines[x-1] 
		ww=r.replace ('\n', '')  # убираем  в конце перенос строки
		f.write(ww+'R'+w)   # пишем в файл 
		x=x+1
		f.close()
        elif lines[x].find('G1')!=-1  : # если текущая строка содержит G1 
		f = open('/home/nkp/temp_rev.ngc','a')
		f.write(lines[x-1])
		x=x+1
		f.close()

        else :
		f = open('/home/nkp/temp_rev.ngc','a')
		f.write('\n')
		x=x+1
		f.close()
