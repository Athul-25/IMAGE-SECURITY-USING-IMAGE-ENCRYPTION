import uuid
from flask import*
from database import *

staff=Blueprint('staff',__name__)


@staff.route('/staffhome')
def staffhome():
    
    return render_template("staff_home.html")



@staff.route('/staff_view_image')
def staff_view_image():
    data={}
    qry="select * from share left join key_request using(share_id) "
    res=select(qry)
    if res:
        data['view']=res
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='request':
            qry1="insert into key_request values(null,'%s','%s','pending')"%(id,session['staff'])
            insert(qry1)
            return ("<script>alert('REQUESTED...');window.location='/staff_view_image'</script>")

    
    return render_template("staff_view_images.html",data=data)

import os
@staff.route("/download_key/<path:filename>")
def download_key(filename):
    # Specify the directory where your .bin files are stored
    directory = ""
    # Decode the filename from bytes to string and remove the unnecessary prefix
    filename = filename.encode("utf-8").decode("utf-8").replace("b'", "").replace("'", "")
    # Join the directory and filename to create the full path
    filepath = os.path.join(directory, filename)
    return send_file(filepath, as_attachment=True)









# @staff.route('/decrypt_image')
# def decrypt_image():
#     id=request.args['id']
#     qry="select * from share where share_id='%s'"%(id)
#     res=select(qry)
#     if res:
#         session['share_2']=res[0]['share_2']
        
#     if'submit'in request.form:
#         image=request.files['image']
#         session['share_1']='static/share_images'+str(uuid.uuid4())+image.filename

# from cryptography.fernet import Fernet

# from PIL import Image
# import os

# @staff.route('/decrypt_image', methods=['GET', 'POST'])
# def decrypt_image():
#     id=request.args['id']
    
#     qry="select * from share where share_id='%s'"%(id)
#     res=select(qry)
#     if res:
#         share_1=res[0]['share_1']
#         share_2=res[0]['share_2']
#         key=res[0]['key']
#         print(key)

        
#         def decryption(key):
#             # Read the shares
#             print("##################",key)
#             with open(share_1, 'rb') as file:
#                 share1 = file.read()

#             with open(share_2, 'rb') as file:
#                 share2 = file.read()

#             # Combine the shares
#             encrypted_image_data = share1 + share2

#             # Create a Fernet object for decryption using the same key
#             cipher_decrypt = Fernet(key)

#             # Decrypt the image data
#             decrypted_image_data = cipher_decrypt.decrypt(encrypted_image_data)

#             # Save the decrypted image
#             with open('decrypted_image.jpg', 'wb') as file:
#                 file.write(decrypted_image_data)

#             print("Decryption complete.")

    

#         # Call the decryption function with the encryption key
#         decryption(key)

from cryptography.fernet import Fernet
from PIL import Image
import os
import base64 
from bb import decrypt_images

@staff.route('/decrypt_image', methods=['GET', 'POST'])
def decrypt_image():
    id = request.args.get('id')
    
    qry = "SELECT * FROM share WHERE share_id='%s'" %(id)
    res = select(qry)
    if res:
        share1_path = res[0]['share_1']
        share2_path = res[0]['share_2']
        key_image = res[0]['key']
        
    if'submit' in request.form:
        image=request.files['image']
        key_image_path='static/share_images/'+image.filename
        
        if key_image_path==key_image:
        
            print(share1_path,share2_path,key_image_path,"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
            
            

            decrypted_image_data = decrypt_images(share1_path,share2_path,key_image_path)

            # Save the decrypted image
            decrypted_image_filename = "decrypted_image.jpg"
            with open("static/decrypted_images/decrypted_image.jpg", 'wb') as file:
                aa=file.write(decrypted_image_data)  
                print("Decryption complete.")
            return render_template("decrypt_images.html", decrypted_image_filename=decrypted_image_filename)

        else:
            return ("<script>alert('KEY MISMATCHING');window.location='/staff_view_image'</script>")

            
        
    return render_template("decrypt_images.html")



