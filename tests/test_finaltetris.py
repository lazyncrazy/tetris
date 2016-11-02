import finaltetris
class Test_item:
    def test_piece(self):
        flag=0
        item = finaltetris.Gameplay()
        h = item.height
        w=item.widths
        if h > 0 and w > 0 and h<=3 and w<=3:
            flag=1
        assert flag == 1
    def test_right(self):
        x = 13
        item=gameplay.Gameplay()
        item.right = 2
        x = finaltetris.block().moveright(item,x)
        assert x == 14
    def test_left(self):
         x=13
         item = gameplay.Gameplay()
         piece.left = 2
         x = item.block().moveleft(item,x)
         assert x == 12
    def test_updatescore_par1(self,tpoints,par):
        tpoints = 100
        par = 1
        tpoints = finaltetris.Gameplay().updatescore(tpoints,par)
        assert tpoints == 110

    def test_updatescore_par2(self,tpoints,par):
        tpoints = 100
        par = 2
        tpoints = finaltetris.Gameplay().updatescore(tpoints,par)
        assert tpoints == 200
    def test_pulldown(self,y,x,piece,screen):
        for i in 31:
            bits[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        bits[32]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        x=13
        y=3
        piece = finaltetris.Gameplay()
        myscreen=curses.initscr()
        curses.curs_set(0)

        diff = finaltetris.Gameplay().pulldown(y,x,bits,piece,myscreen)
        assert diff==29

    def test_rotate(self,y,x,bits,piece):
        y=5
        x=20
        for i in range(1,30):
            for j in  range(1,32):
                bits[i][j] = 0
        piece = finaltetris.Gameplay()
        piece.direction=0
        finaltetris.block().rotate(y,x,bits,piece)
        assert piece.direction == 1

    def test_rowfull(self,bits,tpoints,level):
        for i in 31:
            bits[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        bits[32]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        bits[31]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        tpoints=100
        level=1
        flag=0
        bits,tpoints = finaltetris.Gameplay().checkRowFull(bits,tpoints,level)
        for i in 31:
            temp[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        bits[32]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        if tpoints == 200 and bits==temp:
            flag=1
        assert flag==1

    def test_checkPiecePos(self,y,x,bits,piece):
        ovl=0
        for i in 31:
            bits[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        bits[32]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        bits[31]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        y = 31
        x=15
        piece = gameplay.Gameplay()
        ovl = gameplay.board.checkPiecePos(y,x,bits,piece)
        assert ovl == 1
