A, B, X, Y = map(int, input().split())
mes =2*A + B
ronald = 2*X+Y
if(mes<ronald):
    print("Ronaldo")
elif(mes>ronald):
    print("Messi")
else:
    print("Equal")