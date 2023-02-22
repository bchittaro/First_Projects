import pygame, time, random, os

pygame.init()
wwid=1000
whgt=600
win=pygame.display.set_mode((wwid,whgt))
clock=pygame.time.Clock()
pygame.display.set_caption('Note generator')

#Notes
Note8=pygame.image.load(os.path.join("Notes_Media","8thNote.png"))
Note16=pygame.image.load(os.path.join("Notes_Media","16thNote.png"))
NoteQuarter=pygame.image.load(os.path.join("Notes_Media","QuarterNote.png"))
NoteHalf=pygame.image.load(os.path.join("Notes_Media","HalfNote.png"))
Double8=pygame.image.load(os.path.join("Notes_Media","Double8th.png"))
Double16=pygame.image.load(os.path.join("Notes_Media","Double16th.png"))
Double816=pygame.image.load(os.path.join("Notes_Media","Double8th16th.png"))

#Other
RestQuarter=pygame.image.load(os.path.join("Notes_Media","QuarterRest.png"))
Rest8=pygame.image.load(os.path.join("Notes_Media","8thRest.png"))
Sharp=pygame.image.load(os.path.join("Notes_Media","Sharp.png"))
Flat=pygame.image.load(os.path.join("Notes_Media","Flat.png"))

AllNotes=[NoteHalf,NoteQuarter,RestQuarter,Double8,Double816,Note8,Rest8,Double16,Note16]
Rests=[Rest8,RestQuarter]
length=len(AllNotes)-1

FinalNotes=[]
FinalPos=[0]
BarSpace=16
start=0
Full=False

def ListCorrect(value):
    global FinalPos,BarSpace,start,Full
    BarSpace-=value
    previous=FinalPos[len(FinalPos)-1]
    FinalPos.append(value+previous)

    if BarSpace==0:
        Full=True
    elif BarSpace<2:
        start=8
    elif BarSpace<4:
        start=5
    elif BarSpace<8:
        start=1
    

def NoteValue(selection):
    if selection==0:
        ListCorrect(8)
    elif selection<=4:
        ListCorrect(4)
    elif selection<=7:
        ListCorrect(2)
    elif selection==8:
        ListCorrect(1)
        
    
run=True

while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        
    if Full==True:
        for i in range(len(FinalNotes)):
            Xpos=(FinalPos[i]*50)+100
            ##KEY OPTION:
            NoteRect=FinalNotes[i].get_rect().size
            if FinalNotes[i] in Rests:
                Ypos=300-(NoteRect[1]/2)
            else:
                Ypos=175+((random.randint(1,11)*25)-(NoteRect[1]+10))
            
            win.blit(FinalNotes[i],(round(Xpos),round(Ypos)))

        pygame.display.update()

        time.sleep(2)
        Full=False
        FinalNotes=[]
        FinalPos=[0]
        BarSpace=16
        start=0

    if Full==False:
        pick=random.randint(start,length)
        FinalNotes.append(AllNotes[pick])
        NoteValue(pick)
        

    win.fill((255,255,255))
    pygame.draw.line(win,(0,0,0,),(70,200),(900,200))
    pygame.draw.line(win,(0,0,0,),(70,250),(900,250))
    pygame.draw.line(win,(0,0,0,),(70,300),(900,300))
    pygame.draw.line(win,(0,0,0,),(70,350),(900,350))
    pygame.draw.line(win,(0,0,0,),(70,400),(900,400))
    pygame.draw.rect(win,(0,0,0),(20,200,50,201))
#800/16 = 50 --- 100, 150, 200...850
#Key spots = (25 dist * 11) - 175, 200...425


    
    pygame.display.update()
    clock.tick(20)

pygame.quit()
