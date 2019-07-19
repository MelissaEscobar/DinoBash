import pygame
import random

ANCHO=1300
ALTO=700
BLANCO=[255,255,255]

NEGRO=[0,0,0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]

COLOR = [30, 40, 50]


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
            

class Apple(pygame.sprite.Sprite):
    def __init__(self, pos_ini,image ):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.number = 20 # numero inicial de manzanaspara el nivel 1


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
    
    
    # ----------------------------- CARGA DE IMAGENES GLOBALES --------------------------------


    fondo = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/background.png')

    #imagen de la manzana
    apple = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/apple.png')

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



    # --------------------------- CARGA DE OBJETOS (IMAGENES, MUSICA, GRUPOS) PARA EL NIVEL 1 -------------------------------
    #Dinos boxes
     
    cuadros = pygame.sprite.Group()    

    dinoBox1 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/cuadro1.png')
    c1= CuadroStatic([900, 50], dinoBox1, "dinoFlyBox1")     
    cuadros.add(c1)

    dinoBox2 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/cuadro2.png')
    c2= CuadroStatic([1100, 50], dinoBox2, "dinoRaptorBox2")     
    cuadros.add(c2)

    # ---------------- creacion de los enemigos - monstruos -----------------------------------
    ogresGroup = pygame.sprite.Group()

     #IMagen con los sprites Ogro 1
    img=pygame.image.load('/home/melii/Documents/Python/Dinobash/img/orc1.png')# Ogro 1
    m = cortarimg(img,7,5) 

     #IMagen con los sprites a recortar ogro 2
    imgOgro2=pygame.image.load('/home/melii/Documents/Python/Dinobash/img/orc2.png')# Ogro 2
    mOgro2 = cortarimg(imgOgro2,7,5)

    # ---------------------- creacion  de dinos ------------------------------
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



#   -----------------------CARGA DE OBJETOS (IMAGENES, MUSICA, GRUPOS)PARA EL NIVEL 2 -----------------------------

    # grupo de cuadros para el nivel 2
    cuadros2 = pygame.sprite.Group()  

    #Protoceratops Dino
    dinoBox3 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/cuadro1.png')
    c3= CuadroStatic([1100, 50], dinoBox3, "dinoRaptorBox2")     
    cuadros2.add(c3)

    # Tiranosaurio dino
    dinoBox4 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/cuadro2.png')
    c4= CuadroStatic([1100, 50], dinoBox4, "TiranosaurioBox2")     
    cuadros2.add(c4)
    # cuadros de este tipo de dnosaurio solo aparecen en el nivel 2
    

    # ----------------------------  creacion de trolles para el nivel 2 --------------------

    troll1 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/troll1.png')

    imgTroll1= cortarimg(troll1,7,5) #corte de sprites

    
    troll2 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/troll2.png')
    imgTroll2= cortarimg(troll2,7,5)  #corte de sprites


    troll3 = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/troll2.png')
    imgTroll3= cortarimg(troll3 ,7,5)  #corte de sprites
    



    

    # --------------------------------------------------  WHILE -------------------------------------------------------------------

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True   
            

            
            if event.type == pygame.MOUSEBUTTONDOWN:
        
                p = event.pos # position of the click
        # -----------   FLAG    --------            
                if 850 >p[0] > 490 and  330 >p[1]> 230: # Play -> level 1
                    #background nivel 1
                    if nivel == 1:
                        fondo = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/background.png')


                        if c1.rect.collidepoint(event.pos):
                            newDino = DinoFly(c1.rect, d1 , "fly") 
                            newDino.click = True
                            dinoFlyGroup.add(newDino)

                        if c2.rect.collidepoint(event.pos): #c1 es el cuadro verde
                            newDino = Raptor(c2.rect, d2 , "raptor")
                            newDino.click = True
                            raptorGroup.add(newDino)
                        
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

                    elif nivel == 2:
                        # background nivel 2
                        fondo = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/background2.jpg') 
                        


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

                elif 820 >p[0] > 510 and  450 >p[1]> 370: # tutorial
                    fondo = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/instruccion1.jpg')



                elif 820 >p[0] > 510 and  560 >p[1]> 490: # creditos
                    fondo = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/creditos.jpg')
                    

                elif 820 >p[0] > 510 and  680 >p[1]> 600: # exit 
                    fin = True 

                else:
                    pass


                
        #update        


        pygame.display.flip()
        reloj.tick(10)
        contClock += 10

       # pantalla.fill(NEGRO)
        pantalla.blit(fondo,[0, 0])

            


            
            