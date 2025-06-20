import cv2
import numpy as np

def apply_mean_filter(image, ksize):
    return cv2.blur(image, (ksize, ksize))

if __name__ == "__main__":
    image = cv2.imread("input.jpg")

    for k in [3, 10, 20]:
        blurred = apply_mean_filter(image, k)
        cv2.imwrite(f"results/task2_output_blur_{k}x{k}.jpg", blurred)
        print(f"Saved results/task2_output_blur_{k}x{k}.jpg")
