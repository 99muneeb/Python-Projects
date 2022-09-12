# install qrcode
# pip install qrcode
import qrcode
# import qrcode as qr
# method 1 simple
"""

img=qr.make("linkedin.com/in/muneeb- 99")
img.save("muneeb_linkdin_profile.png")
"""
# method 2 advance
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.facebook.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("facebook_qr.png")


 