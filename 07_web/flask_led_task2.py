from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN1 = 21
LED_PIN2 = 20


# Flask 객체 생성
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

#alt shift 밑에 화살표 = 복붙
# 0.0.0.0:5000/
@app.route("/")
def home():
    return render_template("led2.html")
        

@app.route("/led/<op>")   
def led_color_op(op):
    if op == "Yelon":
        GPIO.output(LED_PIN1, GPIO.HIGH)
        return "Yel LED ON"
        
    elif op == "Yeloff":
        GPIO.output(LED_PIN1, GPIO.LOW)
        return "Yel LED OFF"

    
    
    elif op == "Blueon":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return "Blue LED ON"
        
    elif op == "Blueoff":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return "Blue LED OFF"

    else:
        return "ERROR"


#터미널에서 직접 실행시킨 경우 
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    finally:
        GPIO.cleanup()