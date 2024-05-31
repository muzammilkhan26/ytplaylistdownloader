import os
import threading
from pytube import Playlist
from pytube.exceptions import PytubeError
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def log_message(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)

def download_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        log_message("Playlist fetched successfully.")
    except PytubeError as e:
        log_message(f"Failed to fetch the playlist: {e}")
        messagebox.showerror("Error", f"Failed to fetch the playlist: {e}")
        return

    download_folder = 'downloads'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    log_message(f"Downloading {len(playlist.video_urls)} videos...")

    for video in playlist.videos:
        try:            
            i = 1
            log_message(f"Downloading {video.title}")
            video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(download_folder)
            log_message(f"Downloaded {i} Video out of {len(playlist.video_urls)}")
        except PytubeError as e:
            log_message(f"Failed to download {video.title}: {e}")
            messagebox.showerror("Error", f"Failed to download {video.title}: {e}")

    log_message("All videos downloaded.")
    messagebox.showinfo("Success", "All videos downloaded.")

def start_download():
    playlist_url = url_entry.get()
    if playlist_url:
        threading.Thread(target=download_playlist, args=(playlist_url,)).start()
    else:
        messagebox.showerror("Error", "Please enter a YouTube playlist URL")

app = tk.Tk()
app.title("YouTube Playlist Downloader")

frame = tk.Frame(app)
frame.pack(pady=20, padx=20)

url_label = tk.Label(frame, text="Enter YouTube Playlist URL:")
url_label.grid(row=0, column=0, pady=5)

url_entry = tk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, pady=5)

download_button = tk.Button(frame, text="Download", command=start_download)
download_button.grid(row=1, columnspan=2, pady=10)

log_text = ScrolledText(app, width=80, height=20, wrap=tk.WORD)
log_text.pack(pady=10)

app.mainloop()