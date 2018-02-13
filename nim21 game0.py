x=21
player=1
print("the no. is :" , x)

while True :
    print("player" , player)
    while True:
        y=int(input("put a no.:"))
        if y in [1,2,3] and x>=y :
            break
        else:
            print("this no is not allowed ")
    x=x-y
    print("the no. is :" ,x)
    if x==0:
        print("player" , player , "lose")
        break
    
    if player==1 :
        player=2
    else:
        player=1
        
    
