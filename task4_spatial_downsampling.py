import cv2
import numpy as np

def block_average(image, block_size):
    (h, w) = image.shape
    output = image.copy()

    for y in range(0, h - block_size + 1, block_size):
        for x in range(0, w - block_size + 1, block_size):
            block = image[y:y+block_size, x:x+block_size]
            avg = np.mean(block).astype(np.uint8)
            output[y:y+block_size, x:x+block_size] = avg
    return output

if __name__ == "__main__":
    image = cv2.imread("input.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

    for k in [3, 5, 7]:
        result = block_average(image, k)
        cv2.imwrite(f"results/task4_output_block_avg_{k}x{k}.jpg", result)
        print(f"Saved results/task4_output_block_avg_{k}x{k}.jpg")
        cv2.imshow(f"Block Average {k}x{k}", result)
        cv2.waitKey(0)
