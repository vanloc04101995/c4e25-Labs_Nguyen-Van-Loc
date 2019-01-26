from flask import Flask, render_template
ex2_BMI_2 = Flask(__name__)
con_list=[
    "BMI < 16 : Severely underweight",
    "16 <= BMI < 18.5: Underweight",
    "18.5 <= BMI < 25: Normal",
    "25 <= BMI < 30: Overweight",
    "BMI > 30: Obese"

]
@ex2_BMI_2.route("/bmi/<int:weight>/<int:height>")
def BMI_calc(weight,height):
    height_m = height/100
    BMI_cal = str(round(weight / ( height_m**2),2))
    return render_template("BMI.html",bmi_cal = BMI_cal,con_list=con_list) 


if __name__ == "__main__":
     ex2_BMI_2.run(debug=True)