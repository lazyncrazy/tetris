import curses, random, time
from frame import *
class Gameplay:
	def __init__(self):
		self.selectPiece()
        def checkRowEmpty(self,bits):
	    for j in range(30):
                if bits[j]==[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
                    yes=1
            return yes
            
	
	def selectPiece(self):
		shapes=[]
		shapes.append([[1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]])
		shapes.append([[0,1,1,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]])
		shapes.append([[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
		shapes.append([[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]])
		shapes.append([[1,1,1,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]])
		shapes.append([[1,1,1,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]])
                shapes.append([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
		widths=[]
		widths.append(3)
		widths.append(3)
		widths.append(4)
		widths.append(2)
		widths.append(3)
		widths.append(3)
                widths.append(1)
		heights=[]
		heights.append(2)
		heights.append(2)
		heights.append(1)
		heights.append(2)
		heights.append(2)
		heights.append(2)
                heights.append(1)
		__s=random.randint(0,2)
                __ss=random.randint(0,20)
                if __ss!=1:
		    self.shape=shapes[__s]
		    self.height=heights[__s]
		    self.width=widths[__s]
                    self.flag=0
                else:
                    self.shape=shapes[6]
                    self.height=heights[6]
                    self.width=widths[6]
		__d=random.randint(0,3)
		self.direction=__d
        def updatescore(self,tpoints,par):
            if par==1:
                tpoints+=10
            if par==2:
                tpoints+=100
            return tpoints
        def checkRowFull(self,bits,tpoints,level):
	    
	    for j in range(30-level+1):
	        if bits[j]==[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
		    for k in range(j,0,-1):
			bits[k]=bits[k-1]
			bits[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    tpoints=Gameplay().updatescore(tpoints,2)
            return bits,tpoints


	def update_bits(self,y,x,bits):
		for h in range(self.height):
			for w in range(self.width):
				if self.shape[h][w]==1:
					if self.direction==0:
						bits[y+h-3][x+w-4]=1
					elif self.direction==2:
						bits[y+((self.height-1)-h-3)][x+((self.width-1)-w)-4]=1
					elif self.direction==1:
						bits[y+w-3][x+((self.height-1)-h)-4]=1
					elif self.direction==3:
						bits[y+((self.width-1)-w)-3][x+h-4]=1
		return bits

	def get_width(self):
		if self.direction==1 or self.direction==3:
			return self.height
		elif self.direction==0 or self.direction==2:
			return self.width
class board(Gameplay):    

	def checkPiecePos(self,y,x,bits,piece):
		ovl=0
		for h in range(piece.height):
			for w in range(piece.width):
				if piece.shape[h][w]==1:
					if piece.direction==0:
						yt=y+h
						xt=x+w
					elif piece.direction==1:
						yt=y+w
						xt=x+((piece.height-1)-h)
					elif piece.direction==3:
						yt=y+((piece.width-1)-w)
						xt=x+h
					elif piece.direction==2:
						yt=y+((piece.height-1)-h)
						xt=x+((piece.width-1)-w)
					if xt-4<0:
						ovl=1
					elif xt-4>29:
						ovl=1
					elif bits[yt-3][xt-4]==1:
						ovl=1
		return ovl
	
        def pulldown(self,y,x,bits,piece,screen):
                mind=100
                #print "h1"
		for h in range(piece.height):
			for w in range(piece.width):
				if piece.shape[h][w]==1:
					if piece.direction==0:
						yt=y+h
						xt=x+w
					elif piece.direction==1:
						yt=y+w
						xt=x+((piece.height-1)-h)
					elif piece.direction==2:
						yt=y+((piece.height-1)-h)
						xt=x+((piece.width-1)-w)
					elif piece.direction==3:
						yt=y+((piece.width-1)-w)
						xt=x+h
                                        for m in range(yt-2,31):
                                            if bits[m][xt-4]==1:
                                                diff=m-yt+3
                                                if diff < mind:
                                                    mind=diff
                return mind

class block(Gameplay):
	def rotate(self,y,x,bits,piece):
		overlap=0
		piece.direction=piece.direction+1
		if piece.direction>3:
			piece.direction=0
		
		if board().checkPiecePos(y,x,bits,piece):
			piece.direction=piece.direction-1
			if piece.direction<0:
				piece.direction=3
	def draw(self,piece,y,x,screen,bits):
		piece.cleft=1
		piece.cright=1
		piece.falling=1
		for h in range(piece.height):
			for w in range(piece.width):
			    if piece.shape[h][w]==1:
					if piece.direction==0:
						yt=y+h
						xt=x+w
					elif piece.direction==1:
						yt=y+w
						xt=x+((piece.height-1)-h)
					elif piece.direction==3:
						yt=y+((piece.width-1)-w)
						xt=x+h
					elif piece.direction==2:
						yt=y+((piece.height-1)-h)
						xt=x+((piece.width-1)-w)
					screen.addstr(yt,xt,"@")
					if bits[yt-2][xt-4]==1:
						piece.falling=0
                                                if piece.width==1 and yt-2<30 and piece.flag==0:
                                                    bits[yt-2]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		                                    for k in range(yt-2,0,-1):
			                                bits[k]=bits[k-1]
			                                bits[0]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                                    piece.flag=1
                                                    
					if xt-5<0:
						piece.cleft=0
					elif bits[yt-3][xt-5]==1:
						piece.cleft=0
					if xt-3>29:
						piece.cright=0
					elif bits[yt-3][xt-3]==1:
						piece.cright=0
     
	def moveleft(self,piece):
		return piece.cleft
        def moveright(self,cright):
                return piece.cright

            

myscreen=curses.initscr()
curses.curs_set(0)

curses.noecho()
piece=Gameplay()
qui=1
level=1
incr=0
piece2=Gameplay()
curses.halfdelay(1)

while qui:
	n=0
	x=17
	y=3
	points=0
        #bits[tempvar1][tempvar2]=1;
	bits=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	t=time.time()
	while 1:
		c=myscreen.getch()
		if c==ord('q'):
			break
		elif c==ord('w'):
			block().rotate(y,x,bits,piece)
		elif c==ord('a'):
			x=x-block().moveleft(piece)
		elif c==ord('d'):
			x=x+block().moveright(piece)
		elif c==ord('s'):
			if piece.falling and fall_temp:
				y=y+1
                elif c==ord(' '):
                    if piece.width==1:
                        y=y+board().pulldown(y,x,bits,piece,myscreen)-2
                    else:
                        y=y+board().pulldown(y,x,bits,piece,myscreen)-1
   

		fall_temp=1
		draw_frame(myscreen)
		try:
			block().draw(piece,y,x,myscreen,bits)
		except:
			break
		for j in range(30):
			for i in range(29):
				if bits[j][i]==1:
					myscreen.addstr(j+3,i+4,"%")
		if time.time()-t>1/level:
			tpoints=0
			if piece.falling==0:
				bits=piece.update_bits(y,x,bits)
				x=17
				y=3
                                tpoints=Gameplay().updatescore(tpoints,1)
				piece.selectPiece()
				if board().checkPiecePos(y,x,bits,piece):
					break
			y=y+piece.falling
			fall_temp=not piece.falling
			t=time.time()
                        bits,tpoints=Gameplay().checkRowFull(bits,tpoints,level)
			points=points+tpoints
			myscreen.addstr(1,3,"Score: "+str(points))
                        incr=points-200*(level-1)
                        if incr>200:
                            level=level+1
                            bits.append([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
                            bits[30-level+1]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                        myscreen.addstr(35,3,"level: "+str(level))

	myscreen.refresh()
        
	myscreen.addstr(19,7," q to quit  ")
	myscreen.addstr(13,7," p to play again")
	while 1:
		c=myscreen.getch()
		if c==ord('q'):
			qui=0
			break
		elif c==ord('p'):
			break
	myscreen.refresh()
curses.echo()
curses.endwin()
