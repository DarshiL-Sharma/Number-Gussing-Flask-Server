from flask import Flask
import random

app = Flask(__name__)
print(random.__name__)
print(__name__)
random_number = random.randint(0,9)
print(random_number)

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Guess the number (0-9)</h1>'\
            '<p></p>'\
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGQyNndueHJqcHZtOGw3OXZnZ2RxaHVvM3pvbmppemtsM3o1dDIyYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JdFEeta1hLNnO/giphy.gif" width=500px>'

@app.route("/<int:numbers>")
def number_high(numbers):
    if numbers > random_number:
        return '<p> number is too high </p>'\
               '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDliOXB3Nmw5c2Ryczc3MHV3ZHhlcDNrNDhxa3g3MG16a3ducnVuayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lrN2cR6r4DvcQcTLzz/giphy.gif"width=500px>'

    elif numbers < random_number:
        return '<p> number is too low </p>'\
               '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDNqZDR6MXg3YmVzbzZ3a2Rwanh1b3Zwb3diN2lubGV5NW5ja2x1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.gif"width=700px>'

    else:
        return '<p> Yee! you got it !! </p>'\
               '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd29vbXhnbDBwbWx1NG92cWhwcTMxNW16Z2sycXU2ZThoNHptZDdqYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/x0yxQpWV9gPMRHnw7u/giphy.gif"width=500px>'

if __name__ == "__main__":
     app.run(debug=True)
