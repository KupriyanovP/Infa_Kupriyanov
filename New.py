from graph import *


windowSize(1500,500)
penColor(0, 0, 0)
c = canvas()
canvasSize(1500, 500)
c.configure(background="white")
penSize(1)

def boiii(x, shirt_color, hair_color, eye_color, skin_color):
    #body
    c.create_oval(300+x, 400, 600+x, 600, fill=shirt_color)

    #head
    penSize(0)
    brushColor(skin_color)
    circle(450+x, 300, 125)

    # mouth
    brushColor(255, 0, 0)
    polygon([(450+x, 375), (400+x, 340), (500+x, 340)])

    # nose
    brushColor("brown")
    polygon([(450+x, 330), (435+x, 310), (465+x, 310)])

    # eye holes
    c.create_oval(383+x, 260, 433+x, 300, fill=eye_color)
    c.create_oval(467+x, 260, 517+x, 300, fill=eye_color)

    # pupils
    brushColor("black")
    circle(408+x, 280, 7)
    circle(492+x, 280, 7)

    # hair
    brushColor(hair_color)
    polygon([(336+x, 265), (310+x, 229), (350+x, 234)])
    polygon([(348+x, 239), (337+x, 196), (371+x, 212)])
    polygon([(365+x, 215), (371+x, 174), (393+x, 196)])
    polygon([(384+x, 199), (393+x, 158), (414+x, 188)])
    polygon([(410+x, 189), (421+x, 146), (442+x, 179)])
    polygon([(437+x, 180), (451+x, 147), (467+x, 184)])
    polygon([(461+x, 184), (482+x, 155), (487+x, 189)])
    polygon([(481+x, 189), (507+x, 157), (509+x, 200)])
    polygon([(502+x, 197), (526+x, 163), (526+x, 209)])
    polygon([(521+x, 205), (549+x, 176), (542+x, 222)])
    polygon([(540+x, 221), (569+x, 197), (558+x, 236)])
    polygon([(554+x, 235), (585+x, 225), (564+x, 256)])

    # hands
    brushColor(skin_color)
    penColor('white')
    polygon([(291+x, 435), (155+x, 158), (183+x, 155), (316+x, 404)])
    polygon([(565+x, 400), (647+x, 150), (673+x, 154), (599+x, 412)])

    # sleeves
    penColor('black')
    brushColor(shirt_color)
    polygon([(335+x, 468), (283+x, 463), (268+x, 422), (325+x, 393), (356+x, 425)])
    polygon([(558+x, 455), (603+x, 451), (611+x, 409), (561+x, 382), (536+x, 420)])

    # wrists
    c.create_oval(145+x, 98, 191+x, 168, fill=skin_color, width=0)
    c.create_oval(635+x, 98, 681+x, 168, fill=skin_color, width=0)

boiii(0, 'green','#e7cc04','#9fb6a4', '#F0B8A0')
boiii(500, '#f77000', '#cd05fa', '#8ab3f4', '#F0B8A0')
label("PYTHON is REALLY AMAZING!", 110, 10, font=("Calibry", 83), bg="#00DD10", bd=1)

run()
