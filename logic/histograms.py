from libraries import libs

def histogram_stretching(gray_img):
    min_val = libs.np.min(gray_img)
    max_val = libs.np.max(gray_img)

    if max_val == min_val:
        return libs.np.zeros_like(gray_img)

    stretched = ((gray_img - min_val) * 255.0 / (max_val - min_val)).astype(libs.np.uint8)
    return stretched

def histogram_equalization(gray_img):
    return libs.cv2.equalizeHist(gray_img)