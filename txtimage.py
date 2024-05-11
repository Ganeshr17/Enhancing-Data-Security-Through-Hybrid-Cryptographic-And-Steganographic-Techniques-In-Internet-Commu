import base64
  
def txt_to_image():  
    file = open(r"D:\project\Design Project II\image\decoded.txt", 'rb')
    byte = file.read()
    file.close()
    decodeit = open(r"D:\project\Design Project II\image\detect_aes.jpg", 'wb')  
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()
#txt_to_image()