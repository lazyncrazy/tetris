import curses
def draw_frame(myscreen):
	myscreen.addstr(2,3,"################################")
        myscreen.addstr(36,3,"CONTROLS--> left:a right:d down:s drop:spacebar")
        myscreen.addstr(38,3,"'@' is a special character which clears the row on which it falls")
	for n in range(3,33):
		myscreen.addstr(n,3,"#                              #")
	myscreen.addstr(33,3,"################################")
