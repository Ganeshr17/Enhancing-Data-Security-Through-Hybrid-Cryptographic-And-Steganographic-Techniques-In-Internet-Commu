import sys
import cv2
import os
import numpy as np
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
import hashlib


def decrypt(key, save_folder_path,script_dir):
    key = hashlib.sha256(key.encode()).digest()[:16]
    key = key.hex()

    mode = AES.MODE_CBC
    keySize = 32
    ivSize = AES.block_size if mode == AES.MODE_CBC else 0
    output_image_path = os.path.join(script_dir, "image", "detect_aes.jpg")
    imageEncrypted = cv2.imread(output_image_path)
    key = bytes.fromhex(key)
    rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape
    rowOrig = rowEncrypted - 1
    encryptedBytes = imageEncrypted.tobytes()
    iv = b"MyFixedKey123456"
    imageOrigBytesSize = rowOrig * columnOrig * depthOrig
    paddedSize = (
        imageOrigBytesSize // AES.block_size + 1
    ) * AES.block_size - imageOrigBytesSize
    encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]
    cipher = (
        AES.new(key, AES.MODE_CBC, iv)
        if mode == AES.MODE_CBC
        else AES.new(key, AES.MODE_ECB)
    )
    decryptedImageBytesPadded = cipher.decrypt(encrypted)
    decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)
    decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(
        rowOrig, columnOrig, depthOrig
    )
    decrypted_image_path = os.path.join(save_folder_path, "nonsteg11_33_59decry.png")
    cv2.imwrite(decrypted_image_path, decryptedImage)
    cv2.waitKey()
    cv2.destroyAllWindows()


# text=input("ENTER THE KEY : ")
# key_digest = hashlib.sha256(text.encode()).digest()[:16]
# aes_key = key_digest.hex()
# decrypt(aes_key)
