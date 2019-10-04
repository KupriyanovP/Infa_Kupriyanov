from graph import *
import math


def cords(event):
    print(event.x, event.y)


onMouseDown(cords, 0)


def body(x, shirt_color, skin_color):
    c.create_oval(x - 150, 400, x + 150, 600, fill=shirt_color)

    # hands
    brushColor(skin_color)
    penColor('white')
    polygon([(x - 159, 435), (x - 295, 158), (x - 267, 155), (x - 134, 404)])
    polygon([(115 + x, 400), (197 + x, 150), (223 + x, 154), (149 + x, 412)])

    # sleeves
    penColor('black')
    brushColor(shirt_color)
    polygon([(x - 115, 468), (x - 167, 463), (x - 182, 422), (x - 125, 393), (x - 94, 425)])
    polygon([(x + 108, 455), (x + 153, 451), (x + 161, 409), (x + 111, 382), (x + 86, 420)])

    # wrists
    c.create_oval(x - 305, 98, x - 259, 168, fill=skin_color, width=0)
    c.create_oval(x + 185, 98, x + 231, 168, fill=skin_color, width=0)


def one_hair(face_x, face_y, face_radius, alpha_0):
    polygon([(face_x - (face_radius + 30) * math.cos(alpha_0), face_y - (face_radius + 30) * math.sin(alpha_0)),
             (face_x - (face_radius - 7) * math.cos(alpha_0) + 10 * math.sin(alpha_0),
              face_y - (face_radius - 7) * math.sin(alpha_0) - 10 * math.cos(alpha_0)),
             (face_x - (face_radius - 7) * math.cos(alpha_0) - 10 * math.sin(alpha_0),
              face_y - (face_radius - 7) * math.sin(alpha_0) + 10 * math.cos(alpha_0))])


def face(x, hair_color, eye_color, skin_color):
    penSize(0)
    brushColor(skin_color)
    face_x = x
    face_y = 300
    face_radius = 125
    circle(face_x, face_y, face_radius)

    # mout
    brushColor(255, 0, 0)
    polygon([(face_x, face_y + 75), (face_x - 50, face_y + 40), (face_x + 50, face_y + 40)])

    # nose
    brushColor("brown")
    polygon([(face_x, face_y + 30), (face_x - 15, face_y + 10), (face_x + 15, face_y + 10)])
    x = 0
    # eye holes
    c.create_oval(face_x - 67, face_y - 40, face_x - 17, face_y, fill=eye_color)
    c.create_oval(face_x + 17, face_y - 40, face_x + 67, face_y, fill=eye_color)

    # pupils
    brushColor("black")
    circle(face_x - 42, face_y - 20, 7)
    circle(face_x + 42, face_y - 20, 7)

    # hair
    brushColor(hair_color)
    alpha_0 = math.pi / 6
    for i in range(20):
        one_hair(face_x, face_y, face_radius, alpha_0)
        alpha_0 = alpha_0 + 1 / 30 * math.pi


def boy(x, shirt_color, hair_color, eye_color, skin_color):
    body(x, shirt_color, skin_color)
    face(x, hair_color, eye_color, skin_color)

windowSize(1500, 500)
penColor(0, 0, 0)
c = canvas()
canvasSize(1500, 500)
c.configure(background="white")
penSize(1)

boy(450, 'green', '#e7cc04', '#9fb6a4', '#F0B8A0')
boy(950, '#f77000', '#cd05fa', '#8ab3f4', '#F0B8A0')
label("PYTHON is REALLY AMAZING!", 20, 10, font=("Calibry", 70), bg="#00DD10", bd=1)

run()
