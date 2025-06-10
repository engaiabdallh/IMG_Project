from libraries import libs

def build_point_ops_tab(tab, app):
    # Entry for dynamic value
    app.value_entry = libs.ctk.CTkEntry(tab, placeholder_text="Enter value")
    app.value_entry.pack(pady=(10, 0))

    # Button Row
    app.button_frame = libs.ctk.CTkFrame(tab)
    app.button_frame.pack(pady=10)

    libs.ctk.CTkButton(app.button_frame, text="Complement", command=app.apply_complement).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.button_frame, text="Add", command=app.apply_add).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.button_frame, text="Subtract", command=app.apply_subtract).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.button_frame, text="Divide", command=app.apply_divide).pack(side="left", padx=5)
    libs.ctk.CTkButton(app.button_frame, text="Multiple", command=app.apply_multiply).pack(side="left", padx=5)