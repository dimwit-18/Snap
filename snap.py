# Snap game using tkinter module
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL
import random

def next_shape():    
    global shape
    global curr_col     
    global prev_col
    prev_col = curr_col
    c.delete(shape) # delete current shape
    if len(shapes) > 0: # get the next shape
        shape = shapes.pop()
        c.itemconfigure(shape, state=NORMAL) # display that new shape
        curr_col= c.itemcget(shape, 'fill') # assign it curr_col (current color)
        root.after(1000, next_shape) # wait a second for displaying the next shape
    else:
        # game over, don't respond to the snaps and print the winner or declare draw
        c.unbind('q') 
        c.unbind('p')
        if p1_score > p2_score:
            c.create_text(200, 200, text='Winner: Player 1')
        elif p2_score > p1_score:
            c.create_text(200, 200, text='Winner: Player 2')
        else:
            c.create_text(200, 200, text='Draw')
        c.pack()

def snap(event):    
    global shape    
    global p1_score    
    global p2_score    
    valid = False    
    c.delete(shape)    
    if prev_col == curr_col: # check if point is to be awarded
        valid = True    
    if valid:   # if correct, add 1 to the score and inform the player
        if event.char == 'q':
            p1_score = p1_score + 1
        else:
            p2_score = p2_score + 1
        shape = c.create_text(200, 200, text='SNAP! You score 1 point!')
    else:       # if wrong subtract 1 from the score and inform the player
        if event.char == 'q':
            p1_score = p1_score - 1
        else:
            p2_score = p2_score - 1
        shape = c.create_text(200, 200, text='WRONG! You lose 1 point!')    
    c.pack()    
    root.update_idletasks()    
    time.sleep(1)

# main function
if __name__ == '__main__':

    # Setup GUI, app name ans canvas
    root = Tk() 
    root.title('Snap Game')
    c = Canvas(root, width=400, height=400)
    shapes = []
    # add some colored circles to the shapes list
    circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
    shapes.append(circle)
    circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
    shapes.append(circle)
    circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
    shapes.append(circle)
    circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
    shapes.append(circle)
    # add some colored rectangles to the shapes list
    rectangle = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
    shapes.append(rectangle)
    rectangle = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
    shapes.append(rectangle)
    rectangle = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
    shapes.append(rectangle)
    rectangle = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
    shapes.append(rectangle)
    # add some colored squares to the shapes list
    shapes.append(rectangle)
    square = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
    shapes.append(square)
    square = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
    shapes.append(square)
    square = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
    shapes.append(square)
    square = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
    shapes.append(square)
    c.pack()
    # randomly shuffle the shapes
    random.shuffle(shapes)
    # variables to keep track of current shape, color and previous color and scores of the players
    shape = None
    p1_score = 0
    p2_score = 0
    prev_col = ''
    curr_col= ''
    root.after(3000, next_shape) # delay for the appearance of first shape
    # bind Q and P keys with player 1 and player 2
    c.bind('q', snap)
    c.bind('p', snap)
    c.focus_set() 
    root.mainloop() # next shape is displayed in the GUI

