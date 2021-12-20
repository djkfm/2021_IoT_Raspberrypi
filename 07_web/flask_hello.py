from flask import Flask 

# Flask 객체 생성
app = Flask(__name__)

#alt shift 밑에 화살표 = 복붙
# 0.0.0.0:5000/
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/First">Go First<a/>
        <a href="/Second">Go Second<a/>
    '''
@app.route("/First") 
def first():
    return'''
        <p>First Page</p>
        <a href="/">Go Home</a>
    '''
@app.route("/Second") 
def second():
    return'''
        <p>Second Page</p>
        <a href="/">Go Home</a>
    '''

#터미널에서 직접 실행시킨 경우 
if __name__ == "__main__":
    app.run(host="0.0.0.0")