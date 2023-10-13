import qrcode

data = (
    "BEGIN:VCARD\n"
    "VERSION:3.0\n"
    "N:AHMEDOV;Zafar;;;\n"
    "FN:Zafar AHMEDOV\n"
    "TEL;TYPE=CELL:+998905028888\n"
    "EMAIL;TYPE=EMAIL:evrotbm@evrotbm.uz\n"
    "ORG:EVRO tbm;\n"
    "TITLE:Sales\n"
    "WORK;TYPE=WORK: Sales Manager\n"
    "ADR;TYPE=HOME:;;Evro TBM, Samarkand;;;\n"
    "URL:https://evrotbm.com/en/bosh-sahifa/\n"
    "URL:https://t.me/Evrotbm\n"
    "END:VCARD"
)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="black")
img.save(f"C:/Users/User/Desktop/qr.png")
