from flask import*
from database import*
from admin import admin
from public import public
from staff import staff

app=Flask(__name__)
app.secret_key="crypto"
app.register_blueprint(admin)
app.register_blueprint(public)
app.register_blueprint(staff)


app.run(debug=True,port=5009)