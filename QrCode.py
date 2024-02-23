#pip install QRCode
import qrcode

data = "https://www.youtube.com/watch?v=Ys7-6_t7OEQ"

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color = "white")

#img.show()

img.save("qrcode_python.png")
