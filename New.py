from graph import *


penColor(0, 0, 0)
canva = canvas()
canvasSize(900, 500)
canva.configure(background="black")
penSize(1)
nnn
#body
canva.create_oval(300, 400, 600, 600, fill="orange")

#head
brushColor("#F0B8A0")
circle(450, 300, 125)

# mouth
brushColor(255, 0, 0)
polygon([(450, 375), (400, 350), (500, 350)])

# nose
brushColor("brown")
polygon([(450, 340), (435, 320), (465, 320)])

# eye holes
canva.create_oval(375, 260, 425, 300, fill="#00BFFF")
canva.create_oval(475, 260, 525, 300, fill="#00BFFF")

# pupils
brushColor("black")
circle(400, 280, 5)
circle(500, 280, 5)

# hair
brushColor("violet")
polygon([(336, 265), (310, 229), (350, 234)])
polygon([(348, 239), (337, 196), (371, 212)])
polygon([(365, 215), (371, 174), (393, 196)])
polygon([(384, 199), (393, 158), (414, 188)])
polygon([(410, 189), (421, 146), (442, 179)])
polygon([(437, 180), (451, 147), (467, 184)])
polygon([(461, 184), (482, 155), (487, 189)])
polygon([(481, 189), (507, 157), (509, 200)])
polygon([(502, 197), (526, 163), (526, 209)])
polygon([(521, 205), (549, 176), (542, 222)])
polygon([(540, 221), (569, 197), (558, 236)])
polygon([(554, 235), (585, 225), (564, 256)])

# hands
brushColor("#F0B8A0")
polygon([(291, 435), (155, 158), (183, 155), (316, 404)])
polygon([(565, 400), (647, 150), (673, 154), (599, 412)])

# sleeves
brushColor("orange")
polygon([(335, 468), (283, 463), (268, 422), (325, 393), (356, 425)])
polygon([(558, 455), (603, 451), (611, 409), (561, 382), (536, 420)])

# wrists
canva.create_oval(145, 98, 191, 168, fill="#F0B8A0")
canva.create_oval(635, 98, 681, 168, fill="#F0B8A0")

# text box
label("PYTHON is AMAZING", 0, 0, font=("Times New Roman", 56), bg="#00DD10")
run()
