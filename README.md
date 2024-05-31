  YouTube Playlist Downloader

YouTube Playlist Downloader
===========================

A simple Tkinter-based GUI application to download videos from a YouTube playlist using the Pytube library.

Features
--------

*   Fetch and download all videos from a given YouTube playlist.
*   Log progress in a scrolled text widget.
*   Display success or error messages using message boxes.

Requirements
------------

*   Python 3.x
*   Pytube
*   Tkinter

Installation
------------

1.  Clone the repository:
    
        git clone https://github.com/muzammilkhan26/ytplaylistdownloader.git
        cd ytplaylistdownloader
    
2.  Create a virtual environment (optional but recommended):
    
        python -m venv venv
        source venv/bin/activate   # On Windows: venv\Scripts\activate
    
3.  Install the required packages:
    
        pip install -r requirements.txt
    

Usage
-----

1.  Run the application:
    
        python downloader.py
    
2.  Enter a YouTube playlist URL in the provided text field.
3.  Click the "Download" button to start downloading the videos in the playlist.

Code Overview
-------------

The main functionality of the application is provided in `downloader.py`. The key components are:

*   `log_message(message)`: Function to log messages in the ScrolledText widget.
*   `download_playlist(playlist_url)`: Function to fetch and download videos from the playlist.
*   `start_download()`: Function to start the download process in a separate thread.
*   Tkinter GUI setup to create the application window, input field, button, and log text widget.

Handling Errors
---------------

*   If the playlist URL is invalid or there is an error in fetching the playlist, an error message box is displayed.
*   If any video fails to download, the error is logged, and an error message box is displayed.

Dependencies
------------

Make sure to install the following Python packages:

*   pytube
*   tkinter (usually included with Python installations)

Author
------

*   [Muhammad Muzammil Khan](https://github.com/muzammilkhan26)