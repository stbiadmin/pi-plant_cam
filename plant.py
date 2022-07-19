import numpy as np
import cv2
from fastiecm import fastiecm


def display(image, image_name, man=False):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    if man == True:
        cv2.namedWindow(image_name)
        cv2.imshow(image_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if man == True:
        for i in range (1,5):
            cv2.waitKey(1)
    

def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out

def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

    
def get_image():
    original = cv2.imread('../Mira_chronicles/test.png')
    return original

def main():
    original = get_image()
    display(original, 'Original')
    contrasted = contrast_stretch(original)
    display(contrasted, 'Contrasted original')
    cv2.imwrite('contrasted.png', contrasted)
    ndvi = calc_ndvi(contrasted)
    display(ndvi, 'NDVI')
    ndvi_contrasted = contrast_stretch(ndvi)
    display(ndvi_contrasted, 'NDVI Contrasted')
    cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)
    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    display(color_mapped_image, 'Color mapped')
    cv2.imwrite('color_mapped_image.png', color_mapped_image)
    

    
if __name__ == "__main__":
    main()