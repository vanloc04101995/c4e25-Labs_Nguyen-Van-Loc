from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/") # neu nguoi dung vao trang chu
# def home():# view function
#     return "Hello ,I'm again"

# @app.route("/c4e25")
# def c4e25():
#     return "This is c4e25"

# @app.route("/hi/<name>")
# def hi(name):
#     return "Hello" +" "+ name +". Have a nice day!"

# @app.route("/add/<int:x>/<int:y>")
# def add(x,y):  
#     return str(x+y)

# @app.route("/simple_html")
# def simple_html():
#     return "<h3></h3>"

# @app.route("/html")
# def html():
#     return render_template("sample.html")

# food_list = [
#     "Bun dau",
#     "Spring roll",
#     "Fried chicken"
# ]

food_list=[
    {'title':'bun cha','image':'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/B%C3%BAn_Ch%E1%BA%A3.jpg/1200px-B%C3%BAn_Ch%E1%BA%A3.jpg'},
    {'title':'spring roll','image':'https://tastesbetterfromscratch.com/wp-content/uploads/2013/03/Fresh-Spring-Rolls-15-500x375.jpg'},
    {'title':'fried chicken','image':'https://www.tasteofhome.com/wp-content/uploads/2018/04/Crispy-Fried-Chicken_exps6445_PSG143429D03_05_5b_RMS-1-696x696.jpg'}
    ]
# truyen vao 1 list
@app.route("/menu")
def menu():
    return render_template("menu.html", f_list=food_list)

@app.route("/menu/<int:x>") #detail .1 mon thoi
def food(x):
    return render_template("food.html", Title = food_list[x]['title'],Image = food_list[x]['image'] )

# truyen vao 1 dict
detail = {
    'title': 'bun cha',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/B%C3%BAn_Ch%E1%BA%A3.jpg/1200px-B%C3%BAn_Ch%E1%BA%A3.jpg'
}
@app.route("/food_detail")
def food_detail():
    return render_template("food_detail.html", detail=detail)



# @app.route("/food_dict")
# def food_detail():
#     return render_template("food_detail.html", detail=detail)

if __name__ == "__main__":
     app.run(debug=True)
# nguoi dung truy cap menu, thi se nhoi food_list vao html voi bien ten la food_list, du lieu nay chui vao html chay vong 
# lap for sinh ra so the <li> tuong ung, f_list la list trong html