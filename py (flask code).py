from flask import Flask,render_template,request
from boltiotai import openai
from sec import OPENAI_API
app=Flask(__name__,template_folder='templates')
openai.api_key=OPENAI_API
@app.route('/')
def index():
    return render_template('main.html')
@app.route('/out', methods=['POST'])
def out():
    user_details=request.form['user_details']
    response=openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role':'user','content':user_details
        }]
    ) 
    ans=response['choices'][0]['message']['content']  
    return render_template('main.html',user_details=user_details,ans=ans)
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

