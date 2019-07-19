import pygame
import random


ANCHO=1300
ALTO=700
BLANCO=[255,255,255]

NEGRO=[0,0,0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]

COLOR = [30, 40, 50]




if __name__ == "__main__":
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    contClock = 0 #contador de los pulsos del reloj
    fin = False
    reloj = pygame.time.Clock()
    nivel = 2
    opt = 0 # bandera para saber si debomostrar el menu, el nivel 1, creditos o salir

    #carga de la imagen que contiene el letrero del nivel 1

    fondo = pygame.image.load('/home/melii/Documents/Python/Dinobash/img/instruccion1.jpg')



    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True   

            if event.type == pygame.MOUSEBUTTONDOWN:
                print( event.pos) # position of the click

        pantalla.blit( fondo , [0, 0])
        pygame.display.flip()

