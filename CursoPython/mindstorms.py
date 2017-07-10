import turtle

def draw_mandala ():
    #Funcao desenha uma mandala com o quadrado.

    mandala = turtle.Turtle()
    mandala.shape ("turtle")
    mandala.color ("green")
    mandala.speed (10)

    cnt = 0
    i = 0
    while (cnt < 36): #loop para rotacionar 360 graus em incrementos de 10
        
        if (i<4): #desenha o quadrado
            mandala.forward (100)
            mandala.right (90)
            i = i + 1
        else:
            mandala.right (10) #inclina o desenho
            cnt = cnt + 1
            i = 0
            

def draw_square ():
    #Funcao desenha um quadrado
    
    square = turtle.Turtle()
    square.shape ("turtle")
    square.color ("black")
    square.speed (10)

    i=0
    while (i<4):
        square.forward (100)
        square.right (90)
        i = i + 1

    
def draw_circle ():
    #Funcao desenha um circulo
    
    circle = turtle.Turtle()
    circle.shape ("arrow")
    circle.color ("blue")
    circle.speed (10)

    circle.circle (100)


def draw_triangle ():
    #Funcao desenha um triangulo
    
    tri = turtle.Turtle()
    tri.shape ("arrow")
    tri.color ("white")
    tri.speed (10)

    i=0
    while (i<3):
        tri.forward (100)
        tri.right (120)
        i = i + 1

    
def main ():
    #Funcao principal.
    #Desenha o canvas, chamas as demais funcoes, e permite a finalizacao ao final

    window = turtle.Screen ()
    window.bgcolor ("red")

    #draw_square ()
    #draw_circle ()
    #draw_triangle ()
    draw_mandala ()
    
    window.exitonclick()


main()
