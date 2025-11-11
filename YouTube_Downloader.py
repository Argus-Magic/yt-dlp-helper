import flet as ft
import subprocess
import os
from tkinter import filedialog, Tk

def main(page: ft.Page):
    page.title = "Audio Downloader"
    page.window_width = 500
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Classic Windows XP/7 color scheme
    page.bgcolor = "#ECE9D8"  # Classic beige/gray background
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#0A246A",  # Classic blue
            on_primary="#FFFFFF",
            surface="#D4D0C8",  # Windows gray
            on_surface="#000000",
        )
    )

    # Hide tkinter root window (for folder picker)
    Tk().withdraw()

    # Classic button style
    def create_classic_button(text, on_click=None, width=120, height=28):
        return ft.Container(
            content=ft.Text(
                text, 
                size=11, 
                weight=ft.FontWeight.BOLD,
                color="black"
            ),
            width=width,
            height=height,
            alignment=ft.alignment.center,
            bgcolor="#ECE9D8",
            border=ft.border.all(2, "white"),
            border_radius=0,  # Sharp corners
            padding=ft.padding.all(0),
            margin=ft.margin.all(1),
            on_click=on_click,
            # 3D effect using borders
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#FFFFFF", "#D4D0C8", "#808080"]
            )
        )

    # Classic text field style
    def create_classic_textfield(**kwargs):
        return ft.TextField(
            **kwargs,
            border_color="black",
            border_width=1,
            border_radius=0,
            bgcolor="white",
            text_size=11,
            color="black",
            height=28
        )

    # Classic dropdown style
    def create_classic_dropdown(**kwargs):
        return ft.Dropdown(
            **kwargs,
            border_color="black",
            border_width=1,
            border_radius=0,
            bgcolor="white",
            text_size=11,
            color="black",
            height=28
        )

    # UI Elements with classic styling
    path_field = create_classic_textfield(
        label="Output Directory",
        width=350,
        label_style=ft.TextStyle(size=11, weight=ft.FontWeight.BOLD, color="black")
    )
    
    url_field = create_classic_textfield(
        label="YouTube Link", 
        width=350,
        label_style=ft.TextStyle(size=11, weight=ft.FontWeight.BOLD, color="black")
    )
    
    format_dropdown = create_classic_dropdown(
        label="Format",
        options=[ft.dropdown.Option("mp3"), ft.dropdown.Option("flac"), ft.dropdown.Option("wav")],
        value="mp3",
        width=150,
        label_style=ft.TextStyle(size=11, weight=ft.FontWeight.BOLD, color="black")
    )
    
    quality_dropdown = create_classic_dropdown(
        label="Quality",
        options=[ft.dropdown.Option("best"), ft.dropdown.Option("128k"), ft.dropdown.Option("64k")],
        value="best",
        width=150,
        label_style=ft.TextStyle(size=11, weight=ft.FontWeight.BOLD, color="black")
    )
    
    status = ft.Text(value="", color="green", size=11, weight=ft.FontWeight.BOLD)
    
    open_folder_btn = create_classic_button("Open Folder", visible=False)

    # Functions (unchanged)
    def browse_folder(e):
        folder = filedialog.askdirectory()
        if folder:
            path_field.value = folder
            page.update()

    def paste_link(e):
        try:
            import pyperclip
            url_field.value = pyperclip.paste()
            page.update()
        except ImportError:
            status.value = "Install pyperclip for paste support (pip install pyperclip)"
            page.update()
            
    def open_folder(e):
        if os.path.isdir(path_field.value):
            os.startfile(path_field.value)
        else:
            status.value = "❌ Directory not found!"
        page.update()

    def download(e):
        if not url_field.value or not path_field.value:
            status.value = "❌ Missing link or output directory."
            page.update()
            return

        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format", format_dropdown.value,
            "-o", f"{path_field.value}/%(title)s.%(ext)s",
            url_field.value,
        ]
        subprocess.run(cmd)
        status.value = "✅ Download complete!"
        open_folder_btn.visible = True
        page.update()
        
    open_folder_btn.on_click = open_folder

    # Create classic buttons
    browse_btn = create_classic_button("Browse", on_click=browse_folder, width=80)
    paste_btn = create_classic_button("Paste", on_click=paste_link, width=80)
    download_btn = create_classic_button("DOWNLOAD", on_click=download, width=200, height=32)

    # Layout with classic grouping
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    # Title bar effect
                    ft.Container(
                        content=ft.Text(
                            "AUDIO DOWNLOADER", 
                            size=12, 
                            weight=ft.FontWeight.BOLD,
                            color="white"
                        ),
                        width=480,
                        height=25,
                        alignment=ft.alignment.center_left,
                        padding=ft.padding.only(left=10),
                        bgcolor="#0A246A",  # Classic title bar blue
                        margin=ft.margin.only(bottom=10)
                    ),
                    
                    # Main content area
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Row([path_field, browse_btn]),
                                ft.Row([url_field, paste_btn]),
                                ft.Row([format_dropdown, quality_dropdown]),
                                ft.Container(
                                    content=download_btn,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(top=10, bottom=10)
                                ),
                                ft.Container(
                                    content=open_folder_btn,
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    content=status,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(top=10)
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=12,
                        ),
                        bgcolor="#ECE9D8",
                        padding=20,
                        border=ft.border.all(2, "#808080"),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            ),
            alignment=ft.alignment.center,
            bgcolor="#ECE9D8",
            padding=10,
        )
    )

ft.app(target=main)

# This is to create the executable
# pyinstaller --onefile --noconsole --icon=appicon.ico YouTube_Downloader.py