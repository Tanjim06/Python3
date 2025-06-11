import qrcode as qr

img = qr.make("https://www.facebook.com/profile.php?id=61555378191735")  #this will make a qr image of fb id

img.save("ankon.png")   #this will save the qr image by name of profile.png

