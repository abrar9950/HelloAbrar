while True:
    print("enter 'x' for exit")
    side=input("enter side length of square:")
    if side=='x':
        break
    else:
        side_length=int(side)
        area_square=side_length*side_length
        
        print("area of square=",area_square,"\n")
