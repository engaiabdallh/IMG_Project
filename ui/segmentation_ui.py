from libraries import libs

def build_segmentation_tab(tab, app):
    # Entry for manual threshold value
    app.threshold_entry = libs.ctk.CTkEntry(tab, placeholder_text="Threshold Value (0-255)")
    app.threshold_entry.pack(pady=(10, 5))

    # Button Row
    app.seg_button_frame = libs.ctk.CTkFrame(tab)
    app.seg_button_frame.pack(pady=10)

    libs.ctk.CTkButton(app.seg_button_frame, text="Basic Global Threshold", command=app.apply_global_threshold).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.seg_button_frame, text="Automatic (Otsu)", command=app.apply_otsu_threshold).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.seg_button_frame, text="Adaptive Threshold", command=app.apply_adaptive_threshold).pack(side="left", padx=5)
