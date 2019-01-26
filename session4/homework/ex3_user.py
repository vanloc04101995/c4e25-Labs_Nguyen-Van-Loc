from flask import Flask, render_template
ex3_user = Flask(__name__)

users_dict={
    "huy":{"name":"Nguyen Quang Huy","age":29},
    "tuananh":{"name":"Huynh Tuan Anh","age":22},
    "vanloc":{"name":"Nguyen Van Loc","age":23},
}


@ex3_user.route("/user/<username>")
# def hi(name):
#     return "Hello" +" "+ name +". Have a nice day!"
def name_id(username):
    t= 0 
    for key in users_dict.keys():
        if key == username :
            t += 1 
    if t == 0:
        return "User not found" 
    else :
        return render_template("username.html",html_dicts = users_dict,html_username = username)

if __name__ == "__main__":
     ex3_user.run(debug=True) 
        
