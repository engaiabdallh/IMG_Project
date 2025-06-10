from libraries import libs

def build_morphology_tab(tab, app):
    # Kernel Size Entry
    app.morph_kernel_entry = libs.ctk.CTkEntry(tab, placeholder_text="Kernel Size (e.g. 3)")
    app.morph_kernel_entry.pack(pady=(10, 5))

    # Button Frame
    app.morph_button_frame = libs.ctk.CTkFrame(tab)
    app.morph_button_frame.pack(pady=10)

    libs.ctk.CTkButton(app.morph_button_frame, text="Dilation", command=app.apply_dilation).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.morph_button_frame, text="Erosion", command=app.apply_erosion).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.morph_button_frame, text="Internal Boundary", command=app.apply_internal_boundary).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.morph_button_frame, text="External Boundary", command=app.apply_external_boundary).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.morph_button_frame, text="Morph Gradient", command=app.apply_morph_gradient).pack(side="left", padx=5)
