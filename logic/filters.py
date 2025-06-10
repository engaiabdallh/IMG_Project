from libraries import libs

def average_filter(image, ksize=3):
    return libs.cv2.blur(image, (ksize, ksize))

def laplacian_filter(image):
    return libs.cv2.Laplacian(image, libs.cv2.CV_64F).astype(libs.np.uint8)

def max_filter(image, ksize=3):
    return libs.cv2.dilate(image, libs.np.ones((ksize, ksize), libs.np.uint8))

def min_filter(image, ksize=3):
    return libs.cv2.erode(image, libs.np.ones((ksize, ksize), libs.np.uint8))

def median_filter(image, ksize=3):
    return libs.cv2.medianBlur(image, ksize)

def mode_filter(image, ksize=3):
    if len(image.shape) != 2:
        raise ValueError("Mode filter expects a 2D grayscale image.")

    # Pad the image
    pad = ksize // 2
    padded = libs.np.pad(image, pad, mode='reflect')

    # View as sliding windows
    try:
        windows = libs.view_as_windows(padded, (ksize, ksize))
    except ValueError:
        raise ValueError("Invalid window shape — kernel too large for image.")

    H, W = image.shape
    result = libs.np.zeros((H, W), dtype=libs.np.uint8)

    for i in range(H):
        for j in range(W):
            patch = windows[i, j].flatten()
            result[i, j] = libs.stats.mode(patch, keepdims=False)[0]

    return result
