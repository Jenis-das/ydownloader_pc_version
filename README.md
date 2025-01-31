# YouTube Video Downloader

A desktop application built with Python and Tkinter that allows users to download YouTube videos directly to their computers. The app offers a user-friendly interface and supports multiple resolutions and formats.

**Note**: This project is intended for educational purposes only. 
Many people want to download videos from third-party websites, but often face issues with malicious software or viruses. This tool provides a safe way to download YouTube videos without encountering such problems.

## To Download 
<a href="https://raw.githubusercontent.com/Jenis-das/ydownloader_pc_version/main/src/dist/app.exe" download>
    <button>Download app.exe</button>
</a>

## Features

- **Search and Download**: Search for YouTube videos by URL or keyword and download them easily.
- **Multiple Formats**: Choose from various video resolutions and audio-only formats.
- **Download Manager**: View and manage active and completed downloads.

## Prerequisites

To run this project locally, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **FFmpeg**: For video and audio processing (ensure it's added to your system PATH)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/jenis-das/ydownloader_pc_version.git
   ```
2. Navigate to the project directory
  ```bash 
  cd ydownloader_pc_version
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Run
```bash 
python app.py
```

5. To wrap in one exe file
to add icon
select your icon as png and covert it into .ico file and should be stored near the app.py
```bash
pyinstaller --onefile --windowed --icon=your_icon.ico app.py
```
