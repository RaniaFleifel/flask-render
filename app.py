from flask import Flask,render_template,request
app = Flask(__name__)
a=[]

@app.route('/')
#def hello_world():
#    return 'Hello, World!'
def home():
    return render_template('index_new_v2.html')

@app.route('/amount',methods=['POST'])

def amount():
    #a=[]
    loan_size=[int(x) for x in request.form.values()]#int(request.form.values())
    while loan_size[0]>15000:        
        tmp="The cap of the loan is 15000.. Please re-enter the loan amount"
        # loan_size=[int(x) for x in request.form.values() if isinstance(x,int)]#int(request.form.values())
        for x in request.form.values():
            if isinstance(x,int):
                loan_size=int(x)
            else:
                continue
        output=loan_size#np.round_(prediction[0],2)
        
        return render_template('index_new_v2.html',loan_size_txt=tmp)#.append('The size of the loan is {} egp\n'.format(loan_size[0])))

    else:
        print(request.form.values())
        tmp=f"You selected: {loan_size[0]} egp"
        output=loan_size
        #print(output,output[0])
        print("new entry###############################################")
        
        a.append(loan_size[0])
        print(a)

        return render_template('index_new_v2.html',loan_size_txt=tmp)
    
