import turtle  #turtle ve random kütüphanelerini çağırıyoruz
import random

#öncelikle ekran değişkenimizi ve özelliklerimizi ayarlıyoruz.
#ekran özellikleri ayarının altına kod boyunca kullanılacak değişkenlerimizi tanımlıyoruz
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("monster_turtle 2")

FONT = ("Arial", 30, "normal") # turtleda write fonks kullanılan yerler için özel tanımladığımız font değişkeni
score = 0  # score değişkenimizi ilk başta 0 olarak atadık
game_over = False #oyunu bitirmek için kullandığımız değişkenimiz

# turtle list
turtle_list = []  #ürettiğimiz her turtle ı alacağımız boş liste

# score turtle
score_turtle = turtle.Turtle()  # score oluşturmak için kullandığımız değişkenimiz

#countdown turtle

countdown_turtle = turtle.Turtle() #geri sayım için kullandığımız değişkenimiz

#make turtle properties
x_coordinates = [-30, -20, -10, 0, 10, 20, 30]
y_coordinates = [20, 10, 0, -10, -20]
# turtle grid multiplier
grid_size = 12 # turtle setup ederken kullandığımız x ve ya koordinat çarpanımız




def setup_score_turtle():   #score yazdırmak için kullanılacak fonksiyon
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = turtle_screen.window_height() / 2 #score ekranın neresinde olacağını ayarlamak
    y = top_height * 0.85
    score_turtle.setpos(0, y)
    score_turtle.write(arg="score: 0", move=False, align="center", font=FONT)




def make_turtle(x, y): #turtle oluşturma fonksiyonu
    t = turtle.Turtle()

    def handle_click(x, y): # tıklamayla skoru bir artırma fonks(iç fonks)
        # print(x, y) yapsak sadece koordinat bilgisi alırdık
        global score
        score += 1
        score_turtle.clear() #skorlar her seferinde üstüste yazmasın diye kullandığımız metot
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click) #tıklama metodu
    t.penup()
    t.shape("turtle")
    t.shapesize(2.5, 2.5)
    t.color("olivedrab")
    t.goto(x * grid_size, y * grid_size)  #turtle konum atama metodu
    turtle_list.append(t) #boş listemize üretilen turtle'ları atıyoruz





def setup_turtles(): # bu fonksiyonda for döngüsü kullanarak üretilen her turtle koordinatlara dağıtılır
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():  # tüm turtle'ları öncelikle gizliyoruz
    for t in turtle_list:
        t.hideturtle()

# reqursive function..(bir fonks içinde kendisini çağırma işlemi)
# bir reqursive func yapıyorsak bunun mutlaka bir exit noktası olması gerekir
# aksi halde func sonsuza kadar çalışır programı kapatana kadar
def show_turtles_randomly(): #turtle_list'den random bir tane turtle gösterme fonksiyonu
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        turtle_screen.ontimer(show_turtles_randomly, 200) #yine bir reqursive fonks
    else:
         hide_turtles() #eklenen else kodu (bunu eklemezsek oyun sonunda turtle kaybolmaz)

def countdown(time):  #geri sayım fonks. game overı'ı özellikle burda kullanıyoruz
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    top_height = turtle_screen.window_height()/2  #ekranda konumunu ve yazı fontu ayarlamak
    y = top_height*0.9
    countdown_turtle.setpos(0 , y-60)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear() #üstüste yazmasını engellemek
        countdown_turtle.write(arg="time : {}".format(time),move=False, align="center", font=FONT )
        turtle_screen.ontimer(lambda : countdown(time-1), 1000) #recursive şekilde kullanım var yine countdown için

    else:
        game_over = True
        countdown_turtle.clear() #clear metotla üstüste gerisayım yazması engellenir
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def start_game_up():  #tanımladığımız fonksiyonları düzenlediğimiz fonksiyon
    turtle.tracer(0)  # tracer metodu sayesinde turtle hareket etmeyip teleport olacak
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(15)
    turtle.tracer(1)

start_game_up()

turtle.mainloop() #oyun sonunda ekranın kendiliğinden kapanmasını engellleme metodu
