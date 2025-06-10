from libraries import libs

def build_filters_tab(tab, app):
    # Entry to change kernel size
    app.kernel_entry = libs.ctk.CTkEntry(tab, placeholder_text="Kernel Size (e.g. 3)")
    app.kernel_entry.pack(pady=(10, 5))

    # Button Row
    app.filters_button_frame = libs.ctk.CTkFrame(tab)
    app.filters_button_frame.pack(pady=10)

    libs.ctk.CTkButton(app.filters_button_frame, text="Average Filter", command=app.apply_avg_filter).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.filters_button_frame, text="Laplacian Filter", command=app.apply_laplacian_filter).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.filters_button_frame, text="Max Filter", command=app.apply_max_filter).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.filters_button_frame, text="Min Filter", command=app.apply_min_filter).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.filters_button_frame, text="Median Filter", command=app.apply_median_filter).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.filters_button_frame, text="Mode Filter", command=app.apply_mode_filter).pack(side="left", padx=5)
