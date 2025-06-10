from libraries import libs
def change_channel(image, channel: str, value: int):
    """Change intensity of a specific channel ('R', 'G', 'B') by a given value."""
    image = image.copy()
    idx = {'B': 0, 'G': 1, 'R': 2}.get(channel.upper())
    if idx is None:
        raise ValueError("Invalid channel. Use 'R', 'G', or 'B'.")
    image[:, :, idx] = libs.np.clip(image[:, :, idx] + value, 0, 255)
    return image

def swap_channels(image, ch1: str, ch2: str):
    """Swap two channels, e.g. swap_channels(img, 'R', 'B')"""
    image = image.copy()
    idx1 = {'B': 0, 'G': 1, 'R': 2}.get(ch1.upper())
    idx2 = {'B': 0, 'G': 1, 'R': 2}.get(ch2.upper())
    if idx1 is None or idx2 is None:
        raise ValueError("Channels must be 'R', 'G', or 'B'.")
    image[:, :, [idx1, idx2]] = image[:, :, [idx2, idx1]]
    return image

def eliminate_channel(image, channel: str):
    """Set a specific channel ('R', 'G', 'B') to zero."""
    image = image.copy()
    idx = {'B': 0, 'G': 1, 'R': 2}.get(channel.upper())
    if idx is None:
        raise ValueError("Invalid channel. Use 'R', 'G', or 'B'.")
    image[:, :, idx] = 0
    return image
