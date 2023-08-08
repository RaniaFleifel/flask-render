from flask import Flask,render_template,request
from datetime import datetime, timedelta

app = Flask(__name__)
a=[]
entries=[]
options_month = ['jan', 'feb', 'mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
interest_rate=18/100

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

@app.route('/grace_period',methods=['POST'])
def grace_period():     
        print("grace_period? ###############################################")

        if len(a)<=4:
            loan_size_txt="Loan amount= {} egp".format(a[0])
            loan_size=a[0]
            frequency_txt="Dispersment starts tomorrow (aka month {})".format(a[2])
            start_month=a[2]

        else:
            loan_size_txt="Loan amount= {} egp".format(a[len(a)-3])
            loan_size=a[len(a)-3]
            frequency_txt="Dispersment starts tomorrow (aka month {})".format(a[len(a)-1])
            start_month=a[len(a)-1]

            
        #loan_size_txt="Loan amount= {} egp".format(a[len(a)-3])
        #frequency_txt="Dispersment starts tomorrow (aka month {})".format(a[len(a)-2])
        
        # Get the user-selected value from the dropdown
        selected_option = request.form['option']
        a.append(selected_option)
        
        # Process the selected option (You can add your own logic here)
        options_txt = f"Grace period? {selected_option} "

        df = pd.DataFrame(columns=['month','std_loan','flexible_loan'])
        monthly_share=round((loan_size+(interest_rate*loan_size))/12,1)

        if selected_option.lower()=='non':
            options_txt+="--> std loan schedule"
            num_months=12
            print("###############################################")
            print("monthly_share",monthly_share)
            print(start_month,options_month.index(start_month.lower()))
            loc_start_month=options_month.index(start_month.lower())
           
            for i in range(num_months):
                this_month=options_month[(loc_start_month+i)%12]
                new_line=[this_month,monthly_share,monthly_share]
                
                df.loc[i]=new_line
            
            df.loc[i+1]=["Total (egp)",round(df['std_loan'].sum(),1),round(df['flexible_loan'].sum(),1)]
            print(a)
            table=tabulate(df, headers='keys', tablefmt='psql')
            print(table)

            table = df.to_html(index=False)
        
            entries.append(a)
            return render_template('index_new_v2.html',loan_size_txt=loan_size_txt,frequency_txt=frequency_txt,options_txt=options_txt)#tmp)#+"<br/>The provided loan size is {} EGP".format(output[0]))#.append('The size of the loan is {} egp\n'.format(loan_size[0])))

        else:# selected_option.lower()=='yes':
            print("###############",a)
            #@app.route('/grace_period_months',methods=['POST'])
            return render_template('index_new_v2.html',loan_size_txt=loan_size_txt,frequency_txt=frequency_txt,options_txt=options_txt)#tmp)#+"<br/>The provided loan size is {} EGP".format(output[0]))#.append('The size of the loan is {} egp\n'.format(loan_size[0])))
