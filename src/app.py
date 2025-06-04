from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    try:
#     num1 = int(request.form['num1'])
 #    num2 = int(request.form['num2'])
     
     number1 = request.args.get("number1", "")
     number2 = request.args.get("number2", "")
 
     result  = addnumber(number1,number2)
    except ValueError:
            result = "Invalid input. Please enter numbers only."

    return (
           
            """<form action="" method="get">
                Enter the number1: <input type="text" name="number1">
                <input type="submit" value="number1">
                Enter the number2: <input type="text" name="number2">
                <input type="submit" value="number2">
		 Enter the number3: <input type="text" name="number3">
		 <input type="submit" value="number3">
              </form>"""
          + result
          
    )

#@app.route("/<int:number1>/<int:number2>")
def addnumber (number1,number2):
 a = float(number1)
 b = float(number2)
 sum = a + b
 return str(sum)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
