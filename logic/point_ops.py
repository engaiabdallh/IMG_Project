from libraries import libs

def complement(image):
    return libs.cv2.bitwise_not(image)

def add_brightness(image: libs.np.ndarray, value: int) -> libs.np.ndarray:
    return libs.cv2.add(image, value)

def subtract_brightness(image: libs.np.ndarray, value: int) -> libs.np.ndarray:
    return libs.cv2.subtract(image, value)

def divide_brightness(image: libs.np.ndarray, value: int) -> libs.np.ndarray:
    return libs.np.clip(image // max(1, value), 0, 255).astype(libs.np.uint8)

def multiple_brightness(image: libs.np.ndarray, value: int) -> libs.np.ndarray:
    return libs.np.clip(image * max(1, value), 0, 255).astype(libs.np.uint8)