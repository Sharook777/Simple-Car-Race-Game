
import pygame as pyg
import random


pyg.init()

d_width,d_height=300,500
white=(255,255,255)
black=(0,0,0)
colr = (220,220,220)

color=white

#linex,liney,linew,lineh=148,0,4,500

gameDisplay=pyg.display.set_mode((d_width,d_height))

pyg.display.set_caption('Dhoom')
pyg.mouse.set_visible(0)

time=pyg.time.Clock()

#pyg.draw.rect(gameDisplay,color,[linex,liney,linew,lineh])

image = pyg.image.load('hero1.jpg')
image1 = pyg.image.load('ltruck3.jpg')
image2 = pyg.image.load('police1.jpg')
image3 = pyg.image.load('truck1.jpg')
image4 = pyg.image.load('wtruck2.jpg')
image5 = pyg.image.load('bike.jpg')
image6 = pyg.image.load('car2.jpg')
image7 = pyg.image.load('car1.jpg')
image8 = pyg.image.load('car3.jpg')
image9 = pyg.image.load('car4.jpg')
image10 = pyg.image.load('limo.jpg')
image11 = pyg.image.load('police2.jpg')
image12 = pyg.image.load('sbus.jpg')
image13 = pyg.image.load('taxi.jpg')
image14 = pyg.image.load('truck5.jpg')
image15 = pyg.image.load('truck6.jpg')

car_list=[image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,
          image11,image12,image13,image14,image15]


linew1,lineh1 = 4,10
linew2,lineh2 = 11,10

lines = [15,5,-5]
lines2 = [20,15,10,5,0,-5]
#cross_line = (200,200,200)



red = (255,0,0)
def text_objects(text,font,col):
   textSurface = font.render(text,True,col)
   return textSurface,textSurface.get_rect()



def score_card(text2):
   col = (255,0,0)
   font = pyg.font.Font('freesansbold.ttf',20)
   TextSurf2,TextRect2 = text_objects(text2,font,col)
   gameDisplay.blit(TextSurf2,TextRect2)
   pyg.display.update()


def message_display():
   import time
   text = 'YOU CRASHED '
   font = pyg.font.Font('freesansbold.ttf',35)
   
   TextSurf,TextRect = text_objects(text,font,black)
   
   TextRect.center = ((d_width/2),(d_height/2))
   
   gameDisplay.blit(TextSurf,TextRect)
   pyg.display.update()

   time.sleep(2)
   game_loop()



def cross(linex2):
   #print(linex1,linew1,lineh1 )
   
   liney2 = lines2.pop()
   lines2.insert(0,liney2)
   
   #print(liney1,lines)
   #time.tick(80)
   for i in range(29):
      #while True:

         new=pyg.draw.rect(gameDisplay,(100,100,100),[linex2,liney2,linew2,lineh2])
         #print(new)
         liney2 += 20
         #pyg.display.flip()
         if liney2 > 600:
            liney2 = 0
            #linex1 = 275
         
         #clock.tick(60)

def line(linex1):
   #print(linex1,linew1,lineh1 )
   
   liney1 = lines.pop()
   lines.insert(0,liney1)
   
   #print(liney1,lines)
   time.tick(80)
   for i in range(29):
      #while True:

         new=pyg.draw.rect(gameDisplay,color,[linex1,liney1,linew1,lineh1])
         #print(new)
         liney1 += 20
         #pyg.display.flip()
         if liney1 > 600:
            liney1 = 0
            #linex1 = 275
         
         #clock.tick(60)

def cars(img,x,y):
   gameDisplay.blit(img,(x,y))

def car_move(x,y):
   gameDisplay.blit(image,(x,y))
   #print(x)


def game_loop():
   global crashed,score
   score = 0
   x,y=95,400
   #image=pyg.image.load('hero.jpg')
   crashed=False
   x_change=0

   ways = [25,95,165,235]
   temp = random.sample(ways,3)

   thing_x = temp.pop()
   thing_x2 = temp.pop()
   thing_x3 = temp.pop()
   thing_y = -400
   thing_y1 = -400
   thing_y2 = -400
   thing_speed = 10
   thing_speed1 = 13
   thing_speed2 = 20
   img = random.choice(car_list)
   img2 = random.choice(car_list)
   img3 = random.choice(car_list)

   while not crashed:
      
      for event in pyg.event.get():
         
         
         if event.type==pyg.QUIT:
            pyg.quit()

         if event.type == pyg.KEYDOWN:
            #print(event.type,event.key)
            print(event.key)
            if event.key == pyg.K_LEFT:
               x_change = -70
               if x<70:
                  x_change = 0
                  
            if event.key == pyg.K_RIGHT:
               x_change = 70
               if  x > 220:
                  x_change = 0
               
            x += x_change
               
         if event.type == pyg.KEYUP:
               
            if event.key == pyg.K_RIGHT or event.key == pyg.K_LEFT:
               x_change=0
               
      #print(x)
      
      #if x<=10 or x>=335:
         #x_change = 0
         
      '''if x<70:
         x_change = 0
         
      if  x == 270:
         x_change = -5'''
         
         
      #x += x_change
      #x_change = 0
      
      gameDisplay.fill(colr)
      
      pyg.draw.rect(gameDisplay,color,[148,0,4,500])
      pyg.draw.rect(gameDisplay,color,[9,0,2,500])
      pyg.draw.rect(gameDisplay,color,[289,0,2,500])
      
      #line(150)
      line(78)
      line(218)
      
      cross(0)
      cross(289)
      
      car_move(x,y)
      
      cars(img,thing_x,thing_y)
      cars(img2,thing_x2,thing_y1)
      cars(img3,thing_x3,thing_y2)

      image_rect1 = img.get_rect()
      image_rect2 = img2.get_rect()
      image_rect3 = img3.get_rect()
      
      yy =  image_rect1.height
      yyy =  image_rect2.height
      yyyy =  image_rect3.height

      #print(yy,yyy,yyyy)
      
      if y <= thing_y+yy:
         #print('Y crossess')
         #if x == thing_x and x < thing_x + 40 or x + 40 > thing_x and x + 40 < thing_x + 40:

         if x == thing_x:
            #print('Crashes 1')
            crashed=True

      if y <= thing_y1+yyy:
         if x == thing_x2:
            #print('Crashes 2')
            crashed=True

      if y <= thing_y2+yyyy:
         if x == thing_x3:
            #print('Crashes 3')
            crashed=True

         '''if x == thing_x2 and x < thing_x2 + 40:
            print('Crashes')
            crashed=True

         if x == thing_x3 and x < thing_x3 + 40:
            print('Crashes')
            crashed=True'''
         
      thing_y += thing_speed
      thing_y1 += thing_speed1
      thing_y2 += thing_speed2
      
      if thing_y2 > d_height:
         score += 1
         thing_y2 = -300
         thing_x3 = random.sample(ways,1)
         thing_x3 = thing_x3.pop()
         while (thing_x3 == thing_x2 or thing_x3 == thing_x):
            thing_x3 = random.sample(ways,1)
            thing_x3 = thing_x3.pop()
         img3 = random.choice(car_list)
      
      if thing_y1 > d_height:
         score += 1
         thing_y1 = -300
         thing_x2 = random.sample(ways,1)
         thing_x2 = thing_x2.pop()
         while (thing_x2 == thing_x):
            thing_x2 = random.sample(ways,1)
            thing_x2 = thing_x2.pop()
         img2 = random.choice(car_list)

      if thing_y > d_height:
         score += 1
         thing_y = -300
         #thing_y1 = -300
         thing_x = random.sample(ways,1)
         thing_x = thing_x.pop()
         #thing_x2 = temp.pop() 
         img = random.choice(car_list)
                                    
      #print(score)
      pyg.display.update()
      time.tick(100)
      
      score_card('Score ' + str(score))
      
      if crashed:
         message_display()

      

game_loop()

   
pyg.quit()

