from libraries import libs

def build_histogram_tab(tab, app):
    # Button Row for Histogram Operations
    app.hist_button_frame = libs.ctk.CTkFrame(tab)
    app.hist_button_frame.pack(pady=20)

    libs.ctk.CTkButton(app.hist_button_frame, text="Stretch Histogram", command=app.apply_histogram_stretch).pack(side="left", padx=10)
    libs.ctk.CTkButton(app.hist_button_frame, text="Equalize Histogram", command=app.apply_histogram_equalize).pack(side="left", padx=10)
