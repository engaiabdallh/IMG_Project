import customtkinter as ctk
import cv2
import numpy as np

# main.py
from ui.app_layout import ImageProcessingApp
from tkinter import filedialog

# app_layout.py
from PIL import Image, ImageTk

from ui.point_ops_ui import build_point_ops_tab
from logic.point_ops import add_brightness, subtract_brightness, complement, divide_brightness, multiple_brightness

from ui.color_ops_ui import build_color_ops_tab
from logic.color_ops import change_channel, swap_channels, eliminate_channel

from ui.histogram_ui import build_histogram_tab
from logic.histograms import histogram_stretching, histogram_equalization

from ui.filters_ui import build_filters_tab
from logic.filters import average_filter, laplacian_filter, max_filter, min_filter, median_filter, mode_filter

from ui.restoration_ui import build_restoration_tab
from logic.restoration import add_salt_pepper_noise, average_filter, median_filter, outlier_method, add_gaussian_noise, image_averaging

from ui.segmentation_ui import build_segmentation_tab
from logic.segmentation import basic_global_threshold, automatic_threshold, adaptive_threshold

from ui.morphology_ui import build_morphology_tab
from logic.morphology import dilation, erosion, internal_boundary, external_boundary, morphological_gradient

from ui.edge_detection_ui import build_edge_detection_tab
from logic.edge_detection import sobel_edge_detector, roberts, prewitt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# filters.py
from scipy import stats
from skimage.util.shape import view_as_windows