from flask import Flask,render_template,request
from main import take_command

app=Flask(__name__)

@app.route('/user',methods=['POST'])
def command():
    audio=request.data
    process=audio(take_command)
    

if __name__=='__main__':
    app.run(debug=True)