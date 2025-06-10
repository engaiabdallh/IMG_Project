from libraries import libs

def build_color_ops_tab(tab, app):

    # --- Change Channel ---
    app.color_control_frame = libs.ctk.CTkFrame(tab)
    app.color_control_frame.pack(pady=10)

    app.channel_selector = libs.ctk.CTkOptionMenu(
        app.color_control_frame, values=["B", "G", "R"]
    )
    app.channel_selector.set("B")
    app.channel_selector.pack(side="left", padx=5)

    app.channel_value_entry = libs.ctk.CTkEntry(
        app.color_control_frame, placeholder_text="Enter value"
    )
    app.channel_value_entry.pack(side="left", padx=5)

    libs.ctk.CTkButton(
        app.color_control_frame, text="Change Channel",
        command=app.apply_change_channel
    ).pack(side="left", padx=5)

    # --- Swap Channels ---
    app.swap_frame = libs.ctk.CTkFrame(tab)
    app.swap_frame.pack(pady=10)

    app.swap_from = libs.ctk.CTkOptionMenu(app.swap_frame, values=["B", "G", "R"])
    app.swap_from.set("B")
    app.swap_from.pack(side="left", padx=5)

    app.swap_to = libs.ctk.CTkOptionMenu(app.swap_frame, values=["B", "G", "R"])
    app.swap_to.set("G")
    app.swap_to.pack(side="left", padx=5)

    libs.ctk.CTkButton(
        app.swap_frame, text="Swap Channels",
        command=app.apply_swap_channels
    ).pack(side="left", padx=5)

    # --- Eliminate Channel ---
    app.elim_frame = libs.ctk.CTkFrame(tab)
    app.elim_frame.pack(pady=10)

    app.elim_selector = libs.ctk.CTkOptionMenu(app.elim_frame, values=["B", "G", "R"])
    app.elim_selector.set("B")
    app.elim_selector.pack(side="left", padx=5)

    libs.ctk.CTkButton(
        app.elim_frame, text="Eliminate Channel",
        command=app.apply_eliminate_channel
    ).pack(side="left", padx=5)
