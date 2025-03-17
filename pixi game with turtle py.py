import turtle
import random

# تنظیمات صفحه
s = turtle.Screen()
s.setup(600, 600)
s.title("Pixel Show <3")
s.bgcolor("pink")

# متغیر امتیاز
score = 0

# 🔹 توابع مربوط به کنترل حرکت
def goup():
    """ تغییر جهت کاراکتر به سمت بالا """
    player.seth(90)

def godown():
    """ تغییر جهت کاراکتر به سمت پایین """
    player.seth(270)

def goright():
    """ تغییر جهت کاراکتر به سمت راست """
    player.seth(0)

def goleft():
    """ تغییر جهت کاراکتر به سمت چپ """
    player.seth(180)

# اضافه کردن و تنظیم کاراکتر اصلی
s.addshape(r"Your one")
player = turtle.Turtle()
player.shape(r"Your one")
player.penup()

# اضافه کردن و تنظیم مانع
s.addshape(r"Your one")
obstacle = turtle.Turtle()
obstacle.shape(r"Your one")
obstacle.penup()

# تعیین مکان تصادفی برای مانع
x = random.randint(-280, 280)
y = random.randint(-280, 280)
obstacle.goto(x, y)

# تنظیم قلم برای نمایش امتیاز
score_display = turtle.Turtle()
score_display.penup()
score_display.goto(-280, 250)
score_display.hideturtle()

# 🔹 تنظیم کنترل‌های کاربر
s.listen()
s.onkey(goup, "Up")
s.onkey(godown, "Down")
s.onkey(goleft, "Left")
s.onkey(goright, "Right")

# 🔹 حلقه اصلی بازی
try:
    while True:
        player.forward(3)

        # اگر برخوردی با مانع رخ داد
        if player.distance(obstacle) < 25:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            obstacle.goto(x, y)
            
            # افزایش امتیاز
            score += 3
            
            # نمایش امتیاز جدید
            score_display.clear()
            score_display.write(f"امتیاز شما: {score}", font=("B Nazanin", 20, "bold"))

except turtle.Terminator:
    print("Game Terminated!")

# نگه داشتن صفحه
s.mainloop()

## https://github.com/Shayanthn
## shayanthn78@gmail.com
""" 🚀 About the Developer
Python Expert | Advanced English Instructor | Creative Thinker

Passionate Python developer with expertise in web development, AI, automation, and data science. Skilled in problem-solving, clean code, and scalable solutions. Also an advanced English instructor with strong communication and technical documentation abilities.

💡 Innovator & Idea Generator | Always seeking to create efficient, cutting-edge projects.
📌 Proficient in Django, Flask, FastAPI, TensorFlow, Pandas, Selenium, and more.
🚀 Open to collaboration on GitHub and tech-driven projects.
 """
