from libraries import libs

def add_salt_pepper_noise(image, amount=0.02):
    noisy = image.copy()
    num_pixels = image.shape[0] * image.shape[1]
    num_salt = int(libs.np.ceil(amount * num_pixels * 0.5))
    num_pepper = int(libs.np.ceil(amount * num_pixels * 0.5))

    coords = [libs.np.random.randint(0, i, num_salt) for i in image.shape[:2]]
    if len(image.shape) == 2:
        noisy[coords[0], coords[1]] = 255
    else:
        noisy[coords[0], coords[1]] = [255, 255, 255]


    coords = [libs.np.random.randint(0, i, num_pepper) for i in image.shape[:2]]
    if len(image.shape) == 2:
        noisy[coords[0], coords[1]] = 0
    else:
        noisy[coords[0], coords[1]] = [0, 0, 0]

    return noisy

def average_filter(image, ksize=3):
    return libs.cv2.blur(image, (ksize, ksize))

def median_filter(image, ksize=3):
    return libs.cv2.medianBlur(image, ksize)

def outlier_method(image, ksize=3):
    median = libs.cv2.medianBlur(image, ksize)
    diff = libs.cv2.absdiff(image, median)
    mask = diff > 50
    image[mask] = median[mask]
    return image

def add_gaussian_noise(image, mean=0, std=25):
    noise = libs.np.random.normal(mean, std, image.shape).astype(libs.np.float32)
    noisy = image.astype(libs.np.float32) + noise
    noisy = libs.np.clip(noisy, 0, 255).astype(libs.np.uint8)
    return noisy

def image_averaging(images):
    return libs.np.mean(images, axis=0).astype(libs.np.uint8)
