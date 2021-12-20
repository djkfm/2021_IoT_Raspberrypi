from flask import Flask 
import RPi.GPIO as GPIO

LED_PIN1 = 2
LED_PIN2 = 3


# Flask 객체 생성
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

#alt shift 밑에 화살표 = 복붙
# 0.0.0.0:5000/
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/Led/Yel/on">Led Yel on<a/>
        <a href="/Led/Yel/off">Led Yel off<a/>
        <a href="/Led/Bule/on">Led Bule on<a/>
        <a href="/Led/Bule/off">Led Bule off<a/>
    '''

@app.route("/Led/<color>/<op>")   
def led_color_op(color, op):
    if color == "Yel":
        if op == "on":
            GPIO.output(LED_PIN1, GPIO.HIGH)
            return'''
            <p>Led Yel on</p>
            <a href="/">Go Home</a>
        '''
        elif op == "off":
            GPIO.output(LED_PIN1, GPIO.LOW)
            return'''
            <p>Led Yel off</p>
            <a href="/">Go Home</a>
        '''
    elif color == "Bule":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return'''
            <p>Led Yel on</p>
            <a href="/">Go Home</a>
        '''
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return'''
            <p>Led Yel off</p>
            <a href="/">Go Home</a>
        '''


#터미널에서 직접 실행시킨 경우 
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    finally:
        GPIO.cleanup()