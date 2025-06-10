from libraries import libs

def basic_global_threshold(gray_img, thresh_val=127):
    _, result = libs.cv2.threshold(gray_img, thresh_val, 255, libs.cv2.THRESH_BINARY)
    return result

def automatic_threshold(gray_img):
    _, result = libs.cv2.threshold(gray_img, 0, 255, libs.cv2.THRESH_BINARY + libs.cv2.THRESH_OTSU)
    return result

def adaptive_threshold(gray_img):
    return libs.cv2.adaptiveThreshold(gray_img, 255, libs.cv2.ADAPTIVE_THRESH_MEAN_C,
                                 libs.cv2.THRESH_BINARY, 11, 2)