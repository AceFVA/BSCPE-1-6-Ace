import qrcode
qr = qrcode.QRCode(
	version = 9,
	box_size = 10,
	border = 5,
)

input_data = input("Link: ")

qr.add_data(input_data)
qr.make(fit = True)
image = qr.make_image(fill = "black", back_color = "white")
image.save("GeneratedQR.png")
