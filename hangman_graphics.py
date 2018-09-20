from random import choice
from graphics import *

# list of all possible words
word_list = open("words").readlines()
    
def new_game(word_list):
    playing = True
    
    # list of body parts in order of appearance
    body = []
    # head
    body.append(Circle(Point(400, 200), 50))
    # torso
    body.append(Line(Point(400, 250), Point(400, 375)))
    # arms (left and right)
    body.append(Line(Point(335, 300), Point(400, 300)))
    body.append(Line(Point(400, 300), Point(465, 300)))
    # legs (left and right)
    body.append(Line(Point(400, 375), Point(335, 450)))
    body.append(Line(Point(400, 375), Point(465, 450)))
    # eyes
    body.append([Line(Point(365, 175), Point(390, 200)), Line(Point(365, 200), Point(390, 175))])
    body.append([Line(Point(410, 175), Point(435, 200)), Line(Point(410, 200), Point(435, 175))])
    # mouth
    body.append(Circle(Point(400, 225), 10))
    
    # opens window
    win = GraphWin('Hangman', 800, 650, autoflush = False)
    
    # while player wants to play
    while playing:
        # sets up graphics for beginning of game
        begin_graph(win)
        word = choice(word_list).upper()
    
        # establishes word randomly
        # extra space at the end for some reason so i'm splicing it out
        word = word[0:len(word) - 1]
        # uses dictionary to keep track of letters in word and where they appear
        # think faux hash table
        in_word = {}
        for i in range (0, len(word)):
            char = word[i]
            if not char in in_word:
                in_word[char] = []
            in_word[char].append(i)
        
        # blank spaces displayed to player
        display = []
        for i in range(0, len(word)):
            display.append("_")
        label = Text(Point(400, 50), " ".join(display))
        label.setSize(36)
        label.draw(win)
    
        lets_left = len(word)
        fails = 0
        guessed = [];
        
        # while player still has chances and hasn't solved
        while lets_left > 0 and fails < len(body):
            click = win.getMouse()
            # col and row of letter on screen
            col = (int) (click.getX() / 61.5)
            row = (int) ((click.getY() - 525) / 50)
            while (col < 0 or col > 13 or row < 0 or row > 1):
                click = win.getMouse()
                col = (int) (click.getX() / 61.5)
                row = (int) ((click.getY() - 525) / 50)
            let_ind = col + (13 * row)
            letter = chr(65 + let_ind)
            # line crossing out letter
            cross_out = Line(Point(col * 61.5, 575 + (50 * row)), Point((col + 1) * 61.5, 525 + (50 * row)))
            cross_out.setFill("red")
            cross_out.setWidth(3)
            cross_out.draw(win)
            # checks guess. draws body part if incorrect, fills in blanks if correct
            if (letter not in in_word) and (letter not in guessed):
                draw_body(fails, body, win)
                fails += 1
                guessed.append(letter)
            else:
                # checks if letter has already been guessed
                if letter in guessed:
                    continue
                # changes letters in display and marks letter as guessed
                for ind in in_word[letter]:
                    display[ind] = letter
                    lets_left -= 1
                    guessed.append(letter)
                label.setText(" ".join(display))
                
        # congrats or loss message    
        if lets_left == 0:
            won = Text(Point(185, 125), "Congrats, you won!")
            won.setSize(36)
            won.setFill(color_rgb(31, 122, 33))
            won.draw(win)
        else:
            lost1 = Text(Point(175, 125), "Sorry, you lost!")
            lost2 = Text(Point(175, 175), word)
            lost1.setSize(36)
            lost2.setSize(36)
            lost1.setFill(color_rgb(137, 8, 16))
            lost2.setFill(color_rgb(137, 8, 16))
            lost1.draw(win)
            lost2.draw(win)
            
        # asks to play again  
        play_again = Text(Point(175, 300), "Play again?")
        play_again.setSize(36)
        yes = Text(Point(140, 350), "Y")
        yes.setSize(36)
        no = Text(Point(210, 350), "N")
        no.setSize(36)
        play_again.draw(win)
        yes.draw(win)
        no.draw(win)
        win.update()
        
        # registers mouse click
        click = win.getMouse()
        while (click.getX() < 105 or click.getX() > 245 or click.getY()< 325 or click.getY() > 375):
            click = win.getMouse()
        if (click.getX() < 175):
            clear_screen(win)
        else:
            playing = False
    
    # closes drawing window
    win.close()
    
# draws body part
def draw_body(index, body, win):
    if type(body[index]) == list:
        for i in body[index]:
            i.setWidth(3)
            i.draw(win)
    else:
        body[index].setWidth(3)
        body[index].draw(win)
        
    win.update()

# draws initial graphics
def begin_graph(win):
    # noose
    gallow1 = Line(Point(400, 100), Point(400, 150))
    gallow1.setWidth(3)
    gallow1.setFill("gray")
    # vertical gallow
    gallow2 = Line(Point(600, 100), Point(600, 500))
    gallow2.setWidth(10)
    gallow2.setFill(color_rgb(76,45,45))
    # bottom line
    gallow3 = Line(Point(550, 500), Point(650, 500))
    gallow3.setWidth(10)
    gallow3.setFill(color_rgb(76, 45, 45))
    # top line
    gallow4 = Line(Point(399, 100), Point(605, 100))
    gallow4.setWidth(10)
    gallow4.setFill(color_rgb(76, 45, 45))
    gallow1.draw(win)
    gallow2.draw(win)
    gallow3.draw(win)
    gallow4.draw(win)
    
    # alphabet
    x_jump = 61.5
    for i in range(0, 26):
        letter = Text(Point(30.75 + (x_jump * (i % 13)), 550 + (50 * (int)(i / 13))), chr(65 + i))
        letter.setSize(30)
        letter.draw(win)
        
    win.update()

# clears screen
def clear_screen(win):
    for i in win.items[:]:
        i.undraw()
    win.update()
    
new_game(word_list)