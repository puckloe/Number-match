#import needed modules
import random
import time

#this function gets a random value from a list and then removes it from the list then returns both
def positionGenerator(List):
    index = random.choice(range(len(List)))
    number = List[index]
    List.pop(index)
    return str(number), List

#displays the values and gets next instruction
def getInstruction(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9):
    print('''
     1 2 3   4 5 6   7 8 9
     
a:   '''+a1+''' '''+a2+''' '''+a3+'''   '''+a4+''' '''+a5+''' '''+a6+'''   '''+a7+''' '''+a8+''' '''+a9+'''
b:   '''+b1+''' '''+b2+''' '''+b3+'''   '''+b4+''' '''+b5+''' '''+b6+'''   '''+b7+''' '''+b8+''' '''+b9+'''
c:   '''+c1+''' '''+c2+''' '''+c3+'''   '''+c4+''' '''+c5+''' '''+c6+'''   '''+c7+''' '''+c8+''' '''+c9+'''

d:   '''+d1+''' '''+d2+''' '''+d3+'''   '''+d4+''' '''+d5+''' '''+d6+'''   '''+d7+''' '''+d8+''' '''+d9+'''
e:   '''+e1+''' '''+e2+''' '''+e3+'''   '''+e4+''' '''+e5+''' '''+e6+'''   '''+e7+''' '''+e8+''' '''+e9+'''
f:   '''+f1+''' '''+f2+''' '''+f3+'''   '''+f4+''' '''+f5+''' '''+f6+'''   '''+f7+''' '''+f8+''' '''+f9+'''

g:   '''+g1+''' '''+g2+''' '''+g3+'''   '''+g4+''' '''+g5+''' '''+g6+'''   '''+g7+''' '''+g8+''' '''+g9+'''
h:   '''+h1+''' '''+h2+''' '''+h3+'''   '''+h4+''' '''+h5+''' '''+h6+'''   '''+h7+''' '''+h8+''' '''+h9+'''
i:   '''+i1+''' '''+i2+''' '''+i3+'''   '''+i4+''' '''+i5+''' '''+i6+'''   '''+i7+''' '''+i8+''' '''+i9+'''

''')
    try:
        instruction = input('''
What is your next move?

to see valid inputs enter i
''')
    except KeyboardInterrupt:
        instruction = "not valid input"
        
    return instruction


#main program
List = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9]

#generate random values for each position
a1, number = positionGenerator(List)
a2, number = positionGenerator(List)
a3, number = positionGenerator(List)
a4, number = positionGenerator(List)
a5, number = positionGenerator(List)
a6, number = positionGenerator(List)
a7, number = positionGenerator(List)
a8, number = positionGenerator(List)
a9, number = positionGenerator(List)
b1, number = positionGenerator(List)
b2, number = positionGenerator(List)
b3, number = positionGenerator(List)
b4, number = positionGenerator(List)
b5, number = positionGenerator(List)
b6, number = positionGenerator(List)
b7, number = positionGenerator(List)
b8, number = positionGenerator(List)
b9, number = positionGenerator(List)
c1, number = positionGenerator(List)
c2, number = positionGenerator(List)
c3, number = positionGenerator(List)
c4, number = positionGenerator(List)
c5, number = positionGenerator(List)
c6, number = positionGenerator(List)
c7, number = positionGenerator(List)
c8, number = positionGenerator(List)
c9, number = positionGenerator(List)
d1, number = positionGenerator(List)
d2, number = positionGenerator(List)
d3, number = positionGenerator(List)
d4, number = positionGenerator(List)
d5, number = positionGenerator(List)
d6, number = positionGenerator(List)
d7, number = positionGenerator(List)
d8, number = positionGenerator(List)
d9, number = positionGenerator(List)
e1, number = positionGenerator(List)
e2, number = positionGenerator(List)
e3, number = positionGenerator(List)
e4, number = positionGenerator(List)
e5, number = positionGenerator(List)
e6, number = positionGenerator(List)
e7, number = positionGenerator(List)
e8, number = positionGenerator(List)
e9, number = positionGenerator(List)
f1, number = positionGenerator(List)
f2, number = positionGenerator(List)
f3, number = positionGenerator(List)
f4, number = positionGenerator(List)
f5, number = positionGenerator(List)
f6, number = positionGenerator(List)
f7, number = positionGenerator(List)
f8, number = positionGenerator(List)
f9, number = positionGenerator(List)
g1, number = positionGenerator(List)
g2, number = positionGenerator(List)
g3, number = positionGenerator(List)
g4, number = positionGenerator(List)
g5, number = positionGenerator(List)
g6, number = positionGenerator(List)
g7, number = positionGenerator(List)
g8, number = positionGenerator(List)
g9, number = positionGenerator(List)
h1, number = positionGenerator(List)
h2, number = positionGenerator(List)
h3, number = positionGenerator(List)
h4, number = positionGenerator(List)
h5, number = positionGenerator(List)
h6, number = positionGenerator(List)
h7, number = positionGenerator(List)
h8, number = positionGenerator(List)
h9, number = positionGenerator(List)
i1, number = positionGenerator(List)
i2, number = positionGenerator(List)
i3, number = positionGenerator(List)
i4, number = positionGenerator(List)
i5, number = positionGenerator(List)
i6, number = positionGenerator(List)
i7, number = positionGenerator(List)
i8, number = positionGenerator(List)
i9, number = positionGenerator(List)

solved = False

#keeps repreating until it is solved
while solved == False:
    instruction = getInstruction(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9)

    #if user needs instructions displayed this happens
    if instruction == "i":
                        print('''

    To move a row right enter the row then either r or l for if you want
    to move it left or right. For example if you want to move the a row
    to the right enter ar or if you want to move it to left enter al

    To move a column up or down enter the name of the row then either
    u or d for if you want to move it up or down. For example if you
    want to move column 1 up or down enter 1u or 1d
    ''')
                        time.sleep(1)
    
    elif instruction == "ar":
        a1Store = a1
        a2Store = a2
        a3Store = a3
        a4Store = a4
        a5Store = a5
        a6Store = a6

        a1 = a7
        a2 = a8
        a3 = a9
        a4 = a1Store
        a5 = a2Store
        a6 = a3Store
        a7 = a4Store
        a8 = a5Store
        a9 = a6Store

    elif instruction == "br":
        a1Store = b1
        a2Store = b2
        a3Store = b3
        a4Store = b4
        a5Store = b5
        a6Store = b6

        b1 = b7
        b2 = b8
        b3 = b9
        b4 = b1Store
        b5 = b2Store
        b6 = b3Store
        b7 = b4Store
        b8 = b5Store
        b9 = b6Store

    elif instruction == "cr":
        c1Store = c1
        c2Store = c2
        c3Store = c3
        c4Store = c4
        c5Store = c5
        c6Store = c6

        c1 = c7
        c2 = c8
        c3 = c9
        c4 = c1Store
        c5 = c2Store
        c6 = c3Store
        c7 = c4Store
        c8 = c5Store
        c9 = c6Store

    elif instruction == "dr":
        d1Store = d1
        d2Store = d2
        d3Store = d3
        d4Store = d4
        d5Store = d5
        d6Store = d6

        d1 = d7
        d2 = d8
        d3 = d9
        d4 = d1Store
        d5 = d2Store
        d6 = d3Store
        d7 = d4Store
        d8 = d5Store
        d9 = d6Store

    elif instruction == "er":
        e1Store = e1
        e2Store = e2
        e3Store = e3
        e4Store = e4
        e5Store = e5
        e6Store = e6

        e1 = e7
        e2 = e8
        e3 = e9
        e4 = e1Store
        e5 = e2Store
        e6 = e3Store
        e7 = e4Store
        e8 = e5Store
        e9 = e6Store

    elif instruction == "fr":
        f1Store = f1
        f2Store = f2
        f3Store = f3
        f4Store = f4
        f5Store = f5
        f6Store = f6

        f1 = f7
        f2 = f8
        f3 = f9
        f4 = f1Store
        f5 = f2Store
        f6 = f3Store
        f7 = f4Store
        f8 = f5Store
        f9 = f6Store

    elif instruction == "gr":
        g1Store = g1
        g2Store = g2
        g3Store = g3
        g4Store = g4
        g5Store = g5
        g6Store = g6
        
        g1 = g7
        g2 = g8
        g3 = g9
        g4 = g1Store
        g5 = g2Store
        g6 = g3Store
        g7 = g4Store
        g8 = g5Store
        g9 = g6Store

    elif instruction == "hr":
        h1Store = h1
        h2Store = h2
        h3Store = h3
        h4Store = h4
        h5Store = h5
        h6Store = h6

        h1 = h7
        h2 = h8
        h3 = h9
        h4 = h1Store
        h5 = h2Store
        h6 = h3Store
        h7 = h4Store
        h8 = h5Store
        h9 = h6Store

    elif instruction == "ir":
        i1Store = i1
        i2Store = i2
        i3Store = i3
        i4Store = i4
        i5Store = i5
        i6Store = i6

        i1 = i7
        i2 = i8
        i3 = i9
        i4 = i1Store
        i5 = i2Store
        i6 = i3Store
        i7 = i4Store
        i8 = i5Store
        i9 = i6Store

    elif instruction == "al":
        a1Store = a1
        a2Store = a2
        a3Store = a3
        a4Store = a4
        a5Store = a5
        a6Store = a6

        a1 = a4Store
        a2 = a5Store
        a3 = a6Store
        a4 = a7
        a5 = a8
        a6 = a9
        a7 = a1Store
        a8 = a2Store
        a9 = a3Store

    elif instruction == "bl":
        b1Store = b1
        b2Store = b2
        b3Store = b3
        b4Store = b4
        b5Store = b5
        b6Store = b6

        b1 = b4Store
        b2 = b5Store
        b3 = b6Store
        b4 = b7
        b5 = b8
        b6 = b9
        b7 = b1Store
        b8 = b2Store
        b9 = b3Store

    elif instruction == "cl":
        c1Store = c1
        c2Store = c2
        c3Store = c3
        c4Store = c4
        c5Store = c5
        c6Store = c6

        c1 = c4Store
        c2 = c5Store
        c3 = c6Store
        c4 = c7
        c5 = c8
        c6 = c9
        c7 = c1Store
        c8 = c2Store
        c9 = c3Store

    elif instruction == "dl":
        d1Store = d1
        d2Store = a2
        d3Store = d3
        d4Store = d4
        d5Store = d5
        d6Store = d6

        d1 = d4Store
        d2 = d5Store
        d3 = d6Store
        d4 = d7
        d5 = d8
        d6 = d9
        d7 = d1Store
        d8 = d2Store
        d9 = d3Store

    elif instruction == "el":
        e1Store = e1
        e2Store = e2
        e3Store = e3
        e4Store = e4
        e5Store = e5
        e6Store = e6

        e1 = e4Store
        e2 = e5Store
        e3 = e6Store
        e4 = e7
        e5 = e8
        e6 = e9
        e7 = e1Store
        e8 = e2Store
        e9 = e3Store
        
        
    elif instruction == "fl":
        f1Store = f1
        f2Store = f2
        f3Store = f3
        f4Store = f4
        f5Store = f5
        f6Store = f6

        f1 = f4Store
        f2 = f5Store
        f3 = f6Store
        f4 = f7
        f5 = f8
        f6 = f9
        f7 = f1Store
        f8 = f2Store
        f9 = f3Store

    elif instruction == "gl":
        g1Store = g1
        g2Store = g2
        g3Store = g3
        g4Store = g4
        g5Store = g5
        g6Store = g6

        g1 = g4Store
        g2 = g5Store
        g3 = g6Store
        g4 = g7
        g5 = g8
        g6 = g9
        g7 = g1Store
        g8 = g2Store
        g9 = g3Store

    elif instruction == "hl":
        h1Store = h1
        h2Store = h2
        h3Store = h3
        h4Store = h4
        h5Store = h5
        h6Store = h6

        h1 = h4Store
        h2 = h5Store
        h3 = h6Store
        h4 = h7
        h5 = h8
        h6 = h9
        h7 = h1Store
        h8 = h2Store
        h9 = h3Store

    elif instruction == "il":
        i1Store = i1
        i2Store = i2
        i3Store = i3
        i4Store = i4
        i5Store = i5
        i6Store = i6

        i1 = i4Store
        i2 = i5Store
        i3 = i6Store
        i4 = i7
        i5 = i8
        i6 = i9
        i7 = i1Store
        i8 = i2Store
        i9 = i3Store

    elif instruction == "1u":
        a1Store = a1
        b1Store = b1
        c1Store = c1
        d1Store = d1
        e1Store = e1
        f1Store = f1

        a1 = d1Store
        b1 = e1Store
        c1 = f1Store
        d1 = g1
        e1 = h1
        f1 = i1
        g1 = a1Store
        h1 = b1Store
        i1 = c1Store

    elif instruction == "2u":
        a2Store = a2
        b2Store = b2
        c2Store = c2
        d2Store = d2
        e2Store = e2
        f2Store = f2
        
        a2 = d2Store
        b2 = e2Store
        c2 = f2Store
        d2 = g2
        e2 = h2
        f2 = i2
        g2 = a2Store
        h2 = b2Store
        i2 = c2Store

    elif instruction == "3u":
        a3Store = a3
        b3Store = b3
        c3Store = c3
        d3Store = d3
        e3Store = e3
        f3Store = f3
        
        a3 = d3Store
        b3 = e3Store
        c3 = f3Store
        d3 = g3
        e3 = h3
        f3 = i3
        g3 = a3Store
        h3 = b3Store
        i3 = c3Store
        
    elif instruction == "4u":
        a4Store = a4
        b4Store = b4
        c4Store = c4
        d4Store = d4
        e4Store = e4
        f4Store = f4

        a4 = d4Store
        b4 = e4Store
        c4 = f4Store
        d4 = g4
        e4 = h4
        f4 = i4
        g4 = a4Store
        h4 = b4Store
        i4 = c4Store

    elif instruction == "5u":
        a5Store = a5
        b5Store = b5
        c5Store = c5
        d5Store = d5
        e5Store = e5
        f5Store = f5

        a5 = d5Store
        b5 = e5Store
        c5 = f5Store
        d5 = g5
        e5 = h5
        f5 = i5
        g5 = a5Store
        h5 = b5Store
        i5 = c5Store

    elif instruction == "6u":
        a6Store = a6
        b6Store = b6
        c6Store = c6
        d6Store = d6
        e6Store = e6
        f6Store = f6

        a6 = d6Store
        b6 = e6Store
        c6 = f6Store
        d6 = g6
        e6 = h6
        f6 = i6
        g6 = a6Store
        h6 = b6Store
        i6 = c6Store

    elif instruction == "7u":
        a7Store = a7
        b7Store = b7
        c7Store = c7
        d7Store = d7
        e7Store = e7
        f7Store = f7

        a7 = d7Store
        b7 = e7Store
        c7 = f7Store
        d7 = g7
        e7 = h7
        f7 = i7
        g7 = a7Store
        h7 = b7Store
        i7 = c7Store

    elif instruction == "8u":
        a8Store = a8
        b8Store = b8
        c8Store = c8
        d8Store = d8
        e8Store = e8
        f8Store = f8

        a8 = d8Store
        b8 = e8Store
        c8 = f8Store
        d8 = g8
        e8 = h8
        f8 = i8
        g8 = a8Store
        h8 = b8Store
        i8 = c8Store

    elif instruction == "9u":
        a9Store = a9
        b9Store = b9
        c9Store = c9
        d9Store = d9
        e9Store = e9
        f9Store = f9

        a9 = d9Store
        b9 = e9Store
        c9 = f9Store
        d9 = g9
        e9 = h9
        f9 = i9
        g9 = a9Store
        h9 = b9Store
        i9 = c9Store

    elif instruction == "1d":
        a1Store = a1
        b1Store = b1
        c1Store = c1
        d1Store = d1
        e1Store = e1
        f1Store = f1

        a1 = g1
        b1 = h1
        c1 = i1
        d1 = a1Store
        e1 = b1Store
        f1 = c1Store
        g1 = d1Store
        h1 = e1Store
        i1 = f1Store 
            
    elif instruction == "2d":
        a2Store = a2
        b2Store = b2
        c2Store = c2
        d2Store = d2
        e2Store = e2
        f2Store = f2

        a2 = g2
        b2 = h2
        c2 = i2
        d2 = a2Store
        e2 = b2Store
        f2 = c2Store
        g2 = d2Store
        h2 = e2Store
        i2 = f2Store

    elif instruction == "3d":
        a3Store = a3
        b3Store = b3
        c3Store = c3
        d3Store = d3
        e3Store = e3
        f3Store = f3

        a3 = g3
        b3 = h3
        c3 = i3
        d3 = a3Store
        e3 = b3Store
        f3 = c3Store
        g3 = d3Store
        h3 = e3Store
        i3 = fStore 
         
    elif instruction == "4d":
        a4Store = a4
        b4Store = b4
        c4Store = c4
        d4Store = d4
        e4Store = e4
        f4Store = f4

        a4 = g4
        b4 = h4
        c4 = i4
        d4 = a4Store
        e4 = b4Store
        f4 = c4Store
        g4 = d4Store
        h4 = e4Store
        i4 = f4Store 
 
    elif instruction == "5d":
        a5Store = a5
        b5Store = b5
        c5Store = c5
        d5Store = d5
        e5Store = e5
        f5Store = f5

        a5 = g5
        b5 = h5
        c5 = i5
        d5 = a5Store
        e5 = b5Store
        f5 = c5Store
        g5 = d5Store
        h5 = e5Store
        i5 = f5Store 
 
    elif instruction == "6d":
        a6Store = a6
        b6Store = b6
        c6Store = c6
        d6Store = d6
        e6Store = e6
        f6Store = f6

        a6 = g6
        b6 = h6
        c6 = i6
        d6 = a6Store
        e6 = b6Store
        f6 = c6Store
        g6 = d6Store
        h6 = e6Store
        i6 = f6Store 

    elif instruction == "7d":
        a7Store = a7
        b7Store = b7
        c7Store = c7
        d7Store = d7
        e7Store = e7
        f7Store = f7

        a7 = g7
        b7 = h7
        c7 = i7
        d7 = a7Store
        e7 = b7Store
        f7 = c7Store
        g7 = d7Store
        h7 = e7Store
        i7 = f7Store 
 
    elif instruction == "18d":
        a8Store = a8
        b8Store = b8
        c8Store = c8
        d8Store = d8
        e8Store = e8
        f8Store = f8

        a8 = g8
        b8 = h8
        c8 = i8
        d8 = a8Store
        e8 = b8Store
        f8 = c8Store
        g8 = d8Store
        h8 = e8Store
        i8 = f8Store 

    elif instruction == "9d":
        a9Store = a9
        b9Store = b9
        c9Store = c9
        d9Store = d9
        e9Store = e9
        f9Store = f9

        a9 = g9
        b9 = h9
        c9 = i9
        d9 = a9Store
        e9 = b9Store
        f9 = c9Store
        g9 = d9Store
        h9 = e9Store
        i9 = f9Store

    else:
        print("that is not a valid option")
        time.sleep(1)

    #checks if the program is 
    if (a1 == a2 == a3 == b1 == b2 == b3 == c1 == c2 == c3) and (a4 == a5 == a6 == b4 == b5 == b6 == c4 == c5 == c6) and (a7 == a8 == a9 == b7 == b8 == b9 == c7 == c8 == c9) and (d1 == d2 == d3 == e1 == e2 == e3 == f1 == f2 == f3) and (d4 == d5 == d6 == e4 == e5 == e6 == f4 == f5 == f6) and (d7 == d8 == d9 == e7 == e8 == e9 == f7 == f8 == f9) and (g1 == g2 == g3 == h1 == h2 == h3 == i1 == i2 == i3) and (g4 == g5 == g6 == h4 == h5 == h6 == i4 == i5 == i6) and (g7 == g8 == g9 == h7 == h8 == h9 == i7 == i8 == i9):
        solved = True

#displays message after the program is complete
print('''

Well Done you solved it

''')
