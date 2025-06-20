import cv2
import numpy as np

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return rotated

if __name__ == "__main__":
    image = cv2.imread("input.jpg")

    for angle in [45, 90]:
        rotated = rotate_image(image, angle)
        cv2.imwrite(f"results/task3_output_rotated_{angle}.jpg", rotated)
        print(f"Saved results/task3_output_rotated_{angle}.jpg")
        cv2.imshow(f"Rotated {angle} degrees", rotated)
        cv2.waitKey(0)