import pywt
import numpy as np
from PIL import Image
import os


def Decompression_Process(input_path, output_path):
    # Load compressed image
    image = Image.open(input_path)
    pixels = np.array(image)

    # Crop the input image to an even number of pixels
    pixels = pixels[: pixels.shape[0] // 2 * 2, : pixels.shape[1] // 2 * 2, :]

    # Perform inverse DWT on each color channel
    coeffs = []
    for channel in range(3):
        cA, (cH, cV, cD) = pywt.dwt2(pixels[:, :, channel], "coif2")
        coeffs.append((cA, (cH, cV, cD)))

    # Define compression ratio used during compression
    compression_ratio = 0.9

    # Threshold coefficients using the same threshold as during compression
    thresholded_coeffs = []
    for channel in range(3):
        cA, (cH, cV, cD) = coeffs[channel]
        threshold = np.max(np.abs((cH, cV, cD))) * compression_ratio / 2
        cH = pywt.threshold(cH, threshold, mode="hard")
        cV = pywt.threshold(cV, threshold, mode="hard")
        cD = pywt.threshold(cD, threshold, mode="hard")
        thresholded_coeffs.append((cA, (cH, cV, cD)))

    # Perform inverse DWT on the thresholded coefficients to obtain the decompressed image
    output_pixels = np.zeros_like(pixels)
    for channel in range(3):
        cA, (cH, cV, cD) = thresholded_coeffs[channel]
        output_pixels[:, :, channel] = pywt.idwt2((cA, (cH, cV, cD)), "coif2")

    # Add padding to match the size of the compressed image
    pad_width = [
        (0, pixels.shape[0] - output_pixels.shape[0]),
        (0, pixels.shape[1] - output_pixels.shape[1]),
        (0, 0),
    ]
    output_pixels = np.pad(output_pixels, pad_width, mode="edge")

    # Save the decompressed image
    output_path = os.path.join(output_path, "decompressed.jpg")
    output_image = Image.fromarray(output_pixels.astype("uint8"))
    output_image.save(output_path)


# Decompression_DWT()
