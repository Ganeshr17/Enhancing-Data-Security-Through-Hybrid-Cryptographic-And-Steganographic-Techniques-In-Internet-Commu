import pywt
import numpy as np
from PIL import Image
import os


def Compression_Process(path, script_dir):
    # Load image
    image = Image.open(path)
    pixels = np.array(image)

    # Perform DWT on each color channel
    coeffs = []
    for channel in range(3):
        cA, (cH, cV, cD) = pywt.dwt2(pixels[:, :, channel], "haar")
        coeffs.append((cA, (cH, cV, cD)))

    # Define compression ratio
    compression_ratio = 0.9

    # Threshold coefficients
    thresholded_coeffs = []
    for channel in range(3):
        cA, (cH, cV, cD) = coeffs[channel]
        threshold = np.max(np.abs((cH, cV, cD))) * compression_ratio / 2
        cH = pywt.threshold(cH, threshold, mode="hard")
        cV = pywt.threshold(cV, threshold, mode="hard")
        cD = pywt.threshold(cD, threshold, mode="hard")
        thresholded_coeffs.append((cA, (cH, cV, cD)))

    # Perform inverse DWT
    output_pixels = np.zeros_like(pixels)
    for channel in range(3):
        cA, (cH, cV, cD) = thresholded_coeffs[channel]
        channel_output = pywt.idwt2((cA, (cH, cV, cD)), "haar")
        channel_output = channel_output[
            : pixels.shape[0], : pixels.shape[1]
        ]  # Crop to match original image size
        output_pixels[:, :, channel] = channel_output

    # Save compressed image
    output_image = Image.fromarray(output_pixels.astype("uint8"))
    output_image_path = os.path.join(script_dir, "image", "compressed.jpg")
    output_image.save(output_image_path)
    return output_image
