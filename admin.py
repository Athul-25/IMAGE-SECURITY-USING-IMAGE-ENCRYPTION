import uuid
from flask import*
from database import *

admin=Blueprint('admin',__name__)



@admin.route('/adminhome')
def adminhome():
    return render_template("adminhome.html")


@admin.route('/admin_managestaff',methods=['get','post'])
def admin_managestaff():
    data={}
    qry3="select * from staff"
    res3=select(qry3)
    if res3:
        data['view']=res3
    if'submit'in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        emai=request.form['email']
        address=request.form['address']
        gender=request.form['gender']
        username=request.form['username']
        password=request.form['password']
        
        qry="insert into login values(null,'%s','%s','staff')"%(username,password)
        sid=insert(qry)
        
        qry2="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s')"%(sid,fname,lname,phone,emai,address,gender)
        insert(qry2)
        return ("<script>alert('REGISTERED...');window.location='/admin_managestaff'</script>")

    if'action'in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='update':
            qry4="select * from staff where staff_id='%s'"%(id)
            res4=select(qry4)
            if res4:
                data['up']=res4
                
                if'update'in request.form:
                    fname=request.form['fname']
                    lname=request.form['lname']
                    phone=request.form['phone']
                    emai=request.form['email']
                    address=request.form['address']
                    
                    qry5="update staff set first_name='%s',last_name='%s',phone='%s',email='%s',address='%s' where staff_id='%s'"%(fname,lname,phone,emai,address,id)
                    update(qry5)
                    return ("<script>alert('UPDATED...');window.location='/admin_managestaff'</script>")

        if action=='delete':
            qry6="delete from staff where staff_id='%s'"%(id)
            delete(qry6)
            return ("<script>alert('DELETED...');window.location='/admin_managestaff'</script>")
            
    
    return render_template("admin_manage_staff.html",data=data)


from flask import request, render_template, redirect, url_for
from PIL import Image
import os
import uuid
import random

# @admin.route('/share_image', methods=['GET', 'POST'])
# def share_image():
#     if request.method == 'POST' and 'image' in request.files:
#         image = request.files['image']
#         title=request.form['title']
#         filename = str(uuid.uuid4()) + os.path.splitext(image.filename)[-1]
#         path = os.path.join('static/share_images', filename)
#         image.save(path)

#         # Open the uploaded image
#         original_image = Image.open(path)
#         width, height = original_image.size

#         # Create shares with multiple random colors
#         share1 = create_random_color_image(width, height)
#         share2 = create_random_color_image(width, height)

#         # Save the shares
#         share1_path = f"static/share_images/{uuid.uuid4()}_share1.bmp"
#         share2_path = f"static/share_images/{uuid.uuid4()}_share2.bmp"
#         share1.save(share1_path)
#         share2.save(share2_path)
        
        
#         qry="insert into share values(null,'%s','%s','%s',curdate())"%(title,share1_path,share2_path)
#         insert(qry)

#         # Return the paths to the shares
#         return render_template("admin_share_image.html", share1_path=share1_path, share2_path=share2_path)

#     return render_template("admin_share_image.html")


# @admin.route('/share_image', methods=['GET', 'POST'])


# def share_image():
#     if request.method == 'POST' and 'image' in request.files:
#         image = request.files['image']
#         title = request.form['title']
#         filename = str(uuid.uuid4()) + os.path.splitext(image.filename)[-1]
#         path = os.path.join('static/share_images', filename)
#         image.save(path)

#         # Open the uploaded image
#         original_image = Image.open(path)
#         width, height = original_image.size

#         # Create shares with multiple random colors
#         share1 = create_random_color_image(width, height)
#         share2 = create_random_color_image(width, height)

#         # Save the shares
#         share1_path = f"static/share_images/{uuid.uuid4()}_share1.bmp"
#         share2_path = f"static/share_images/{uuid.uuid4()}_share2.bmp"
#         share1.save(share1_path)
#         share2.save(share2_path)

#         # Insert share paths into the database
       
       
#         qry="insert into share values(null,'%s','%s','%s',curdate())"%(title,share1_path,share2_path)
#         insert(qry)

#         # Return the paths to the shares
#         return render_template("admin_share_image.html", share1_path=share1_path, share2_path=share2_path)

#     return render_template("admin_share_image.html")

# def create_random_color_image(width, height):
#     # Create a new blank image
#     image = Image.new("RGB", (width, height))

#     # Fill the image with multiple random colors
#     for x in range(width):
#         for y in range(height):
#             # Generate a random color
#             color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#             image.putpixel((x, y), color)
#     return image




#########################ORIGINAL CODE#######################################

# from cryptography.fernet import Fernet


# @admin.route('/share_image', methods=['GET', 'POST'])


# def share_image():
#     if request.method == 'POST' and 'image' in request.files:
#         image = request.files['image']
#         title = request.form['title']
#         filename = str(uuid.uuid4()) + os.path.splitext(image.filename)[-1]
#         path = os.path.join('static/share_images', filename)
#         image.save(path)
        

#         key = Fernet.generate_key()
#         cipher = Fernet(key)
#         keys=str(key)
#         print(key)
        
#         def encryption():
#             with open(path, 'rb') as file:
#                 image_data = file.read()

#             encrypted_image_data = cipher.encrypt(image_data)

#             with open('encrypted_image.enc', 'wb') as file:
#                 file.write(encrypted_image_data)

#             share1 = encrypted_image_data[:len(encrypted_image_data)//2]
#             share2 = encrypted_image_data[len(encrypted_image_data)//2:]
#             share1_path="static/share_images/"+str(uuid.uuid4())+"share1.enc"
#             share2_path="static/share_images/"+str(uuid.uuid4())+"share2.enc"

#             with open(share1_path, 'wb') as file:
#                 file.write(share1)

#             with open(share2_path, 'wb') as file:
#                 file.write(share2)

#             print("Encryption and splitting complete.")
            
#             qry='insert into share values(null,"%s","%s","%s","%s",curdate())'%(title,share1_path,share2_path,keys)
#             insert(qry)
            
#         encryption()
        
    

            
 
                
#     return render_template("admin_share_image.html")


###############################END######################


########################NEW CODE################
from cryptography.fernet import Fernet
from PIL import Image
import os
import uuid

@admin.route('/share_image', methods=['GET', 'POST'])
def share_image():
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image']
        title = request.form['title']
        filename = str(uuid.uuid4()) + os.path.splitext(image.filename)[-1]
        path = os.path.join('static/share_images', filename)
        image.save(path)

        # Generate a 32-byte Fernet key
        key = Fernet.generate_key()

        # Convert the key to a string for storage
        key_str = key.decode('utf-8')
        
        # Save the key as share2 image path
        key_image_path = os.path.join('static/share_images/', str(uuid.uuid4()) + '_key.png')
        with open(key_image_path, 'wb') as key_file:
            key_file.write(key)

        cipher = Fernet(key)

        # Encrypt the image data
        with open(path, 'rb') as file:
            image_data = file.read()

        encrypted_image_data = cipher.encrypt(image_data)

        # Split the encrypted data into two parts
        share1 = encrypted_image_data[:len(encrypted_image_data)//2]
        share2 = encrypted_image_data[len(encrypted_image_data)//2:]

        share1_path = os.path.join('static/share_images/', str(uuid.uuid4()) + 'share1.enc')
        share2_path = os.path.join('static/share_images/', str(uuid.uuid4()) + 'share2.enc')

        # Save share1 as an encrypted image
        with open(share1_path, 'wb') as file:
            file.write(share1)

        # Save share2 as an encrypted image
        with open(share2_path, 'wb') as file:
            file.write(share2)

        print("Encryption and splitting complete.")

        # Insert into database with share2 image path as key
        qry = 'INSERT INTO share VALUES (null, "%s", "%s", "%s", "%s", curdate())' % (title, share1_path, share2_path, key_image_path)
        insert(qry)

    return render_template("admin_share_image.html")







@admin.route('/admin_request')
def admin_request():
    data={}
    qry="select * from key_request inner join share using(share_id) inner join staff using(staff_id)"
    res=select(qry)
    if res:
        data['view']=res
    
    if'action'in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='sendkey':
            qry1="select * from key_request inner join share using(share_id)  where request_id='%s'"%(id)
            res1=select(qry1)
            if res1:
                key=res1[0]['key']
                
                qry2='update key_request set key_file="%s" where request_id="%s"'%(key,id)
                update(qry2)
                return ("<script>alert('KEY SENDED...');window.location='/admin_request'</script>")

            
    return render_template("admin_request.html",data=data) 

