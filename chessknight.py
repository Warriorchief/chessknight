def chessKnight(cell):
    out=0
    fyles=['a','b','c','d','e','f','g','h']
    fyle=fyles.index(cell[0])+1
    start=(fyle,int(cell[1]))
    print('start is',start)
    if start[0]+1<=8 and start[1]+2<=8:
        print('nne is on board')
        out+=1
    if start[0]+2<=8 and start[1]+1<=8:
        print('ene is on board')
        out+=1
    if start[0]+2<=8 and start[1]-1>=1:
        print('ese is on board')
        out+=1
    if start[0]+1<=8 and start[1]-2>=1:
        print('sse is on board')
        out+=1
    if start[0]-1>=1 and start[1]-2>=1:
        print('ssw is on board')
        out+=1
    if start[0]-2>=1 and start[1]-1>=1:
        print('wsw is on board')
        out+=1
    if start[0]-2>=1 and start[1]+1<=8:
        print('wnw is on board')
        out+=1
    if start[0]-1>=1 and start[1]+2<=8:
        print('nnw is on board')
        out+=1
    print(out)
    return out