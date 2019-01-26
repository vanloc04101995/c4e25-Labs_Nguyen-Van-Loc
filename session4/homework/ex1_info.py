from flask import Flask, render_template,redirect
ex1_info = Flask(__name__)
info_list = [
   {'name': 'Nguyen Van Loc',
   'age': 23,
   'school': 'Ha Noi university of science and technology',
   'hobby':['Football','Reading books']
   },
#    {'name': 'Nguyen Quang Huy',
#    'age': 24,
#    'school': 'Ha Noi university of science and technology',
#    'hobby':'Reading book',
#    }
]

@ex1_info.route("/about-me")
def c4e25():
    return render_template("information.html",i_list = info_list)

@ex1_info.route("/school")
def school():
    return redirect("http://techkids.vn")
    
if __name__ == "__main__":
     ex1_info.run(debug=True)