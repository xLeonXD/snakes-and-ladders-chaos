import random

"""

5 layers of data is used for now

layer 1 - > map_dict, stores map nums and coordinates  - > layer 2 - > layer 3
layer 2 - > board , stores only the nums , constantly being emptied and filled  - > layer 3
layer 3 - > display , not a data but uses the other 2 for showing the data - > layer 4 , - > layer 5
layer 4 - > new_dict , stores map nums and coordinates, its better than the first one cause the first one had desync 
                                                        problems with the display but with this its fixed
layer 5 - > new_board , stores only the nums , constantly being emptied and filled

"""
# no snake on cxry - done
# make snakes into a list with the values u get from start - done
# help. - nope

# player movement
# for r2s move backward - done but reverse
# could limit the y to 2%0 only or you could use old map_dict for odd maps. no need , the bug is fixed - done
# the player/cpu limit can be the amount of columns on available map - done
# player + cpu <= x - done

# use 2 functions
# one to calculate the next pos
# one to move and place the players
# for the start of the game, use for and the player_dict and put everyone
# save values like oldposc,oldposr = move(oldposc,oldposr)
# this way u can replace the old ones with numbers and get the new pos of players for future
# have an if statement for first movement, so it also generates the oldpos


# make the odd row movement calc



# ----------- Architecture ----------- #
"""create_board(map_dict,board,x,y)
display_board(board,x,y)
map_dict,snakes_ladders = create_snake(snakes_ladders, map_dict, board, x, y)
map_dict,snakes_ladders = create_ladder(snakes_ladders,map_dict,board,x,y)
map_dict_org = map_dict.copy() # Static backup for restoring cells during movement (no players)
print(snakes_ladders)

board= []
create_board(map_dict,board,x,y)
display_board(board,x,y)

player_list = create_player2(2,2,x,y)
map_dict,last_location = player_placement(map_dict,player_list,True)

board = []
create_board(map_dict, board, x, y)
display_board(board,x,y)

final_col,final_row = calculate_pos(1,1,x,y,20,map_dict)
player_movement(map_dict,map_dict_org,"player1",player_list,last_location, final_col, final_row, snakes_ladders)

board = []
create_board(map_dict, board, x, y)
display_board(board,x,y)"""


map_dict = {}
board = []
snakes_ladders = {}
player_turn = 0

x,y = 10,10

def map_create(map_dict,x,y):
    # this is simple enough i guess.
    # makes a dictionary with x*y amount of squares with a coordinate system
    sqr = 1
    sqr2 = 1
    x1 = x
    for i in range(1,y+1):
        #print(f"x",i)
        for j in range(1,x+1):
            if i % 2 == 0:
                if x1 == x:
                    sqr2 = sqr -1
                if x1 == 0:
                    x1 = x
                    sqr2 = sqr - 1
                #print (sqr2)
                #print(f"yy",j)
                map_dict[f"c{j}r{i}"] = sqr2 + x1
                x1 -= 1
            else:
                #print(f"y",j)
                map_dict[f"c{j}r{i}"] = sqr
            sqr += 1
    return map_dict


def create_board(map_dict,board,x,y):
    # also another simple one
    # it takes the dictionary and puts the values into a list
    for i in range(1,y+1):
        x1 = 0
        for j in range(1,x+1):
            if x1 <= x:
                #if i % 2 == 0:
                #    pass
                #else:
                board.append(map_dict[f"c{j}r{i}"])
                #print(map_dict[f"c{j}r{i}"])
                x1 += 1
    return board


def display_board(board,x,y,*args):
    # this one is a little complicated.
    # if the args are empty it will just display the map
    # but if its not it will also make a new dictionary which is more in synced with other functions and display
    # there are some comments up on this file
    sqrs = x*y - 1
    sqrs1 = x*y - 1
    y1 = 1
    y2 = y
    x2 = x
    while y1 <= y:
        newb = []
        x1 = x -1
        x2 = x -1
        for i in range(x):
            """if x1 == x -1 :
                sqrs1 = sqrs
            """""""if y1 % 2 ==0:
                newb.append(board[sqrs1 - x1])

                x1 -= 1
            else:"""
            newb.append(board[sqrs])
            sqrs -= 1
            if args:
                temp = args[0]
                temp[f"c{i+1}r{y2}"] = board[sqrs1]
                sqrs1 -= 1
        if not args:
            print(newb)
        y1 += 1
        y2 -= 1
    if args:
        new_board = []
        new_board = create_board(temp,new_board,x,y)
        return args[0],new_board
    else:
        return



def create_snake(snakes_ladders,map_dict,board,x,y):
    # my favorite. I hate this function and i will refactor it someday to also absorb create_ladder
    # its really long and i cant really explain it in a few comments but i think it should be simple enough ?
    # p.s ccrr is current column current row

    snakes = 0
    ladders = 0
    snake_limit = False
    if y < 3 and x < 3:
        snakes = 0
        ladders = 0
    elif y <= 5 and x <= 5:
        snakes = random.randint(1,2)
        ladders = 1
    elif y <= 10 and x <= 10:
        snakes = random.randint(2,4)
        ladders = 2
    elif y > 10 and x > 10:
        snakes = random.randint(3,5)
        ladders = 2

    for _ in range(snakes):
        # head snake generation
        n = 0
        snake_place = False
        temp_list = []
        for temp in range(3,y):
            temp_list.append(temp)
        finish = True
        work3 = True
        work2 = True
        while finish:
            if snake_limit:
                break
            work = True
            if temp_list == []:
                break
            else:
                r = random.choice(temp_list)
            c = random.randint(1,x)
            i = c
            # check for duplicates in same row
            print("retry")
            while work:
                if temp_list == []:
                    work = False
                    finish = False
                    snake_limit = True
                    #temp_list_limit = True
                    break
                if map_dict[f"c{i}r{r}"] == map_dict[f"c{x}r{y}"]:
                    print("error 0")
                    temp_list.remove(r)
                    work = False
                    break
                if map_dict[f"c{i}r{r}"] == "V" or map_dict[f"c{i}r{r}"] == "S" or map_dict[f"c{i}r{r}"] == "^" or map_dict[f"c{i}r{r}"] == "H" or map_dict[f"c{i}r{r}"] == "#" or map_dict[f"c{i}r{r}"] == "A":
                    print("error")
                    temp_list.remove(r)
                    work = False
                    break
                if not i == x:
                    if map_dict[f"c{i+1}r{r}"] == "V" or map_dict[f"c{i+1}r{r}"] == "S" or map_dict[f"c{i+1}r{r}"] == "^" or map_dict[f"c{i+1}r{r}"] == "H" or map_dict[f"c{i+1}r{r}"] == "#" or map_dict[f"c{i+1}r{r}"] == "A":
                        print("error")
                        temp_list.remove(r)
                        work = False
                        break
                if not i == 1:
                    if map_dict[f"c{i-1}r{r}"] == "V" or map_dict[f"c{i-1}r{r}"] == "S" or map_dict[f"c{i-1}r{r}"] == "^" or map_dict[f"c{i-1}r{r}"] == "H" or map_dict[f"c{i-1}r{r}"] == "#" or map_dict[f"c{i-1}r{r}"] == "A":
                        print("error")
                        temp_list.remove(r)
                        work = False
                        break
                if  not r == 1:
                    if map_dict[f"c{i}r{r-1}"] == "V" or map_dict[f"c{i}r{r-1}"] == "S" or map_dict[f"c{i}r{r-1}"] == "^" or map_dict[f"c{i}r{r-1}"] == "H" or map_dict[f"c{i}r{r-1}"] == "#" or map_dict[f"c{i}r{r-1}"] == "A":
                        print("error 2")
                        temp_list.remove(r)
                        work = False
                        break
                    if not i == x:
                        if map_dict[f"c{i+1}r{r-1}"] == "V" or map_dict[f"c{i+1}r{r-1}"] == "S" or map_dict[f"c{i+1}r{r-1}"] == "^" or map_dict[f"c{i+1}r{r-1}"] == "H" or map_dict[f"c{i+1}r{r-1}"] == "#" or map_dict[f"c{i+1}r{r-1}"] == "A":
                            print("error 2")
                            temp_list.remove(r)
                            work = False
                            break
                    if not i == 1:
                        if map_dict[f"c{i-1}r{r-1}"] == "V" or map_dict[f"c{i-1}r{r-1}"] == "S" or map_dict[f"c{i-1}r{r-1}"] == "^" or map_dict[f"c{i-1}r{r-1}"] == "H" or map_dict[f"c{i-1}r{r-1}"] == "#" or map_dict[f"c{i-1}r{r-1}"] == "A":
                            print("error 2")
                            temp_list.remove(r)
                            work = False
                            break
                if not r == y:
                    if map_dict[f"c{i}r{r+1}"] == "V" or map_dict[f"c{i}r{r+1}"] == "S" or map_dict[f"c{i}r{r+1}"] == "^" or map_dict[f"c{i}r{r+1}"] == "H" or map_dict[f"c{i}r{r+1}"] == "#" or map_dict[f"c{i}r{r+1}"] == "A":
                        print("error 3")
                        temp_list.remove(r)
                        work = False
                        break
                    if not i == x:
                        if map_dict[f"c{i+1}r{r+1}"] == "V" or map_dict[f"c{i+1}r{r+1}"] == "S" or map_dict[f"c{i+1}r{r+1}"] == "^" or map_dict[f"c{i+1}r{r+1}"] == "H" or map_dict[f"c{i+1}r{r+1}"] == "#" or map_dict[f"c{i+1}r{r+1}"] == "A":
                            print("error 3")
                            temp_list.remove(r)
                            work = False
                            break
                    if not i == 1:
                        if map_dict[f"c{i-1}r{r+1}"] == "V" or map_dict[f"c{i-1}r{r+1}"] == "S" or map_dict[f"c{i-1}r{r+1}"] == "^" or map_dict[f"c{i-1}r{r+1}"] == "H" or map_dict[f"c{i-1}r{r+1}"] == "#" or map_dict[f"c{i-1}r{r+1}"] == "A":
                            print("error 3")
                            temp_list.remove(r)
                            work = False
                            break
                work = False
                finish = False
                snake_place = True
        if snake_place:
            ccrr = map_dict[f"c{c}r{r}"]
            print(f"head at {c, r} with value {map_dict[f"c{c}r{r}"]}")
            map_dict[f"c{c}r{r}"] = "V"
        # body
        r2 = r - 1
        while work2 and n < 100:
            if c == 1:
                choice = random.randint(2,3)
            elif c == x:
                choice = random.randint(1,2)
            else:
                choice = random.randint(1,3)
            if choice == 1:
                c2 = c - 1
            elif choice == 2:
                c2 = c
            elif choice == 3:
                c2 = c + 1
            if map_dict[f"c{c2}r{r2}"] == "V" or map_dict[f"c{c2}r{r2}"] == "S" or map_dict[f"c{c2}r{r2}"] == "^" or map_dict[f"c{c2}r{r2}"] == "H" or map_dict[f"c{c2}r{r2}"] == "#" or map_dict[f"c{c2}r{r2}"] == "A":
                print("retry 2")
                n += 1
                continue
            work2 = False
        if not snake_limit and snake_place:
            cc2rr2 = map_dict[f"c{c2}r{r2}"]
            map_dict[f"c{c2}r{r2}"] = "S"
            print(f"body at {c2,r2}")
        # tail
        r3 = r2 - 1
        while work3 and n < 100:
            if c2 == 1:
                choice2 = random.randint(2,3)
            elif c2 == x:
                choice2 = random.randint(1,2)
            else:
                choice2 = random.randint(1,3)
            if choice2 == 1:
                c3 = c2 - 1
            elif choice2 == 2:
                c3 = c2
            elif choice2 == 3:
                c3 = c2 + 1
            if map_dict[f"c{c3}r{r3}"] == "V" or map_dict[f"c{c3}r{r3}"] == "S" or map_dict[f"c{c3}r{r3}"] == "^" or map_dict[f"c{c3}r{r3}"] == "H" or map_dict[f"c{c3}r{r3}"] == "#" or map_dict[f"c{c3}r{r3}"] == "A":
                print("retry 3")
                n += 1
                continue
            work3 = False
        if not snake_limit and snake_place:
            cc3rr3 = map_dict[f"c{c3}r{r3}"]
            map_dict[f"c{c3}r{r3}"] = "^"
            print(f"tail at {c3, r3}")
        if not snake_limit and snake_place:
            snakes_ladders[f"snake_head{_}"] = f"c{c}r{r}"
            snakes_ladders[f"snake_tail{_}"] = f"c{c3}r{r3}"
        if n >= 100:
            if snake_place:
                map_dict[f"c{c}r{r}"] = ccrr
            if snake_place and not snake_limit:
                map_dict[f"c{c2}r{r2}"] = cc2rr2
            if snake_place and not snake_limit:
                map_dict[f"c{c3}r{r3}"] = cc3rr3
            print("snake disbanded")
    return map_dict,snakes_ladders


def create_ladder(snakes_ladders,map_dict,board,x,y):
    snakes = 0
    ladders = 0
    snake_limit = False
    if y < 3 and x < 3:
        snakes = 0
        ladders = 0
    elif y <= 5 and x <= 5:
        snakes = random.randint(1,2)
        ladders = 1
    elif y <= 10 and x <= 10:
        snakes = random.randint(2,3)
        ladders = 2
    elif y > 10 and x > 10:
        snakes = random.randint(3,6)
        ladders = 3

    for _ in range(ladders):
        # head ladder generation
        n = 0
        snake_place = False
        temp_list = []
        for temp in range(4,y):
            temp_list.append(temp)
        finish = True
        work3 = True
        work2 = True
        while finish:
            if snake_limit:
                break
            work = True
            if temp_list == []:
                break
            else:
                r = random.choice(temp_list)
            c = random.randint(1,x)
            i = c
            # check for duplicates in same row
            print("ladder retry")
            while work:
                if temp_list == []:
                    work = False
                    finish = False
                    snake_limit = True
                    #temp_list_limit = True
                    break
                if map_dict[f"c{i}r{r}"] == map_dict[f"c{x}r{y}"]:
                    print("ladder error 0")
                    temp_list.remove(r)
                    work = False
                    break
                if map_dict[f"c{i}r{r}"] == "V" or map_dict[f"c{i}r{r}"] == "S" or map_dict[f"c{i}r{r}"] == "^" or map_dict[f"c{i}r{r}"] == "H" or map_dict[f"c{i}r{r}"] == "#" or map_dict[f"c{i}r{r}"] == "A":
                    print("laddererror")
                    temp_list.remove(r)
                    work = False
                    break
                if not i == x:
                    if map_dict[f"c{i+1}r{r}"] == "V" or map_dict[f"c{i+1}r{r}"] == "S" or map_dict[f"c{i+1}r{r}"] == "^" or map_dict[f"c{i+1}r{r}"] == "H" or map_dict[f"c{i+1}r{r}"] == "#" or map_dict[f"c{i+1}r{r}"] == "A":
                        print("ladder error")
                        temp_list.remove(r)
                        work = False
                        break
                if not i == 1:
                    if map_dict[f"c{i-1}r{r}"] == "V" or map_dict[f"c{i-1}r{r}"] == "S" or map_dict[f"c{i-1}r{r}"] == "^" or map_dict[f"c{i-1}r{r}"] == "H" or map_dict[f"c{i-1}r{r}"] == "#" or map_dict[f"c{i-1}r{r}"] == "A":
                        print("ladder error")
                        temp_list.remove(r)
                        work = False
                        break
                if  not r == 1:
                    if map_dict[f"c{i}r{r-1}"] == "V" or map_dict[f"c{i}r{r-1}"] == "S" or map_dict[f"c{i}r{r-1}"] == "^" or map_dict[f"c{i}r{r-1}"] == "H" or map_dict[f"c{i}r{r-1}"] == "#" or map_dict[f"c{i}r{r-1}"] == "A":
                        print("ladder error 2")
                        temp_list.remove(r)
                        work = False
                        break
                    if not i == x:
                        if map_dict[f"c{i+1}r{r-1}"] == "V" or map_dict[f"c{i+1}r{r-1}"] == "S" or map_dict[f"c{i+1}r{r-1}"] == "^" or map_dict[f"c{i+1}r{r-1}"] == "H" or map_dict[f"c{i+1}r{r-1}"] == "#" or map_dict[f"c{i+1}r{r-1}"] == "A":
                            print("ladder error 2")
                            temp_list.remove(r)
                            work = False
                            break
                    if not i == 1:
                        if map_dict[f"c{i-1}r{r-1}"] == "V" or map_dict[f"c{i-1}r{r-1}"] == "S" or map_dict[f"c{i-1}r{r-1}"] == "^" or map_dict[f"c{i-1}r{r-1}"] == "H" or map_dict[f"c{i-1}r{r-1}"] == "#" or map_dict[f"c{i-1}r{r-1}"] == "A":
                            print("ladder error 2")
                            temp_list.remove(r)
                            work = False
                            break
                if not r == y:
                    if map_dict[f"c{i}r{r+1}"] == "V" or map_dict[f"c{i}r{r+1}"] == "S" or map_dict[f"c{i}r{r+1}"] == "^" or map_dict[f"c{i}r{r+1}"] == "H" or map_dict[f"c{i}r{r+1}"] == "#" or map_dict[f"c{i}r{r+1}"] == "A":
                        print("ladder error 3")
                        temp_list.remove(r)
                        work = False
                        break
                    if not i == x:
                        if map_dict[f"c{i+1}r{r+1}"] == "V" or map_dict[f"c{i+1}r{r+1}"] == "S" or map_dict[f"c{i+1}r{r+1}"] == "^" or map_dict[f"c{i+1}r{r+1}"] == "H" or map_dict[f"c{i+1}r{r+1}"] == "#" or map_dict[f"c{i+1}r{r+1}"] == "A":
                            print("ladder error 3")
                            temp_list.remove(r)
                            work = False
                            break
                    if not i == 1:
                        if map_dict[f"c{i-1}r{r+1}"] == "V" or map_dict[f"c{i-1}r{r+1}"] == "S" or map_dict[f"c{i-1}r{r+1}"] == "^" or map_dict[f"c{i-1}r{r+1}"] == "H" or map_dict[f"c{i-1}r{r+1}"] == "#" or map_dict[f"c{i-1}r{r+1}"] == "A":
                            print("ladder error 3")
                            temp_list.remove(r)
                            work = False
                            break
                work = False
                finish = False
                snake_place = True
        if snake_place:
            lccrr = map_dict[f"c{c}r{r}"]
            print(f"ladder head at {c, r} with value {map_dict[f"c{c}r{r}"]}")
            map_dict[f"c{c}r{r}"] = "A"
        # body
        r2 = r - 1
        while work2 and n < 100:
            if c == 1:
                choice = random.randint(2,3)
            elif c == x:
                choice = random.randint(1,2)
            else:
                choice = random.randint(1,3)
            if choice == 1:
                c2 = c - 1
            elif choice == 2:
                c2 = c
            elif choice == 3:
                c2 = c + 1
            if map_dict[f"c{c2}r{r2}"] == "V" or map_dict[f"c{c2}r{r2}"] == "S" or map_dict[f"c{c2}r{r2}"] == "^" or map_dict[f"c{c2}r{r2}"] == "H" or map_dict[f"c{c2}r{r2}"] == "#" or map_dict[f"c{c2}r{r2}"] == "A":
                print("ladder retry 2")
                n += 1
                continue
            work2 = False
        if not snake_limit and snake_place:
            lcc2rr2 = map_dict[f"c{c2}r{r2}"]
            map_dict[f"c{c2}r{r2}"] = "#"
            print(f"ladder body at {c2,r2}")
        # tail
        r3 = r2 - 1
        while work3 and n < 100:
            if c2 == 1:
                choice2 = random.randint(2,3)
            elif c2 == x:
                choice2 = random.randint(1,2)
            else:
                choice2 = random.randint(1,3)
            if choice2 == 1:
                c3 = c2 - 1
            elif choice2 == 2:
                c3 = c2
            elif choice2 == 3:
                c3 = c2 + 1
            if map_dict[f"c{c3}r{r3}"] == "V" or map_dict[f"c{c3}r{r3}"] == "S" or map_dict[f"c{c3}r{r3}"] == "^" or map_dict[f"c{c3}r{r3}"] == "H" or map_dict[f"c{c3}r{r3}"] == "#" or map_dict[f"c{c3}r{r3}"] == "A":
                print("ladder retry 3")
                n += 1
                continue
            work3 = False
        if not snake_limit and snake_place:
            lcc3rr3 = map_dict[f"c{c3}r{r3}"]
            map_dict[f"c{c3}r{r3}"] = "H"
            print(f"ladder tail at {c3,r3}")
        if not snake_limit and snake_place:
            snakes_ladders[f"ladder_head{_}"] = f"c{c}r{r}"
            snakes_ladders[f"ladder_tail{_}"] = f"c{c3}r{r3}"
        if n >= 100:
            if snake_place:
                map_dict[f"c{c}r{r}"] = lccrr
            if snake_place and not snake_limit:
                map_dict[f"c{c2}r{r2}"] = lcc2rr2
            if snake_place and not snake_limit:
                map_dict[f"c{c3}r{r3}"] = lcc3rr3
            print("ladder disbanded")
    return map_dict,snakes_ladders

def create_player(player,cpu,x,y):
    # creates a dict of players and cpus
    player_dict = {}
    if player and cpu:
        n = 1
        # first add players, then add cpus
        for i in range(1,player+1):
            if not n >= x:
                player_dict["player"+str(i)] = f"c{n}r1"
                n += 1
        for i in range(1,cpu+1):
            if not n >= x:
                player_dict["cpu"+str(i)] = f"c{n}r1"
                n += 1
    elif player:
        n = 1
        for i in range(1,player+1):
            if not n >= x:
                player_dict["player"+str(i)] = f"c{n}r1"
                n += 1
    elif cpu:
        n = 1
        for i in range(1,cpu+1):
            if not n >= x:
                player_dict["cpu"+str(i)] = f"c{n}r1"
                n += 1
    return player_dict

def create_player2(player,cpu,x,y):
    player_list = []
    n = 1
    if player:
        for i in range(1,player+1):
            if not n > x:
                player_list.append("player"+str(i))
                n += 1
    if cpu:
        for i in range(1,cpu+1):
            if not n > x:
                player_list.append("cpu"+str(i))
                n += 1
    return player_list

def parse_coord(coord):
    # gets the numbers from cxry
    # "c10r5" -> (10, 5)
    col_part = coord.split('r')[0]  # "c10"
    col = int(col_part[1:])         # slice from index 1 -> "10"
    row = int(coord.split('r')[1])  # "5"
    return col, row

def calculate_pos(col,row,x,y,dice_roll,map_dict):
    # oh boy, this is like the most complicated function I've wrote so far
    # and boy am I proud of it
    # sure theres some nested if statements but thats half the fun
    # basically it first checks for odd or even rows
    # then based on that information it will either sum or subtract from the col
    # and based on the starting row, the opposite row should go in reverse ( x - new_col )
    not_within_x_range = True
    while not_within_x_range:
        if row % 2 == 0:
            new_col = col - dice_roll
            if 0 < new_col <= x:
                final_col = new_col
                not_within_x_range = False
                break
            if new_col == 0:
                row += 1
                new_col += 1
                final_col = new_col
                not_within_x_range = False
                break
            if new_col < 0:
                #row += 1
                while True:
                    if row % 2 == 0:
                        if 0 <= new_col <= x:
                            if new_col == 0:
                                row += 1
                                final_col = 1
                                not_within_x_range = False
                                break
                            elif new_col > 0:
                                final_col = new_col
                                not_within_x_range = False
                                break
                        else:
                            row += 1
                            new_col = new_col + x
                    else:
                        if 0 <= new_col <= x:
                            if new_col == 0:
                                row += 1
                                final_col = x
                                not_within_x_range = False
                                break
                            elif new_col > 0:
                                final_col = x+1 - new_col
                                not_within_x_range = False
                                break
                        else:
                            row += 1
                            new_col = new_col + x
        else:
            new_col = col + dice_roll
            if 0 < new_col <= x:
                final_col = new_col
                not_within_x_range = False
                break
            elif new_col == x+1:
                row += 1
                final_col = x
                not_within_x_range = False
                break
            elif new_col > x:
                while True:
                    if row % 2 == 0:
                        if 0 <= new_col <= x:
                            if new_col == 0:
                                row += 1
                                final_col = x
                                not_within_x_range = False
                                break
                            elif new_col > 0:
                                final_col = x+1 - new_col
                                not_within_x_range = False
                                break
                        else:
                            row += 1
                            new_col = new_col - x
                    else:
                        if 0 <= new_col <= x:
                            if new_col == 0:
                                row += 1
                                final_col = 1
                                not_within_x_range = False
                                break
                            elif new_col > 0:
                                final_col = new_col
                                not_within_x_range = False
                                break
                        else:
                            row += 1
                            new_col = new_col - x

    if not not_within_x_range:
        if f"c{final_col}r{row}" in map_dict:
            return final_col,row
        else:
            print("Dice rolled out of the map!")
            return None,None



def roll_dice(dice_range,type,max_roll,*args):
    # add presets in game loop
    # presets:
    # d6, normal maps - type normal
    # d20 for huge maps - type normal
    # d3 for smaller maps - type normal
    dice_range1 = None
    if type == "normal_dice":
        dice_range1 = 1
    elif type == "heavy_roll_dice":
        dice_range1 = dice_range * 0.5
        dice_range1 = dice_range1.ceil()
    elif type == "light_roll_dice":
        dice_range1 = 1
        dice_range = dice_range * 0.5
        dice_range = dice_range.floor()
    elif type == "double_dice":
        dice_range1 = 1
        dice_range = 2 * dice_range
    elif type == "custom_dice" and args:
        # must be within dice_range
        custom_num = args[0]
        if isinstance(custom_num,int):
            if custom_num >= dice_range:
                dice_roll = dice_range
            elif custom_num < 0:
                dice_roll = 1
            elif 0 <= custom_num <= dice_range:
                dice_roll = custom_num
    else:
        print("Dice type is wrong.")
    if dice_range and dice_range1 and type and max_roll:
        dice_roll = dice_range
    elif dice_range and dice_range1 and type:
        dice_roll = random.randint(dice_range1,dice_range)
    if dice_roll:
        return dice_roll
    else:
        print("Something went wrong in roll_dice")
        return None

dice_list = ["normal_dice",
             "heavy_roll_dice",
             "light_roll_dice",
             "double_dice",
             "custom_dice",]

def player_placement(map_dict,player_list,turn_0):
    if turn_0:
        col = 1
        row = 1
        last_location = {}
        for p in player_list:
            map_dict[f"c{col}r{row}"] = p
            last_location[p] = f"c{col}r{row}"
            col += 1
        return map_dict,last_location


def player_movement(map_dict,map_dict_org,player,player_list,last_location,final_col,final_row,snakes_ladders):
    # places the player based on next location

    old_pos = last_location[player]
    new_pos = f"c{final_col}r{final_row}"
    #*-------------------SNAKE-------------------*#
    if map_dict[new_pos] == "V":
    #    print("WE ARE IN V")
    #    print("new_pos",new_pos)
        snake_head_num = False
        for i in snakes_ladders:
            #print("i",i)
            #print("snakes_ladders[i]",snakes_ladders[i])
            if i.startswith("snake_head"):
                if new_pos == snakes_ladders[i] and not snake_head_num:
                    snake_head_num = i.replace("snake_head","")
                    #print(snake_head_num)
                    #return map_dict,last_location
        if snake_head_num:
            final_col,final_row = parse_coord(snakes_ladders[f"snake_tail{snake_head_num}"])
            return player_movement(map_dict, map_dict_org, player, player_list, last_location, final_col, final_row, snakes_ladders)
    #*-------------------LADDER-------------------*#
    elif map_dict[new_pos] == "H":
    #    print("WE ARE IN H")
    #    print("new_pos", new_pos)
        ladder_bottom_num = False
        for i in snakes_ladders:
            #print("i", i)
            #print("snakes_ladders[i]", snakes_ladders[i])
            if i.startswith("ladder_tail"):
                if new_pos == snakes_ladders[i] and not ladder_bottom_num:
                    ladder_bottom_num = i.replace("ladder_tail", "")
                    #print(ladder_bottom_num)
                    # return map_dict,last_location
        if ladder_bottom_num:
            final_col, final_row = parse_coord(snakes_ladders[f"ladder_head{ladder_bottom_num}"])
            return player_movement(map_dict, map_dict_org, player, player_list, last_location, final_col, final_row,snakes_ladders)
    #*-------------------PLAYER-------------------*#
    elif map_dict[new_pos] in player_list:
        # if map is full there will be bugs - fixed
        n = 0
        trying = True
        dead_player = map_dict[new_pos]
        for i in range(1,x+1):
            if f"c{i}r1" in player_list and trying:
                n += 1
            elif not f"c{i}r1" in player_list and trying:
                empty_space = i
                new_dead_player = f"c{empty_space}r1"
                trying = False
        if n == x:
            empty_space = old_pos
        if empty_space:
            map_dict[dead_player] = map_dict_org[last_location[dead_player]]
            map_dict[new_dead_player] = dead_player
            last_location[dead_player] = new_dead_player
            map_dict[new_pos] = player
            last_location[player] = new_pos
            return map_dict,last_location
    else:
        #*-------------------NORMAL-------------------*#
        #print(map_dict[old_pos])
        map_dict[old_pos] = map_dict_org[old_pos]
        #print(map_dict[old_pos])
        #print(map_dict_org[old_pos])
        map_dict[new_pos] = player
        last_location[player] = new_pos
        return map_dict,last_location

def turn_order(player_list,player_turn,dice_range,dice_list,x,y):
    action_list = ["1","2","3"]
    action = False
    turn_amount = 1
    player_amount = len(player_list)
    if player_turn > player_amount:
        player_turn = 0
    if turn_amount: # unnecessary
        while not action:
            print(" 1 ) Roll dice ")
            print(" 2 ) Use items ")
            print(" 3 ) forfeit turn ")
            action = input("What will you do ? ")
            if action in action_list:
                pass
            else:
                print("wrong input, try again.")
                action = False
    if action == str(1):
        dice = False
        while not dice:
            n = 1
            print("Choose one of the following options.")
            for i in dice_list:
                print(f"{n} ) {i}")
                n += 1
            dice = input()
            try:
                dice = int(dice)
            except TypeError:
                print("Wrong, choose again!")
                dice = False
            if dice in range(1,len(dice_list)+1):
                pass
            else:
                print("Wrong,choose again!")
                dice = False


        turn_amount -= 1
        dice_roll = roll_dice(dice_range,dice_list[dice],False)
        max_roll = roll_dice(dice_range,dice_list[dice],True)
        if dice_roll == max_roll:
            turn_amount += 1
    elif action == str(2):
        turn_amount -= 1
        pass
    elif action == str(3):
        turn_amount -= 1
        pass
    if turn_amount > 0:
        return turn_order(player_list,player_turn,dice_range,dice_list,x,y)
    player_turn += 1
    return player_turn



# HOW TO SETUP :
#   map_create ( map_dict )
#   create_board ( map_dict )
#   display_board
#   map_dict,snakes_ladders = create_snake(snakes_ladders,map_dict,board,x,y)
#   map_dict_org = map_dict.copy()


map_dict = map_create(map_dict,x,y)

#print(map_dict)

create_board(map_dict,board,x,y)
display_board(board,x,y)
map_dict,snakes_ladders = create_snake(snakes_ladders, map_dict, board, x, y)
map_dict,snakes_ladders = create_ladder(snakes_ladders,map_dict,board,x,y)
map_dict_org = map_dict.copy()
print(snakes_ladders)

board= []
create_board(map_dict,board,x,y)
display_board(board,x,y)

player_list = create_player2(2,2,x,y)
map_dict,last_location = player_placement(map_dict,player_list,True)

board = []
create_board(map_dict, board, x, y)
display_board(board,x,y)

final_col,final_row = calculate_pos(1,1,x,y,30,map_dict)
player_movement(map_dict,map_dict_org,"player1",player_list,last_location, final_col, final_row, snakes_ladders)

board = []
create_board(map_dict, board, x, y)
display_board(board,x,y)
