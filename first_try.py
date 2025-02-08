import qrcode
def get_user_inpts(user_website,user_file): 
    website = input("Please enter a website: ")
    file = input("What would you like to name the img?: ")
    return website, file 

def generate_qr():
    img = qrcode.make(get_user_inpts)
    type(img)
    img.save("")

generate_qr()
