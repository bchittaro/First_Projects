import pygame
import time

pygame.init()
wwid=700
whgt=500
win=pygame.display.set_mode((wwid,whgt))
clock=pygame.time.Clock()

def Reset():
    global checkpress, animation, fallY, prevLetters, finalLetter
    checkpress = True
    animation = False
    animInit = False
    prevLetters = []
    finalLetter = []
    fallY = 0
    win.fill((0,0,0))

Reset()

txtY = 230
txtSize = 50
text_width = 0


letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
           "q","r","s","t","u","v","w","x","y","z"," ","0","1","2","3","4",
           "5","6","7","8","9"]
keyInput = [pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,
            pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,
            pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,
            pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,
            pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,
            pygame.K_z,pygame.K_SPACE,pygame.K_0,pygame.K_1,
            pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,
            pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]


def Textify():
    global prevLetters, text_width
    text=''
    for i in range(len(prevLetters)):
        text+=prevLetters[i]
    if len(prevLetters)>0:
        initTxt=font.render(text,1,(255,255,255))
        text_width = initTxt.get_width()
        ##manual size change
        x = (wwid/2)-(text_width/2)
        win.blit(initTxt,(round(x),txtY))
    else:
        text_width = 0

def getLetters():
    global letters,finalLetter,prevLetters,keyInput, animInit
    initLen=len(prevLetters)
    lettercheck = finalLetter
    for i in range(len(letters)):
        if keys[(keyInput[i])]:
            if len(finalLetter)>0:
                prevLetters.append(finalLetter[0])
            finalLetter=[letters[i]]
    finalLen=len(prevLetters)
    if initLen<finalLen or lettercheck!=finalLetter:
        animInit=True
    else:
        animInit=False
    if keys[pygame.K_BACKSPACE] and len(finalLetter)>0:
        wordLen = len(prevLetters)-1
        finalLetter.clear()
        finalLetter.append(prevLetters[wordLen])
        prevLetters.pop(wordLen)
        

def animateLetter():
    global finalLetter, text_width, fallY, animation
    Textify()
    initTxt=font.render(finalLetter[0],1,(255,255,255))
    fallY+=10
    x = (wwid/2)+(text_width/2)
    win.blit(initTxt,(round(x),fallY))
    if fallY>=230:
        animation=False
        fallY=230
        win.blit(initTxt,(round(x),fallY))
        fallY=0

def keyEvent():
    global checkpress, animInit, animation
    checkpress=False
    getLetters()
    if animInit:
        animation=True


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    win.fill((0,0,0))

    keys=pygame.key.get_pressed()

    if checkpress:
        ##enter key -- clear all
        if keys[pygame.K_RETURN]:
            Reset()
            pygame.display.update()


        ##any other keypress        
        elif event.type==pygame.KEYDOWN:
            keyEvent()
#            print("final letter = ",finalLetter)
#            print("prev letter = ",prevLetters)
            
    elif event.type==pygame.KEYUP:
        checkpress=True

    if animation:
        animateLetter()
        pygame.display.update()
    



        
    clock.tick(50)

pygame.quit()
