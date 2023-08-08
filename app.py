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
    
@app.route('/freq',methods=['POST'])
def freq():     
        print("freq ###############################################")
        print(len(a)-2)

        if len(a)<=4:
            loan_size_txt="Loan amount= {} egp".format(a[0])
        else:
            loan_size_txt="Loan amount= {} egp".format(a[len(a)-1])
        # Get the user-selected value from the dropdown
        selected_option = request.form['option']
        a.append(selected_option)
        
        # Process the selected option (You can add your own logic here)
        result = f"You selected: {selected_option} payements"
        tom_date = datetime.now()+timedelta(1)
        tom_month=tom_date.strftime("%b")
        
        print(tom_month)
       
        if selected_option=='monthly':
            result+="..... Dispersment starts tomorrow (aka month {})".format(tom_month)
            a.append(tom_month)
        else:
            result+="..This option is not applied in the website yet"  
            
        print(a)
        return render_template('index_new_v2.html',loan_size_txt=loan_size_txt,frequency_txt=result)#tmp)#+"<br/>The provided loan size is {} EGP".format(output[0]))#.append('The size of the loan is {} egp\n'.format(loan_size[0])))
