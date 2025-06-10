from libraries import libs

def preprocess(image):
    gray = libs.cv2.cvtColor(image, libs.cv2.COLOR_BGR2GRAY)
    _, binary = libs.cv2.threshold(gray, 127, 255, libs.cv2.THRESH_BINARY)
    return binary

def dilation(binary_image, kernel_size=3):
    return libs.cv2.dilate(binary_image, libs.np.ones((kernel_size, kernel_size), libs.np.uint8))

def erosion(binary_image, kernel_size=3):
    return libs.cv2.erode(binary_image, libs.np.ones((kernel_size, kernel_size), libs.np.uint8))

def internal_boundary(binary_image, kernel_size=3):
    eroded = erosion(binary_image, kernel_size)
    return libs.cv2.subtract(binary_image, eroded)

def external_boundary(binary_image, kernel_size=3):
    dilated = dilation(binary_image, kernel_size)
    return libs.cv2.subtract(dilated, binary_image)

def morphological_gradient(binary_image, kernel_size=3):
    dilated = dilation(binary_image, kernel_size)
    eroded = erosion(binary_image, kernel_size)
    return libs.cv2.subtract(dilated, eroded)
