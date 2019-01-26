from flask import Flask, render_template
ex2_BMI = Flask(__name__)

@ex2_BMI.route("/bmi/<int:weight>/<int:height>")
def BMI_calc(weight,height):
    height_m = height/100
    BMI_cal = str(weight / ( height_m**2))
    return BMI_cal +" <br><p>BMI < 16 : Severely underweight</p> <br><p>18.5 <= BMI < 25: Normal</p> <br><p>25 <= BMI < 30: Overweight</p> <br><p>BMI > 30: Obese</p>" 


if __name__ == "__main__":
     ex2_BMI.run(debug=True)