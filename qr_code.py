import qrcode

def make_qr():
    web = input("Enter a valid WEB address: ")
    file = input("Enter a filename please: ")

    output_img = qrcode.make(f"{web}")
    type(output_img)
    output_img.save(f"{file}")
    return file
make_qr()
