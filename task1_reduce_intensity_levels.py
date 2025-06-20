import cv2
import numpy as np

def reduce_intensity_levels(image, levels):
    factor = 256 // levels
    reduced = (image // factor) * factor
    return reduced

if __name__ == "__main__":
    image = cv2.imread("input.jpg")
    levels = int(input("Enter intensity levels (2, 4, 8, ..., 256): "))
    
    if levels not in [2 ** i for i in range(1, 9)]:
        print("Please enter a valid power-of-2 between 2 and 256")
    else:
        reduced_image = reduce_intensity_levels(image, levels)
        cv2.imwrite(f"results/task1_output_reduced_{levels}_levels.jpg", reduced_image)
        print(f"Saved output as output_reduced_{levels}_levels.jpg")
        cv2.imshow("Reduced Intensity Levels", reduced_image)
        cv2.waitKey(0)