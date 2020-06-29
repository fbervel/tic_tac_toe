# write your code here
cells = "_________"
cells = cells.upper()
cell_one = [list(cells[0:3]),list(cells[3:6]),list(cells[6:9])]
#result = ""
cerrado = False
while not cerrado:  # bucle de recorrido
#contador = 0
#while contador < 2:
    print("---------")
    for x in cell_one:
        print("|",end=" ")
        for y in x:
            #print(y,end=" ")
            print(y if y != "_" else " ",end=" ")
        print("|")
    print("---------")

    lineas = []
    # horizontal
    lineas.append([x for x in cell_one[0]])
    lineas.append([x for x in cell_one[1]])
    lineas.append([x for x in cell_one[2]])

    # vertical
    lineas.append([cell_one[0][0], cell_one[1][0], cell_one[2][0]])
    lineas.append([cell_one[0][1], cell_one[1][1], cell_one[2][1]])
    lineas.append([cell_one[0][2], cell_one[1][2], cell_one[2][2]])

    # diagonal
    lineas.append([cell_one[2][0], cell_one[1][1], cell_one[0][2]])
    lineas.append([cell_one[0][0], cell_one[1][1], cell_one[2][2]])

    num = 0
    blank = 0
    count_x = 0
    count_y = 0

    for pos in lineas:
        if pos[0] == '_' or pos[1] == '_' or pos[2] == '_':
            blank += 1
        elif pos[0] == pos[1] == pos[2]:
            num += 3
            winner = pos[0]

    count_x, count_y = cells.count('X'), cells.count('O')
    cerrado = False

    if count_x > count_y:
        letra = 'O'
    else:
        letra = 'X'
    #letra = 'X'
    
    if num > 3 or abs(count_x - count_y) >= 2:
        print("Impossible")
        cerrado = True
    elif num == 3:
        print(winner, 'win')
        cerrado = True
    elif blank == 0 and (count_x + count_y) == 9:
        print("Draw")
        cerrado = True
    elif blank > 0:
        #validar la entrada
        #pos_x, pos_y = input("Enter the coordinates: ").split()
        valido = True
        
        # quitar en el ultimo paso
        #if contador == 1:
        #    valido = False

        while valido:
            pos_x, pos_y = input("Enter the coordinates: ").split()

            if not pos_x.isdigit() or not pos_y.isdigit():
                valido = True
                print("You should enter numbers!")
            elif pos_x not in '123' or pos_y not in '123':
                print("Coordinates should be from 1 to 3!")
                valido = True
            else:
                y = 3 - int(pos_y)
                x = int(pos_x) - 1
                if cell_one[y][x] != "_":
                    print('This cell is occupied! Choose another one!')
                    valido = True
                else:
                    cell_one[y][x] = letra
                    valido = False

        # asignando la nueva cadena
        cells = "".join(x for celda in cell_one for x in celda)
    #contador += 1