from flask import Flask 
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello,world!'
@app.route('/getdetails')
def get_details():
    return 'Nagajothi - 22it024'
if__name__ == '__main__':
    app.run(debug=True)