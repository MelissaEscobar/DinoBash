import pygame
import random
from time import sleep

ANCHO=1300
ALTO=700
BLANCO=[255,255,255]

NEGRO=[0,0,0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]

COLOR = [30, 40, 50]



#TODO: hacer que cuando se arrastre el cuadro movil hacia la linea, ella se desplace por la trayectoria de 
#la linea 

# algoritmo Montecarlo para juegos de azar 
#juegos plataforma 


def cortarimg(img,fx,fy):
    # 'fx' es el numero de figuras que hay en el eje x
    # 'fy' es el numero de figuras que hay en el eje y
    #matriz que guarda la posicion de las imagenes ya recortadas
    m=[]
    #guarda la info de la imagen
    info=img.get_rect()
    ancho_img=info[2]   #guardo ancho de la imagen
    alto_img=info[3]    #guarda alto de la imagen

    for s in range(0,fx):
        ls=[]
        for i in range(0,fy):
            ls.append(img.subsurface(s*(ancho_img/fx),i*(alto_img/fy),(ancho_img/fx),(alto_img/fy)))
        m.append(ls)

    return m


class Ogre1(pygame.sprite.Sprite):
    def __init__(self, pos_ini, mat_i , name):
        pygame.sprite.Sprite.__init__(self)
        
        self.x=0 # Da el movimiento segun la direccion en la que se desplaza. Asociada a las columnas
        self.dir=1 # dirección en la que se va a mover, está asociada a las filas de la matriz
        self.m=mat_i #matriz inicial con los sprites recortados
        self.image = self.m[self.x][self.dir] #se settea la imagen inicial
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx=0
        self.vely=0
        self.name = name
        self.click = False
        self.vida = 250

        #velocidad del objeto en x  y en y
        self.velx = 0
        self.vely = 0


    def update(self):

        self.image = self.m[self.x][self.dir]
        self.x+=1

        if self.click==False:
            self.rect.x += self.velx
            self.rect.y += self.vely
        if self.click:
            self.rect.center= pygame.mouse.get_pos()
        if self.x > 6: #Como se trata del dino2, entre las columnas 0 a 4
            if self.dir == 3: #Animacion en la que el monstruo muere
                self.x= 6
                self.velx =0
                self.vely = 0
            elif self.dir ==2: #Animacion en la que el monstruo recibe un golpe 
                self.dir= 1
                self.x = 0
            else:                    
                self.x=0


# Ogre 2

class Ogre2(pygame.sprite.Sprite):
    def __init__(self, pos_ini, mat_i , name):
        pygame.sprite.Sprite.__init__(self)
        
        self.x=0 # Da el movimiento segun la direccion en la que se desplaza. Asociada a las columnas
        self.dir=1 # dirección en la que se va a mover, está asociada a las filas de la matriz
        self.m=mat_i #matriz inicial con los sprites recortados
        self.image = self.m[self.x][self.dir] #se settea la imagen inicial
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx=0
        self.vely=0
        self.name = name
        self.click = False

        #velocidad del objeto en x  y en y
        self.velx = 0
        self.vely = 0
        self.vida= 500


    def update(self):

        self.image = self.m[self.x][self.dir]
        self.x+=1

        if self.click==False:
            self.rect.x += self.velx
            self.rect.y += self.vely
        if self.click:
            self.rect.center= pygame.mouse.get_pos()
        if self.x > 6: #Como se trata del dino2, entre las columnas 0 a 4
            if self.dir == 3: #Animacion en la que el monstruo muere
                self.x= 6
                self.velx =0
                self.vely = 0
            elif self.dir ==2: #Animacion en la que el monstruo recibe un golpe 
                self.dir= 1
                self.x = 0
            else:                    
                self.x=0


class DinoFly(pygame.sprite.Sprite):
    def __init__(self, pos_ini, mat_i , name):
        pygame.sprite.Sprite.__init__(self)
        
        self.x=0 # Da el movimiento segun la direccion en la que se desplaza. Asociada a las columnas
        self.dir=1 # dirección en la que se va a mover, está asociada a las filas de la matriz
        self.m=mat_i #matriz inicial con los sprites recortados
        self.image = self.m[self.x][self.dir] #se settea la imagen inicial
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx=0
        self.vely=0
        self.name = name
        self.click = False

        #velocidad del objeto en x  y en y
        self.velx = 0
        self.vely = 0


    def update(self):

        self.image = self.m[self.x][self.dir]
        self.x+=1

        if self.click==False:
            self.rect.x += self.velx
            self.rect.y += self.vely
        if self.click:
            self.rect.center= pygame.mouse.get_pos()
        if self.x > 8: #Como se trata del dino2, entre las columnas 0 a 4
            self.x=0


class Raptor(pygame.sprite.Sprite):
    def __init__(self, pos_ini, mat_i , name):
        pygame.sprite.Sprite.__init__(self)
        
        self.x=0 # Da el movimiento segun la direccion en la que se desplaza. Asociada a las columnas
        self.dir=0 # dirección en la que se va a mover, está asociada a las filas de la matriz
        self.m=mat_i #matriz inicial con los sprites recortados
        self.image = self.m[self.x][self.dir] #se settea la imagen inicial
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx=0
        self.name = name
        self.click = False

        #velocidad del objeto en x  y en y
        self.velx = 0


    def update(self):

        self.image = self.m[self.x][self.dir]
        self.x+=1

        if self.click==False:
            self.rect.x += self.velx
        if self.click:
            self.rect.center= pygame.mouse.get_pos()
        if self.x > 4: #Como se trata del dino2, entre las columnas 0 a 4
            if self.dir == 0:
                self.dir = 2 # cambia de caminar a correr                 
            
            self.x=0



class Egg(pygame.sprite.Sprite):
    def __init__(self, pos_ini, matrix):
        pygame.sprite.Sprite.__init__(self)
        
        self.x=0 # Da el movimiento segun la direccion en la que se desplaza. Asociada a las columnas
        self.dir=0 # dirección en la que se va a mover, está asociada a las filas de la matriz
        self.m=matrix #matriz inicial con los sprites recortados
        self.image = self.m[self.x][self.dir] #se settea la imagen inicial
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.life = 160
        

    def update(self):

        if self.life == 160:
            self.x = 0
        elif self.life <=120:
            self.x = 1
        elif self.life <= 80:
            self.x = 2
        elif self.life <= 40:
            self.x = 3
        else:
            self.x = 4 #huevo roto 

        self.image = self.m[self.x][self.dir]
            

# class Apple(pygame.sprite.Sprite):
#     def __init__(self, pos_ini,image ):
#         pygame.sprite.Sprite.__init__(self)

#         self.image = image 


class CuadroStatic(pygame.sprite.Sprite):
    def __init__(self, pos_ini,image, name ):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([100, 50])
        self.image = image # Imagen del paquete de dinosaurio
        self.rect = self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]

        self.name = name

        # Al darle click debe generar un objeto de tipo Cuadro normal, que se va a mover y se va a desplazar 
        # hacia la derecha si es rojo y hacia abajo si es verde        
        self.click = False

    def update(self):
        if self.click:
            self.rect.center= pygame.mouse.get_pos()


if __name__ == "__main__":
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    contClock = 0 #contador de los pulsos del reloj
    fin = False
    reloj = pygame.time.Clock()
    nivel = 2

    #carga de la imagen que contiene el letrero del nivel 1

    nivel1Img = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/Nivel1.png')

    #carga de la imagen que contiene el letrero del nivel 2
    nivel2Img = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/Nivel2.png')

    #imagen de la manzana

    apple = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/apple.png')

    #background nivel 1
    fondo = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/background.png')

    #background nivel 2
    fondo2 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/background.png')



    #Dinos boxes 

    dinoBox1 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/cuadro1.png')
    c1= CuadroStatic([900, 50], dinoBox1, "dinoFlyBox1")     

    dinoBox2 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/cuadro2.png')
    c2= CuadroStatic([1100, 50], dinoBox2, "dinoRaptorBox2")     
    cuadros = pygame.sprite.Group()    
    #Agrego al grupoo los cuadros estaticos que estaran al final 
    #de la pantalla
    cuadros.add(c1)
    if nivel ==2:
        cuadros.add(c2)


    #---------------------  Carga de imagenes para el huevo: ----------------------------------
    eImage = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/Egg.png')
    eHuevo = cortarimg(eImage, 5, 1)
    eggg = Egg([1000, 350], eHuevo)
    #Grupo de huevos
    eggs = pygame.sprite.Group()

    eggs.add(eggg)
    vidas = 160 # variable auxiliar para saber cuantas vidas tiene el huevo despues de ser colisionado
    contTouch = 0
    contTouchOgre = 0

    # ---------------- creacion de los enemigos - monstruos -----------------------------------
    ogresGroup = pygame.sprite.Group()

     #IMagen con los sprites Ogro 1
    img=pygame.image.load('/home/melii/Documents/Python/Dinobash/img/orc1.png')# Ogro 1
    m = cortarimg(img,7,5)



     #IMagen con los sprites a recortar ogro 2
    imgOgro2=pygame.image.load('/home/melii/Documents/Python/Dinobash/img/orc2.png')# Ogro 2
    mOgro2 = cortarimg(imgOgro2,7,5)


    # creacion del dino que vuela
    dinoFlyGroup = pygame.sprite.Group()
    d1Ima = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/dino1.png')
    d1 = cortarimg(d1Ima, 9, 2)

    #Creacion del raptor 
    raptorGroup = pygame.sprite.Group()
    d2Ima = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/dino2.png')
    d2 = cortarimg(d2Ima, 7, 3)

    # configurar música

    pygame.mixer.music.load('/home/melii/Documents/Python/Dinobash/music/fondo4.wav')
    pygame.mixer.music.play(-1)

    # pygame.mixer.music.load('/home/melii/Documents/Python/Dinobash/img/pain.wav')
    # pygame.mixer.music.play(0)


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.MOUSEBUTTONDOWN:

                if nivel== 1:
                    if c1.rect.collidepoint(event.pos):
                        newDino = DinoFly(c1.rect, d1 , "fly") 
                        newDino.click = True
                        dinoFlyGroup.add(newDino)

                        
                if nivel == 2:

                    if c1.rect.collidepoint(event.pos):
                        newDino = DinoFly(c1.rect, d1 , "fly") 
                        newDino.click = True
                        dinoFlyGroup.add(newDino)
                        
                    if c2.rect.collidepoint(event.pos): #c1 es el cuadro verde
                        newDino = Raptor(c2.rect, d2 , "raptor")
                        newDino.click = True
                        raptorGroup.add(newDino)

            if event.type == pygame.MOUSEBUTTONUP:
                newDino.click = False
                if newDino.name == "raptor":
                    newDino.velx = -10 # Velocidad hacia abajo
                
                if newDino.name == "fly":
                    newDino.velx = -15

            #Control vida del huevo
            # for o in ogresGroup:
            #     posEgg=[eggg.rect.right, eggg.rect.y]
            #     if o.rect.collidepoint(posEgg):
            #         print ("Me ha tocao. Soy el Egg")

            # for d in dinoFlyGroup:
            #     posEgg=[eggg.rect.right, eggg.rect.y]
            #     print("paso por aquí")
            #     if d.rect.collidepoint(posEgg):
            #         print ("Me ha tocao un dino Fly. Soy el Egg")

            #control

            for d in eggs:
                ls=pygame.sprite.spritecollide(d ,ogresGroup ,False) #ogros que colisionan con el huevo

                for e in ls:
                    print("ME ha tocao un ogro")
                    contTouchOgre += 1
                    print(contTouchOgre)

                    #Movimiento del ogro
                    e.velx = 0
                    e.dir = 4
                eggg.life -= contTouchOgre  #le quita una vida al huevo
                
                contTouchOgre = 0

            # for f in eggs:
            #     ls=pygame.sprite.spritecollide(f ,dinoFlyGroup ,False) #dinos que colisionan con el huevo
            #     for h in ls:
                    
            #         contTouch += 1
            #         print("ME ha tocao un dino fly")
            #         print(eggg.life )
            #         print(contTouch)
            # eggg.life -= contTouch
            # contTouch= 0



            for g in dinoFlyGroup:
                ls=pygame.sprite.spritecollide(g ,ogresGroup ,False) #dinos que colisionan con el huevo
                for h in ls:
                    h.dir = 2
                    h.vida -=1

                    if h.vida <0:
                        h.dir = 3
                        pantalla.blit( apple , [h.rect.x,h.rect.y ])
                        
                    #ogresGroup.remove(h)


            for i in raptorGroup:
                ls=pygame.sprite.spritecollide(i ,ogresGroup ,False) #dinos que colisionan con el huevo
                for h in ls:
                    h.dir = 2
                    h.vida -=1
                
                    if h.vida <0:
                        h.dir = 3
                        pantalla.blit( apple , [h.rect.x,h.rect.y ])

                    #ogresGroup.remove(h)


            
        #update        

        pantalla.fill(NEGRO)
        cuadros.update()
        dinoFlyGroup.update()
        eggs.update()
        ogresGroup.update()
        raptorGroup.update()


        pantalla.blit( apple , [800, 400 ])
        pantalla.blit(fondo,[0, 0])
        if (nivel == 1 and contClock< 500):
            pantalla.blit( nivel1Img , [400, 100])

        elif (nivel ==2 and contClock< 500):
            pantalla.blit( nivel2Img , [400, 100])

        cuadros.draw(pantalla)
        eggs.draw(pantalla)
        dinoFlyGroup.draw(pantalla)
        raptorGroup.draw(pantalla)
        ogresGroup.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
        contClock += 10
        #print (contClock)


        if (contClock % 500 == 0 and nivel ==1 and len(ogresGroup)<5):
             for i in range (1): 
                 randomy = random.randrange(400,450)
                 #randomy = rand + 200
                 r = Ogre1([-40, randomy], m, "r") 
                 r.velx= random.randrange(1,6)
                 ogresGroup.add(r)    

        if (contClock % 500 == 0 and nivel ==2 and len(ogresGroup)<7):
            for i in range (1): 
                 randomy = random.randrange(400,450)
                 #randomy = rand + 200
                 r = Ogre1([-40, randomy], m, "r") 
                 r.velx= random.randrange(1,6)
                 ogresGroup.add(r) 

                 randomy2 = random.randrange(400,450)
                 #randomy = rand + 200
                 r2 = Ogre2([-40, randomy2], mOgro2, "r2") 
                 r2.velx= random.randrange(1,7)
                 ogresGroup.add(r2)
            


            
            