import pygame
import random
import sys

#VARIABLES A UTILIZAR

ALTO = 600 #defino el alto de la ventana
ANCHO = 600#defino el ancho de la ventana

#un par de colores que voy a usar mas adelante
BLACK = (0, 0, 0) #le asigno el color con numeros
RED = (255, 0, 122)
PURPLE = (100, 0, 255)
YELLOW = (255, 236, 0)
GREEN = (43, 159, 3)

#tamaño del cuadro
cuadro = 200

class Snake: #creo una clase para crear la serpiente
    def __init__(self): 
        self.velocity = 20 #con esto determinamos la velocidad del snake
        self.length = 1 #longitud del snake
        self.snake_body = [[220, 220], [240, 220]] #cuerpo de la serpiente
        self.actual_mo = random.choice(["right", "left", "down", "up"]) #movimiento actual, solo que al inicio es random
        self.incorrectmo = {"right": ["left"], #diccionario
                            "left": ["right",],
                            "up": ["down"],
                            "down": ["up"]} #esto lo hago para cuando vaya a la derecha no vaya a la izquierda y asi con los demas lados
        
        self.best_score = 1 #puntuacion max
        self.temp_score = 1 #score q llevas en la partida
    
    def moveSnake(self, screen): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #mover snake con el teclado
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    self.actual_mo = "left" #si presiono la flecha hacia la izquierda va a ese lado
                if event.key == pygame.K_RIGHT:
                    self.actual_mo = "right"#si presiono la flecha hacia la derecha va a ese lado
                if event.key == pygame.K_UP:
                    self.actual_mo = "up"#si presiono la flecha hacia arriba va hacia arriba
                if event.key == pygame.K_DOWN:
                    self.actual_mo = "down"#si presiono la flecha hacia abajo va hacia abajo
             
        self.snake_mov(screen)

    def snake_mov(self, screen): #mover sin problemas
        if self.actual_mo == "right":
            temp = self.snake_body[0][0] + self.velocity
            x = self.bandas(temp, "max_limit")
            self.actuSnake(x, "X", screen)
        if self.actual_mo == "left":
            temp = self.snake_body[0][0] - self.velocity
            x = self.bandas(temp, "min_limit")
            self.actuSnake(x, "X", screen)
        if self.actual_mo == "up":
            temp = self.snake_body[0][1] - self.velocity
            y = self.bandas(temp, "min_limit")
            self.actuSnake(y, "Y", screen)
        if self.actual_mo == "down":
            temp = self.snake_body[0][1] + self.velocity
            y = self.bandas(temp, "max_limit")
            self.actuSnake(y, "Y", screen) #movimiento vertical

    def actuSnake(self, value, key, screen):
        if key == "X":
            self.snake_body.insert(0, [value, self.snake_body[0][1]])
            self.snake_body.pop()#eliminar la ultima parte del snake
            self.dibujoSnake(screen)
        else:
            self.dibujoSnake(screen)
            self.snake_body.pop()#eliminar la ultima parte del snake
            self.snake_body.insert(0, [self.snake_body[0][0], value])

    
    def movimiento_valido(self, next_mov):
        if next_mov in self.incorrectmo[self.actuSnake()]:
            return True

    def dibujoSnake(self, screen):
        for idx, body in enumerate(self.snake_body):
            if idx == 0:
                pygame.draw.rect(screen, YELLOW, [body[0], body[1], 20, 20])
                continue
            pygame.draw.rect(screen, PURPLE, [body[0],body[1], 20, 20])

    def bandas(self, value_to_check, limit): #funcion para cuando llegue al borde de la pantalla aparezca en el otro lado
        if limit == "max_limit":
            if value_to_check > 580:
                return 0
            else:
                return value_to_check
        
        else:
            if value_to_check < 0:
                return 580
            else:
                return value_to_check

    def cabezaSnake(self):
        return self.snake_body[0]

class Food: #clase para la comida
    def __init__(self): #creo el metodo constructor
        self.foodPosition = (0, 0)
        self.randomFood()

    def randomFood(self): #función para la comida en lugar random
        self.foodPosition = (random.randrange(0, 580, 20), random.randrange(0, 580, 20))

    def comidaDibujo(self, screen):#para dibujar la comida en la panmtalla
        pygame.draw.rect(screen, GREEN, [self.foodPosition[0], self.foodPosition[1], 20, 20])

def verComida(snake, food, screen):
    if tuple(snake.cabezaSnake()) == food.foodPosition:
        food.randomFood()
        food.comidaDibujo(screen)

#funcion para decorar la ventana
def dibujar(screen):
    screen.fill(BLACK)
    x = 0
    y = 0
    for i in range(ANCHO):
        x += cuadro
        y += cuadro


def inicio(): #funcion par ainiciar pygame
    pygame.init()
    screen = pygame.display.set_mode((ALTO, ANCHO)) #paso los valores de la ventana
    pygame.display.set_caption("Proyecto final")#nombre de la ventana
    
    clock = pygame.time.Clock() #reloj para que no vaya tan rápido el juego
    snake = Snake()

    food = Food()

    fuente = pygame.font.SysFont("Ahoroni", 30) #variable para el texto en pantalla

    #bucle para crear el juego
    while True: 
        clock.tick(11) #agrego al bucle el reloj
        

        dibujar(screen)#mando a llamar la funcion con la que pinto la ventana
        snake.moveSnake(screen)
        verComida(snake, food, screen)
        score = fuente.render("Score: ", True, RED) #este el texto donde aparece el score
        screen.blit(score, (10, 560))
        best_score = fuente.render("Best score: ", True, RED)
        screen.blit(best_score, (10, 580))
        
        food.comidaDibujo(screen)
        pygame.display.update()

inicio()
