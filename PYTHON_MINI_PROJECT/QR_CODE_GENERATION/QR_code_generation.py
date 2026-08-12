import qrcode
# taking upi id as a input
upi_id=input("enter your UPI ID =")
# upi://pay?pa=UPI_ID&pn=name&am=Amount&cu=CURRENCY&tn=MESSAGE
# define the payment uri based on the upi id and the payment app
#you can modify these url based on the payment apps ypu want to support

google_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# create qr code
google_pay_url_qr=qrcode.make(google_pay_url)
# save the  qr code to image file
google_pay_url_qr.save('google_pay_url.png')

#display the qr code 
google_pay_url_qr.show()