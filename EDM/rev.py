#!/usr/bin/python
import hal, linuxcnc
h = hal.component("rev")
h.newpin("stop", hal.HAL_BIT, hal.HAL_IN)
h.newpin("rev", hal.HAL_BIT, hal.HAL_IN)
h.newpin("rerev-stop", hal.HAL_BIT, hal.HAL_IN)
h.newpin("curent-line",hal.HAL_S32,hal.HAL_IN)
h.newpin("minmax-reset", hal.HAL_BIT, hal.HAL_OUT) 
h.newpin("again_forward", hal.HAL_BIT, hal.HAL_IN)
h.newpin("number-in",hal.HAL_S32,hal.HAL_IN)
h.newpin("number-out", hal.HAL_S32, hal.HAL_OUT) 
    
h.ready()
c = linuxcnc.command()
s = linuxcnc.stat()
def ret_line(number):
	f = open('/home/nkp/temp_rev.ngc', "r") #here prepared code(revers Gcode)
	lines = f.readlines()
	f.close()
	if number >= 0:	
	    print number
	    return lines[number]
	else:
	    return lines[0]		   
def stop():
	c.abort()
	c.wait_complete()
	print 'ok-stop'
 	h["stop"]=0
 	h["rerev-stop"]=0
def back():
	c.mode(linuxcnc.MODE_MDI)
	c.wait_complete()
	c.mdi(ret_line(h["curent-line"]))
	c.wait_complete()
	h["minmax-reset"] = 0
	h["rev"]=0
def again_forward():	
        s.poll()
	if s.interp_state == linuxcnc.INTERP_IDLE:
                c.mode(linuxcnc.MODE_AUTO)
                c.wait_complete()
                s.poll()
                c.wait_complete()
                if s.task_mode == 2 :
                        c.auto(linuxcnc.AUTO_RUN, (h["curent-line"]+1))
                        h["minmax-reset"] = 1
                else:
                        print 'linuxcnc.MODE_AUTO False'                
                h["again_forward"]=0
                print 'ok'
	else:
                h["again_forward"]=0	
try:
    while 1:	 
	if h["stop"]==1:
		stop()		
	if h["rerev-stop"]==1:
		stop()
	if h["rev"]==1:
		back()
	if h["again_forward"]==1:
		again_forward()			
except KeyboardInterrupt:
    raise SystemExit
