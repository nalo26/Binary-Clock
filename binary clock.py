import curses
import time

# init curses
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

	
while True:
	w.erase()
	HourFormat = '%H : %M : %S'
	halfscreen = int(sw/2)-int(len(time.strftime(HourFormat))/2)
	w.addstr(sh-5, halfscreen, time.strftime(HourFormat))
	# save the actual time
	hour  = time.strftime('%H')
	min = time.strftime('%M')
	sec = time.strftime('%S')
	# list = [FullyBin, FirstBinValueConvertion, FirstCharConvertion, SecondBinValueConvertion, SecondCharConvertion]
	Bhour = [str(bin(int(hour))[2:]), str(bin(int(hour[:1]))[2:]), '', str(bin(int(hour[1:]))[2:]), '']
	Bmin = [str(bin(int(min))[2:]), str(bin(int(min[:1]))[2:]), '', str(bin(int(min[1:]))[2:]), '']
	Bsec = [str(bin(int(sec))[2:]), str(bin(int(sec[:1]))[2:]), '', str(bin(int(sec[1:]))[2:]), '']
	
	# add some '0' missing for 4 digits
	for i in range(0, 4-len(Bhour[1])):
		Bhour[1] = '0'+Bhour[1]
	for i in range(0, 4-len(Bmin[1])):
		Bmin[1] = '0'+Bmin[1]
	for i in range(0, 4-len(Bsec[1])):
		Bsec[1] = '0'+Bsec[1]
	
	for i in range(0, 4-len(Bhour[3])):
		Bhour[3] = '0'+Bhour[3]
	for i in range(0, 4-len(Bmin[3])):
		Bmin[3] = '0'+Bmin[3]
	for i in range(0, 4-len(Bsec[3])):
		Bsec[3] = '0'+Bsec[3]
	
	if True:  #Just for retract this massiv sh*t
		#replace all 1 by a bloc, and all 0 by '-'
		symb = ''
		Sep = list(Bhour[1])
		for i in range(0, len(Sep)):
			if Sep[i] == '1':
				symb += '█'
			elif Sep[i] == '0':
				symb += '─'
		Bhour[2] = symb
		symb = ''
		Sep = list(Bmin[1])
		for i in range(0, len(Sep)):
			if Sep[i] == '1':
				symb += '█'
			elif Sep[i] == '0':
				symb += '─'
		Bmin[2] = symb
		symb = ''
		Sep = list(Bsec[1])
		for i in range(0, len(Sep)):
			if Sep[i] == '1':
				symb += '█'
			elif Sep[i] == '0':
				symb += '─'
		Bsec[2] = symb
		symb = ''
		Sep = list(Bhour[3])
		for i in range(0, len(Sep)):
			if Sep[i] == '1':
				symb += '█'
			elif Sep[i] == '0':
				symb += '─'
		Bhour[4] = symb
		symb = ''
		Sep = list(Bmin[3])
		for i in range(0, len(Sep)):
			if Sep[i] == '1':
				symb += '█'
			elif Sep[i] == '0':
				symb += '─'
		Bmin[4] = symb
		symb = ''
		Sep = list(Bsec[3])
		for i in range(0, len(Sep)):
			if Sep[i] == '1':
				symb += '█'
			elif Sep[i] == '0':
				symb += '─'
		Bsec[4] = symb
	
	if True: # Printing system to hide	
		# printing system
		w.addch(sh-10, halfscreen+0, list(Bhour[2])[0])
		w.addch(sh-9, halfscreen+0, list(Bhour[2])[1])
		w.addch(sh-8, halfscreen+0, list(Bhour[2])[2])
		w.addch(sh-7, halfscreen+0, list(Bhour[2])[3])
		
		w.addch(sh-10, halfscreen+1, list(Bhour[4])[0])
		w.addch(sh-9, halfscreen+1, list(Bhour[4])[1])
		w.addch(sh-8, halfscreen+1, list(Bhour[4])[2])
		w.addch(sh-7, halfscreen+1, list(Bhour[4])[3])
		
		w.addch(sh-10, halfscreen+5, list(Bmin[2])[0])
		w.addch(sh-9, halfscreen+5, list(Bmin[2])[1])
		w.addch(sh-8, halfscreen+5, list(Bmin[2])[2])
		w.addch(sh-7, halfscreen+5, list(Bmin[2])[3])
		
		w.addch(sh-10, halfscreen+6, list(Bmin[4])[0])
		w.addch(sh-9, halfscreen+6, list(Bmin[4])[1])
		w.addch(sh-8, halfscreen+6, list(Bmin[4])[2])
		w.addch(sh-7, halfscreen+6, list(Bmin[4])[3])
		
		w.addch(sh-10, halfscreen+10, list(Bsec[2])[0])
		w.addch(sh-9, halfscreen+10, list(Bsec[2])[1])
		w.addch(sh-8, halfscreen+10, list(Bsec[2])[2])
		w.addch(sh-7, halfscreen+10, list(Bsec[2])[3])
		
		w.addch(sh-10, halfscreen+11, list(Bsec[4])[0])
		w.addch(sh-9, halfscreen+11, list(Bsec[4])[1])
		w.addch(sh-8, halfscreen+11, list(Bsec[4])[2])
		w.addch(sh-7, halfscreen+11, list(Bsec[4])[3])
	
	# to close program just click esc/escape/echape
	key = w.getch()
	if key == 27:  #esc
		curses.endwin()
		quit()