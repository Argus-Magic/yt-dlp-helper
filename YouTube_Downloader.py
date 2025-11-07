import flet as ft
import subprocess
import os
from tkinter import filedialog, Tk

def main(page: ft.Page):
    page.title = "Audio Downloader"
    page.window_width = 450
    page.window_height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Hide tkinter root window (for folder picker)
    Tk().withdraw()

    # UI Elements
    path_field = ft.TextField(label="Output Directory", width=350)
    url_field = ft.TextField(label="YouTube Link", width=350)
    format_dropdown = ft.Dropdown(
        label="Format",
        options=[ft.dropdown.Option("mp3"), ft.dropdown.Option("flac"), ft.dropdown.Option("wav")],
        value="mp3",
        width=150,
    )
    quality_dropdown = ft.Dropdown(
        label="Quality",
        options=[ft.dropdown.Option("best"), ft.dropdown.Option("128k"), ft.dropdown.Option("64k")],
        value="best",
        width=150,
    )
    status = ft.Text(value="", color="green")
    open_folder_btn = ft.ElevatedButton("Open Folder", visible=False)

    # Functions
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

    # Layout
    page.add(
        ft.Column(
            [
                ft.Row([path_field, ft.ElevatedButton("Browse", on_click=browse_folder)]),
                ft.Row([url_field, ft.ElevatedButton("Paste", on_click=paste_link)]),
                ft.Row([format_dropdown, quality_dropdown]),
                ft.ElevatedButton("Download", on_click=download),
                open_folder_btn,
                status,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)

#This is to create the executable
#pyinstaller --onefile --noconsole --icon=appicon.ico YouTube_Downloader.py
