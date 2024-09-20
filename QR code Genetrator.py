import qrcode as qr
image =qr.make("https://www.youtube.com/")
image.save("Youtube_QR.png")

