from libraries import libs

class ImageProcessingApp(libs.ctk.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"project\assets\logo.ico")
        self.title("Image Processing Project")
        self.geometry("1100x750")

        self.processed_image = None  # live edited image
        self.input_image = None
        self.input_photo = None
        self.result_photo = None

        # === TOP: Shared Display Area ===
        self.display_frame = libs.ctk.CTkFrame(self)
        self.display_frame.pack(side="top", pady=15)

        self.display_inner_frame = libs.ctk.CTkFrame(self.display_frame)
        self.display_inner_frame.pack(anchor="center")

        self.left_display = libs.ctk.CTkFrame(self.display_inner_frame)
        self.left_display.pack(side="left", padx=30)

        self.right_display = libs.ctk.CTkFrame(self.display_inner_frame)
        self.right_display.pack(side="left", padx=30)

        self.input_canvas = libs.ctk.CTkLabel(self.left_display, text="Original Image")
        self.input_canvas.pack(pady=5)

        self.input_hist_frame = libs.ctk.CTkFrame(self.left_display, width=350, height=200)
        self.input_hist_frame.pack(pady=5)

        self.result_canvas = libs.ctk.CTkLabel(self.right_display, text="Processed Image")
        self.result_canvas.pack(pady=5)

        self.result_hist_frame = libs.ctk.CTkFrame(self.right_display, width=350, height=200)
        self.result_hist_frame.pack(pady=5)

        # === BOTTOM AREA (Sidebar + Tabs) ===
        self.bottom_frame = libs.ctk.CTkFrame(self)
        self.bottom_frame.pack(fill="both", expand=True)

        self.sidebar = libs.ctk.CTkFrame(self.bottom_frame, width=200)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.theme_switch = libs.ctk.CTkSwitch(self.sidebar, text="Dark Mode", command=self.toggle_theme)
        self.theme_switch.select()  # Default: dark
        self.theme_switch.pack(pady=5)

        self.upload_btn = libs.ctk.CTkButton(self.sidebar, text="Upload Image", command=self.load_image)
        self.upload_btn.pack(pady=10)

        self.show_hist_checkbox = libs.ctk.CTkCheckBox(
            self.sidebar, text="Show Histogram", command=self.toggle_histogram
        )
        self.show_hist_checkbox.pack(pady=5)

        self.reset_btn = libs.ctk.CTkButton(self.sidebar, text="Reset Image", command=self.reset_image)
        self.reset_btn.pack(pady=10)

        self.save_btn = libs.ctk.CTkButton(self.sidebar, text="Save Image", command=self.save_image)
        self.save_btn.pack(pady=5)

        self.gray_convert_btn = libs.ctk.CTkButton(
            self.sidebar, text="Convert to Grayscale", command=self.convert_to_grayscale
        )
        self.gray_convert_btn.pack(pady=5)


        self.tabview = libs.ctk.CTkTabview(self.bottom_frame)
        self.tabview.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        self.tabs = {
            "Point Ops": self.tabview.add("Point Ops"),
            "Color Ops": self.tabview.add("Color Ops"),
            "Histogram": self.tabview.add("Histogram"),
            "Filters": self.tabview.add("Filters"),
            "Restoration": self.tabview.add("Restoration"),
            "Segmentation": self.tabview.add("Segmentation"),
            "Morphology": self.tabview.add("Morphology"),
            "Edge Detection": self.tabview.add("Edge Detection")
            }
        
        libs.build_point_ops_tab(self.tabs["Point Ops"], self)

        libs.build_color_ops_tab(self.tabs["Color Ops"], self)

        libs.build_histogram_tab(self.tabs["Histogram"], self)

        libs.build_filters_tab(self.tabs["Filters"], self)

        libs.build_restoration_tab(self.tabs["Restoration"], self)

        libs.build_segmentation_tab(self.tabs["Segmentation"], self)

        libs.build_morphology_tab(self.tabs["Morphology"], self)

        libs.build_edge_detection_tab(self.tabs["Edge Detection"], self)

    def toggle_theme(self):
        mode = "dark" if self.theme_switch.get() else "light"
        libs.ctk.set_appearance_mode(mode)

    def load_image(self):
        file_path = libs.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.input_image = libs.Image.open(file_path).convert("RGB")
            self.cv_image = libs.cv2.cvtColor(libs.np.array(self.input_image), libs.cv2.COLOR_RGB2BGR)
            self.processed_image = self.cv_image.copy()

            resized = self.input_image.resize((300, 300))
            self.input_photo = libs.ImageTk.PhotoImage(resized)
            self.input_canvas.configure(image=self.input_photo)
            self.input_canvas.image = self.input_photo

            self.result_canvas.configure(image=None, text="Processed Image")
            self.clear_histogram(target="result")
        
        if self.show_hist_checkbox.get():
           self.show_histogram(self.cv_image, target="input")
        else:
            self.clear_histogram(target="input")

    def show_cv_image(self, cv_img):
        rgb = libs.cv2.cvtColor(cv_img, libs.cv2.COLOR_BGR2RGB)
        pil_img = libs.Image.fromarray(rgb).resize((300, 300))
        self.result_photo = libs.ImageTk.PhotoImage(pil_img)
        self.result_canvas.configure(image=self.result_photo)
        self.result_canvas.image = self.result_photo

        if self.show_hist_checkbox.get():
            self.show_histogram(cv_img, target="result")
        else:
            self.clear_histogram(target="result")
        
    def display_result(self, image):
        self.processed_image = image
        resized = image.resize((300, 300))
        self.result_photo = libs.ImageTk.PhotoImage(resized)
        self.result_canvas.configure(image=self.result_photo)
        self.result_canvas.image = self.result_photo

    def reset_image(self):
        if self.input_image:
            self.processed_image = self.cv_image.copy()
            self.show_cv_image(self.processed_image)

            resized = self.input_image.resize((300, 300))
            self.input_photo = libs.ImageTk.PhotoImage(resized)
            self.input_canvas.configure(image=self.input_photo)
            self.input_canvas.image = self.input_photo
    
    def save_image(self):
        if self.processed_image is not None:
            file_path = libs.filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
            )
            if file_path:
                libs.cv2.imwrite(file_path, self.processed_image)

    def convert_to_grayscale(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)

            gray_bgr = libs.cv2.cvtColor(gray, libs.cv2.COLOR_GRAY2BGR)

            self.processed_image = gray_bgr

            self.show_cv_image(self.processed_image)

            pil_img = libs.Image.fromarray(libs.cv2.cvtColor(gray_bgr, libs.cv2.COLOR_BGR2RGB)).resize((300, 300))
            self.input_photo = libs.ImageTk.PhotoImage(pil_img)
            self.input_canvas.configure(image=self.input_photo)
            self.input_canvas.image = self.input_photo

    """Point Operation Functions"""
    def apply_complement(self):
        if self.processed_image is not None:
            value = self.get_entry_value()
            result = libs.complement(self.processed_image)
            self.processed_image = result
            self.show_cv_image(result)
    
    def get_entry_value(self) -> int:
        try:
            return int(self.value_entry.get())
        except ValueError:
            return 0  # fallback if input is invalid or empty

    def apply_add(self):
        if self.processed_image is not None:
            value = self.get_entry_value()
            result = libs.add_brightness(self.processed_image, value)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_subtract(self):
        if self.processed_image is not None:
            value = self.get_entry_value()
            result = libs.subtract_brightness(self.processed_image, value)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_divide(self):
        if self.processed_image is not None:
            value = self.get_entry_value()
            result = libs.divide_brightness(self.processed_image, value)
            self.processed_image = result
            self.show_cv_image(result)
    
    def apply_multiply(self):
        if self.processed_image is not None:
            value = self.get_entry_value()
            result = libs.multiple_brightness(self.processed_image, value)
            self.processed_image = result
            self.show_cv_image(result)

    """Color Operation Functions"""
    def apply_change_channel(self):
        if self.processed_image is not None:
            try:
                val = int(self.channel_value_entry.get())
                channel = self.channel_selector.get()
                result = libs.change_channel(self.processed_image.copy(), channel, val)
                self.processed_image = result
                self.show_cv_image(result)
            except Exception as e:
                print("Error changing channel:", e)

    def apply_swap_channels(self):
        if self.processed_image is not None:
            ch1 = self.swap_from.get()
            ch2 = self.swap_to.get()
            result = libs.swap_channels(self.processed_image.copy(), ch1, ch2)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_eliminate_channel(self):
        if self.processed_image is not None:
            channel = self.elim_selector.get()
            result = libs.eliminate_channel(self.processed_image.copy(), channel)
            self.processed_image = result
            self.show_cv_image(result)


    """Histograms"""
    def apply_histogram_stretch(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            stretched = libs.histogram_stretching(gray)
            result = libs.cv2.cvtColor(stretched, libs.cv2.COLOR_GRAY2BGR)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_histogram_equalize(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            equalized = libs.histogram_equalization(gray)
            result = libs.cv2.cvtColor(equalized, libs.cv2.COLOR_GRAY2BGR)
            self.processed_image = result
            self.show_cv_image(result)

    """Filters"""
    def get_kernel_size(self):
        try:
            k = int(self.kernel_entry.get())
            if k % 2 == 0:
                k += 1  # auto fix to odd
            return k
        except:
            return 3

    def apply_avg_filter(self):
        if self.processed_image is not None:
            ksize = self.get_kernel_size()
            result = libs.average_filter(self.processed_image, ksize)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_laplacian_filter(self):
        if self.processed_image is not None:
            result = libs.laplacian_filter(self.processed_image)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_max_filter(self):
        if self.processed_image is not None:
            ksize = self.get_kernel_size()
            result = libs.max_filter(self.processed_image, ksize)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_min_filter(self):
        if self.processed_image is not None:
            ksize = self.get_kernel_size()
            result = libs.min_filter(self.processed_image, ksize)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_median_filter(self):
        if self.processed_image is not None:
            ksize = self.get_kernel_size()
            result = libs.median_filter(self.processed_image, ksize)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_mode_filter(self):
        if self.processed_image is not None:
            ksize = self.get_kernel_size()

            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)

            try:
                filtered = libs.mode_filter(gray, ksize)
                result = libs.cv2.cvtColor(filtered, libs.cv2.COLOR_GRAY2BGR)
                self.processed_image = result
                self.show_cv_image(result)
            except ValueError as e:
                print("Mode filter failed:", e)

    """Restoration"""
    def add_salt_pepper(self):
        if self.processed_image is not None:
            result = libs.add_salt_pepper_noise(self.processed_image.copy())
            self.processed_image = result
            self.show_cv_image(result)

    def remove_sp_avg(self):
        if self.processed_image is not None:
            result = libs.average_filter(self.processed_image.copy(), 3)
            self.processed_image = result
            self.show_cv_image(result)

    def remove_sp_median(self):
        if self.processed_image is not None:
            result = libs.median_filter(self.processed_image.copy(), 3)
            self.processed_image = result
            self.show_cv_image(result)

    def remove_sp_outlier(self):
        if self.processed_image is not None:
            result = libs.outlier_method(self.processed_image.copy(), 3)
            self.processed_image = result
            self.show_cv_image(result)

    def add_gaussian(self):
        if self.processed_image is not None:
            result = libs.add_gaussian_noise(self.processed_image.copy())
            self.processed_image = result
            self.show_cv_image(result)

    def remove_gaussian_avg_filter(self):
        if self.processed_image is not None:
            result = libs.average_filter(self.processed_image.copy(), ksize=3)
            self.processed_image = result
            self.show_cv_image(result)

    def remove_gaussian_averaging(self):
        if self.processed_image is not None:
            # Create 5 noisy versions
            noisy_images = [libs.add_gaussian_noise(self.processed_image.copy()) for _ in range(5)]
            result = libs.image_averaging(noisy_images)
            self.processed_image = result
            self.show_cv_image(result)

    """Segmentations"""
    def get_threshold_value(self) -> int:
        try:
            return int(self.threshold_entry.get())
        except ValueError:
            return 127  # Default threshold

    def apply_global_threshold(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            thresh_val = self.get_threshold_value()
            result = libs.basic_global_threshold(gray, thresh_val)
            self.processed_image = libs.cv2.cvtColor(result, libs.cv2.COLOR_GRAY2BGR)
            self.show_cv_image(self.processed_image)

    def apply_otsu_threshold(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            result = libs.automatic_threshold(gray)
            self.processed_image = libs.cv2.cvtColor(result, libs.cv2.COLOR_GRAY2BGR)
            self.show_cv_image(self.processed_image)

    def apply_adaptive_threshold(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            result = libs.adaptive_threshold(gray)
            self.processed_image = libs.cv2.cvtColor(result, libs.cv2.COLOR_GRAY2BGR)
            self.show_cv_image(self.processed_image)

    """Morphological"""
    def get_morph_kernel(self) -> int:
        try:
            return int(self.morph_kernel_entry.get())
        except ValueError:
            return 3

    def apply_dilation(self):
        if self.processed_image is not None:
            k = self.get_morph_kernel()
            result = libs.dilation(self.processed_image, k)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_erosion(self):
        if self.processed_image is not None:
            k = self.get_morph_kernel()
            result = libs.erosion(self.processed_image, k)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_internal_boundary(self):
        if self.processed_image is not None:
            result = libs.internal_boundary(self.processed_image)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_external_boundary(self):
        if self.processed_image is not None:
            result = libs.external_boundary(self.processed_image)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_morph_gradient(self):
        if self.processed_image is not None:
            result = libs.morphological_gradient(self.processed_image)
            self.processed_image = result
            self.show_cv_image(result)

    """Edge detection"""
    def apply_sobel_edge(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            edges = libs.sobel_edge_detector(gray)
            result = libs.cv2.cvtColor(edges, libs.cv2.COLOR_GRAY2BGR)
            self.processed_image = result
            self.show_cv_image(result)

    def apply_roberts(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            edges = libs.roberts(gray)  # use correct function name here
            result = libs.cv2.cvtColor(edges, libs.cv2.COLOR_GRAY2BGR)
            self.processed_image = result
            self.show_cv_image(result)
    
    def apply_prewitt(self):
        if self.processed_image is not None:
            gray = libs.cv2.cvtColor(self.processed_image, libs.cv2.COLOR_BGR2GRAY)
            edges = libs.prewitt(gray)  # use correct function name here
            result = libs.cv2.cvtColor(edges, libs.cv2.COLOR_GRAY2BGR)
            self.processed_image = result
            self.show_cv_image(result)

    """================================================================="""

    def show_histogram(self, image, target="input"):
        # Clear previous histogram
        self.clear_histogram(target)

        gray = libs.cv2.cvtColor(image, libs.cv2.COLOR_BGR2GRAY)
        hist = libs.cv2.calcHist([gray], [0], None, [256], [0, 256])

        fig = libs.Figure(figsize=(4.5, 2.2), dpi=100)  # 👈 Bigger size
        ax = fig.add_subplot(111)
        ax.plot(hist, color='black')
        ax.set_title("Histogram")
        ax.set_xlim([0, 256])
        ax.set_xticks([])
        ax.set_yticks([])

        canvas = libs.FigureCanvasTkAgg(fig, master=self.input_hist_frame if target == "input" else self.result_hist_frame)
        canvas.draw()

        if target == "input":
            self.input_hist_canvas = canvas
        else:
            self.result_hist_canvas = canvas

        canvas.get_tk_widget().pack()

    def clear_histogram(self, target="result"):
        if target == "result" and hasattr(self, "result_hist_canvas"):
            self.result_hist_canvas.get_tk_widget().destroy()
            del self.result_hist_canvas
        elif target == "input" and hasattr(self, "input_hist_canvas"):
            self.input_hist_canvas.get_tk_widget().destroy()
            del self.input_hist_canvas

    def toggle_histogram(self):
        if self.cv_image is not None:
            if self.show_hist_checkbox.get():
                self.show_histogram(self.cv_image, target="input")
                self.show_histogram(self.processed_image, target="result")
            else:
                self.clear_histogram("input")
                self.clear_histogram("result")