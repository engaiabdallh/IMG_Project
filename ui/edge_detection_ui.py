from libraries import libs

def build_edge_detection_tab(tab, app):
    app.edge_button_frame = libs.ctk.CTkFrame(tab)
    app.edge_button_frame.pack(pady=20)

    libs.ctk.CTkButton(app.edge_button_frame, text="Sobel Detection", command=app.apply_sobel_edge).pack(side="left", padx=10)
    libs.ctk.CTkButton(app.edge_button_frame, text="Roberts Detection", command=app.apply_roberts).pack(side="left", padx=10)
    libs.ctk.CTkButton(app.edge_button_frame, text="Prewitt Detection", command=app.apply_prewitt).pack(side="left", padx=10)