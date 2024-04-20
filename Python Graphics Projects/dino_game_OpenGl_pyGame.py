import pygame
from pygame.locals import *
from OpenGL.GL import *
import turtle


# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 300
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
glOrtho(0, width, height, 0, -1, 1) #sets prespective

# Ground level
ground_level = height - 30 #ground level determined by display

# Dino properties
dino_x = 50
dino_width = 30
dino_height = 30
dino_jump_velocity = 10  # postive so it jumps up
dino_gravity = 0.5 #gravity is gonna be subtracted so it goes down
dino_velocity = 0 #vertical velocity
jumping = False
dino_y = ground_level - dino_height  # Initial y-coordinate

# Obstacle properties
obstacle_width = 20
obstacle_height = 20
obstacle_x = width
obstacle_speed = 5

# Score
score = 0 #U CAN ADD A DRAW SCORE FUNCTION HERE ,MAYBE MAKE IT CHANGE COLOR FOR EACH SCORE

# Function to draw the dinosaur
def draw_dino(): #glvertex2f auto sets z axis to zero
    glColor3f(1, 1, 1)#gives colors to next vertexes
    glBegin(GL_QUADS) #OpenGL's GL_QUADS primitive draws a four- sided polygon ,
    # glbegin Draws a connected group of line segments from the first vertex to the last, then back to the first
    glVertex2f(dino_x, dino_y)
    glVertex2f(dino_x + dino_width, dino_y)
    glVertex2f(dino_x + dino_width, dino_y + dino_height)
    glVertex2f(dino_x, dino_y + dino_height)
    glEnd()

# Function to draw the ground
def draw_ground():
    glColor3f(0, 1, 0) #U CAN CHANGE THE COLORS HERE OR ADD TEXTURES
    glBegin(GL_QUADS)
    glVertex2f(0, ground_level)
    glVertex2f(width, ground_level)
    glVertex2f(width, height)
    glVertex2f(0, height)
    glEnd()

# Function to draw obstacles
def draw_obstacle(x):
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(x, ground_level - obstacle_height)
    glVertex2f(x + obstacle_width, ground_level - obstacle_height)
    glVertex2f(x + obstacle_width, ground_level)
    glVertex2f(x, ground_level)
    glEnd()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #on key press space, and the dino isnt already jumping or falling>>dino_y==ground_level-dinoheight
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping and dino_y == ground_level - dino_height:
            dino_velocity = dino_jump_velocity  # change the dion velocity(vertical velo) to its jump 'velocity'
            jumping = True #set state jumping to True

    # Update dino position
    if jumping or (dino_velocity < 0 and dino_y > 0): #if we are jumping or have vertical velo or falling(dino_y>0)
        dino_velocity -= dino_gravity #our vertical velocity is  negative to imitate gravity
        #ADD HERE ROTATION TO DINO ONLY IDK HOW


    dino_y = max(0, min(ground_level - dino_height, dino_y - dino_velocity))#our y pos is determined by this equation
#the lower bound of either the ground_level-dinoheight or dino_y pos - its velocity as in going up or down
    # Check if the dino has landed
    if dino_y >= ground_level - dino_height and jumping: #check if we are on ground if not jumping is false
        jumping = False

    # Update obstacle position
    obstacle_x -= obstacle_speed #we change it x axis determined by its speed , sub because we goin right to left
    if obstacle_x < 0:
        obstacle_x = width
        score += 1
    obstacle_speed += 0.0009 * score #increase speed as score increases

    # Check for collision with obstacles
    if (
        dino_x < obstacle_x + obstacle_width # IF DINO SQUARE SHAPE IS IN CONCTACT WITH AN OBSTACLE X AXIS
        and dino_x + dino_width > obstacle_x
        and dino_y < ground_level - obstacle_height#SAME BUT FOR HEIHGT
        and dino_y + dino_height > ground_level - obstacle_height #if dino shape height in its y pos in no contact
    ):#if one if these is not true then
        print("Game Over. Score:", score)

        # Turtle Game Over Screen
        turtle.screensize(600, 300, "black")
        turtle.speed(2)

        turtle.penup()
        turtle.goto(0, 50)
        turtle.color("red")
        turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
        turtle.goto(0, 20)
        turtle.write("Score: {}".format(score), align="center", font=("Arial", 18, "normal"))
        turtle.hideturtle()

        turtle.done()

        pygame.quit()
        quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw ground
    draw_ground()

    # Draw dino
    draw_dino()

    # Draw obstacles
    draw_obstacle(obstacle_x)
    #IDK HOW YET BUT MAYBE ADD A COUNTDOWN TIMER
    pygame.display.flip() #updates entire display
    pygame.time.wait(10) #sets delay
