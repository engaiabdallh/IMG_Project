from libraries import libs

def sobel_edge_detector(image):
    grad_x = libs.cv2.Sobel(image, libs.cv2.CV_64F, 1, 0, ksize=3)
    grad_y = libs.cv2.Sobel(image, libs.cv2.CV_64F, 0, 1, ksize=3)
    magnitude = libs.cv2.magnitude(grad_x, grad_y)
    return libs.cv2.convertScaleAbs(magnitude)

def prewitt(image):
    kernelx = libs.np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]], dtype=libs.np.float32)
    
    kernely = libs.np.array([[-1, -1, -1],
                             [ 0,  0,  0],
                             [ 1,  1,  1]], dtype=libs.np.float32)

    grad_x = libs.cv2.filter2D(image, libs.cv2.CV_64F, kernelx)
    grad_y = libs.cv2.filter2D(image, libs.cv2.CV_64F, kernely)
    magnitude = libs.cv2.magnitude(grad_x, grad_y)
    return libs.cv2.convertScaleAbs(magnitude)

def roberts(image):
    kernelx = libs.np.array([[-1, 0],
                             [0,  1]], dtype=libs.np.float32)
    
    kernely = libs.np.array([[0, -1],
                             [1,  0]], dtype=libs.np.float32)

    grad_x = libs.cv2.filter2D(image, libs.cv2.CV_64F, kernelx)
    grad_y = libs.cv2.filter2D(image, libs.cv2.CV_64F, kernely)
    magnitude = libs.cv2.magnitude(grad_x, grad_y)
    return libs.cv2.convertScaleAbs(magnitude)
