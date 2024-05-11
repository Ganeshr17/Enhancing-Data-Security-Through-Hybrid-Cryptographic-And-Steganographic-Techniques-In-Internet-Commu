from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np

def ssim_indx(cvr_path,steg_path):
    cvr_path = cv2.imread(cvr_path)
    steg_path= cv2.imread(steg_path)
    gray_img1 = cv2.cvtColor(cvr_path, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(steg_path, cv2.COLOR_BGR2GRAY)
    ssim_value = ssim(gray_img1, gray_img2)
    return ssim_value
def psnr_indx(cvr_path,stego_path):
    global psnr
    stego_path = cv2.imread(stego_path)
    cvr_path = cv2.imread(cvr_path)
    mse = ((stego_path - cvr_path) ** 2).mean()
    if mse == 0:
        psnr = float('inf')
    else:
        max_pixel_value = 255.0
        psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr
