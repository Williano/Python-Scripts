"""
    Script: Averaging filter function
    Description: This program loads an image with salt and pepper noise in it
                 and applies a 3 x 3 averaging filter function to reduce the noise
"""

import cv2
import numpy as np


def load_image():

    # Read the image
    image = cv2.imread('Lena_noise.jpg', 0)

    # return image loaded
    return image


def filter_image_with_3x3_averaging(image):

    # Extracts the number of rows and columns in the image
    rows, columns = image.shape

    # Creates Averaging filter(3, 3) mask
    mask = np.ones([3, 3], dtype = int)
    mask = mask / 9

    # Combines the 3X3 mask over the image
    new_image = np.zeros([rows, columns])

    # Loop through the image.
    # For every 3X3 area, find the average of the pixels and
    # replace the ceter pixel by the average
    for row in range(1, rows-1):
        for column in range(1, columns-1):
            temp_mask = image[row-1, column-1]*\
                mask[0, 0]+image[row-1, column]*\
                    mask[0, 1]+image[row-1, column + 1]*\
                        mask[0, 2]+image[row, column-1]*\
                            mask[1, 0]+ image[row, column]*\
                                mask[1, 1]+image[row, column + 1]*\
                                    mask[1, 2]+image[row + 1, column-1]*\
                                        mask[2, 0]+image[row + 1, column]*\
                                            mask[2, 1]+image[row + 1, column + 1]\
                                                *mask[2, 2]

            new_image[row, column]= temp_mask

    # Convert the new image into numpy unsigned integer 8
    new_image = new_image.astype(np.uint8)

    # Write blurred image into new file called Lena blurred average
    cv2.imwrite('Lena_blurred_average.jpg', new_image)


def main():

    # Load image and save into loaded image variable
    loaded_image = load_image()

    # Filter the loaded image
    filter_image_with_3x3_averaging(loaded_image)


# Call the main function if the file is not being imported as a module
if __name__ == "__main__":
    main()