from libraries import libs

def build_restoration_tab(tab, app):
    # === Row 1: Add Salt & Pepper (Centered) ===
    app.salt_papper_frame = libs.ctk.CTkFrame(tab)
    app.salt_papper_frame.pack(pady=20)

    row1 = libs.ctk.CTkFrame(app.salt_papper_frame)
    row1.pack(pady=10)
    libs.ctk.CTkButton(row1, text="Add Salt & Pepper", command=app.add_salt_pepper).pack()

    # === Row 2: Remove Salt & Pepper Filters (Same row) ===
    row2 = libs.ctk.CTkFrame(app.salt_papper_frame)
    row2.pack(pady=10)
    libs.ctk.CTkButton(row2, text="Remove (Median)", command=app.remove_sp_median).pack(side="left", padx=5)
    libs.ctk.CTkButton(row2, text="Remove (Avg Filter)", command=app.remove_sp_avg).pack(side="left", padx=5)
    libs.ctk.CTkButton(row2, text="Remove (Outlier)", command=app.remove_sp_outlier).pack(side="left", padx=5)

    # === Row 3: Add Gaussian Noise (Centered) ===
    app.gaussian_noise_frame = libs.ctk.CTkFrame(tab)
    app.gaussian_noise_frame.pack(pady=20)

    row3 = libs.ctk.CTkFrame(app.gaussian_noise_frame)
    row3.pack(pady=10)
    libs.ctk.CTkButton(row3, text="Add Gaussian Noise", command=app.add_gaussian).pack()

    # === Row 4: Remove Gaussian Noise (Same row) ===
    row4 = libs.ctk.CTkFrame(app.gaussian_noise_frame)
    row4.pack(pady=10)
    libs.ctk.CTkButton(row4, text="Remove Gaussian (Image Averaging)", command=app.remove_gaussian_averaging).pack(side="left", padx=5)
    libs.ctk.CTkButton(row4, text="Remove Gaussian (Avg Filter)", command=app.remove_gaussian_avg_filter).pack(side="left", padx=5)
