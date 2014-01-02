#!/usr/bin/python
import hal, linuxcnc
h = hal.component("rev")
h.newpin("stop", hal.HAL_BIT, hal.HAL_IN)
h.newpin("rev", hal.HAL_BIT, hal.HAL_IN)
h.newpin("rerev", hal.HAL_BIT, hal.HAL_IN)
h.newpin("curent-line",hal.HAL_S32,hal.HAL_IN)
h.newpin("minmax-reset", hal.HAL_BIT, hal.HAL_OUT) 


h.newpin("number-in",hal.HAL_S32,hal.HAL_IN)
h.newpin("number-out", hal.HAL_S32, hal.HAL_OUT) 
    
h.ready()
c = linuxcnc.command()
s = linuxcnc.stat()
def ensure_mode(m, *p):
    s.poll()
    if s.task_mode == m or s.task_mode in p: return True
    if running(do_poll=False): return False
    c.mode(m)
    c.wait_complete()
    return True
    
def running(do_poll=True):
    if do_poll: s.poll()
    return s.task_mode == linuxcnc.MODE_AUTO and s.interp_state != linuxcnc.INTERP_IDLE
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
 	h["stop"]=0
def back():
	c.mode(linuxcnc.MODE_MDI)
	c.wait_complete()
	c.mdi(ret_line(h["curent-line"]))
	c.wait_complete()
	h["minmax-reset"] = 0
	h["rev"]=0
def again_forward():
	
	c.abort()
	c.wait_complete()
#	s.poll()
	'''if s.interp_state == linuxcnc.INTERP_IDLE:
		print c.wait_complete(),':c.wait_complete()'
		ensure_mode(linuxcnc.MODE_AUTO)
		if ensure_mode(linuxcnc.MODE_AUTO) :
			c.auto(linuxcnc.AUTO_RUN, (h["curent-line"]+1))
		else:
			print 'linuxcnc.MODE_AUTO False'
		h["minmax-reset"] = 1
		h["rerev"]=0
		print 'ok'
	else:
		h["rerev"]=0
		return'''
	h["rerev"]=0
try:
    while 1:	 
	if h["stop"]==1:
		stop()
	if h["rev"]==1:
		back()		
	if h["rerev"]==1:
		again_forward()	
except KeyboardInterrupt:
    raise SystemExit
