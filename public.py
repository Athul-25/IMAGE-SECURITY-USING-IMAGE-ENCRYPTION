from flask import*
from database import*

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')


@public.route('/login',methods=['get','post'])
def login():
    if'submit'in request.form:
        username=request.form['username']
        password=request.form['password']
        
        
        qry="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(qry)
        if res:
            session['log']=res[0]['login_id']
            usertype=res[0]['usertype']
            
            if usertype=='admin':
                return ("<script>alert('WELCOME ADMIN...');window.location='/adminhome'</script>")
            if usertype=='staff':
                qry3="select * from staff where login_id='%s'"%(session['log'])
                res3=select(qry3)
                if res3:
                    session['staff']=res3[0]['staff_id']
                    return ("<script>alert('WELCOME STAFF...');window.location='/staffhome'</script>")

    
    return render_template("login.html")
