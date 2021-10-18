from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open("static/qr_photos/qrdata.png"))
new = data[0].data
print(new)
new = new.decode('utf-8')
letter_list = new.split(",")
print(letter_list)


