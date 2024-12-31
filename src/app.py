# import tkinter as tk
# from tkinter import messagebox, ttk, filedialog
# import yt_dlp as ydl
# import os
# import threading

# # Function to read the saved download location
# def read_download_location():
#     if os.path.exists("config.txt"):
#         with open("config.txt", "r") as f:
#             print(f.read)
#             return f.read().strip()
#     return ""

# # Function to save the download location to the config file
# def save_download_location(path):
#     with open("config.txt", "w") as f:
#         f.write(path)

# # Function to Display Available Formats
# def show_formats():
#     link = url_entry.get()
#     if not link:
#         messagebox.showwarning("Warning", "Please enter a valid YouTube URL!")
#         return
    
#     try:
#         with ydl.YoutubeDL() as ydl_instance:
#             info_dict = ydl_instance.extract_info(link, download=False)
#             formats = info_dict.get('formats', [])
#             format_info = "\n".join([f"{fmt['format_id']}: {fmt.get('format_note', 'N/A')} ({fmt['ext']})" for fmt in formats])
#             log_text.delete('1.0', tk.END)
#             log_text.insert(tk.END, format_info)
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to retrieve formats: {e}")


# # Download Functionality
# def download_video():
#     link = url_entry.get()
#     if not link:
#         messagebox.showwarning("Warning", "Please enter a valid YouTube URL!")
#         return

#     # Get the selected format from the Combobox
#     choice = format_var.get()

#     # Validate the choice
#     valid_choices = ["Audio Only", "Video Only", "Best Quality", "Low Quality"]
#     if choice not in valid_choices:
#         messagebox.showerror("Error", f"Invalid choice: {choice}. Please select a valid format.")
#         return

#     download_options = {
#         "Audio Only": {
#             'format': 'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }],
#         },
#         "Video Only": {
#             'format': 'bestvideo[ext=mp4]',
#         },
#         "Best Quality": {
#             'format': 'bestvideo+bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegVideoConvertor',
#                 'preferedformat': 'mp4',
#             }],
#         },
#         "Low Quality": {
#             'format': 'worstvideo+worstaudio/worst',
#         }
#     }

#     # Get the saved download location
#     download_location = read_download_location()
#     if not download_location:
#         # Prompt user for location if not set
#         download_location = filedialog.askdirectory(title="Select Download Location")
#         if not download_location:
#             messagebox.showwarning("Warning", "Download location not selected!")
#             return
#         save_download_location(download_location)  # Save the location

#     ydl_opts = {
#         'outtmpl': f'{download_location}/%(title)s.%(ext)s',  # Use user-selected path
#         **download_options.get(choice, {})
#     }

#     # Use a separate thread to handle the download process
#     download_thread = threading.Thread(target=perform_download, args=(link, ydl_opts))
#     download_thread.start()


# # Perform the actual download in a separate thread
# def perform_download(link, ydl_opts):
#     try:
#         log_text.delete('1.0', tk.END)
#         log_text.insert(tk.END, f"Downloading {format_var.get()}...\n")
#         with ydl.YoutubeDL(ydl_opts) as ydl_instance:
#             ydl_instance.download([link])
#         log_text.insert(tk.END, "✅ Download completed successfully!\n")
#     except Exception as e:
#         log_text.insert(tk.END, f"❌ Error during download: {e}\n")
#         messagebox.showerror("Error", f"Download failed: {e}")


# # Function to change the download location
# def change_location():
#     new_location = filedialog.askdirectory(title="Select New Download Location")
#     if new_location:
#         save_download_location(new_location)
#         messagebox.showinfo("Success", f"Download location changed to:\n{new_location}")

# # Initialize Tkinter Window
# root = tk.Tk()
# root.title("YouTube Video & Audio Downloader by JD")
# root.geometry("600x600")
# root.resizable(False, False)

# # Title Label
# title_label = tk.Label(root, text="YouTube Downloader", font=("Arial", 20, "bold"))
# title_label.pack(pady=10)

# # URL Entry Field
# url_label = tk.Label(root, text="Video URL:", font=("Arial", 12))
# url_label.pack(pady=5)

# url_entry = tk.Entry(root, width=50, font=("Arial", 12))
# url_entry.pack(pady=5)

# # Format Options Dropdown
# format_label = tk.Label(root, text="Select Format:", font=("Arial", 12))
# format_label.pack(pady=5)

# format_var = tk.StringVar(value="Audio Only")
# format_menu = ttk.Combobox(root, textvariable=format_var, values=["Audio Only", "Video Only", "Best Quality", "Low Quality"], font=("Arial", 12))
# format_menu.pack(pady=5)

# # Download Button
# download_btn = tk.Button(root, text="Download", command=download_video, bg="green", fg="white", font=("Arial", 12, "bold"))
# download_btn.pack(pady=20)

# # Change Download Location Button
# change_location_btn = tk.Button(root, text="Change Location", command=change_location, bg="orange", fg="white", font=("Arial", 12))
# change_location_btn.pack(pady=10)

# # Status/Log Textbox
# # log_label = tk.Label(root, text="Download Log:", font=("Arial", 12))
# # log_label.pack(pady=5)

# log_text = tk.Text(root, height=3, width=50, font=("Arial", 10))
# log_text.pack(pady=5)

# # Run Tkinter Mainloop
# root.mainloop()



import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import yt_dlp as ydl
import os
import threading

# Function to read the saved download location
def read_download_location():
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as f:
            return f.read().strip()
    return ""

# Function to save the download location to the config file
def save_download_location(path):
    with open("config.txt", "w") as f:
        f.write(path)

# Function to Display Available Formats
def show_formats():
    link = url_entry.get()
    if not link:
        messagebox.showwarning("Warning", "Please enter a valid YouTube URL!")
        return
    
    try:
        with ydl.YoutubeDL() as ydl_instance:
            info_dict = ydl_instance.extract_info(link, download=False)
            formats = info_dict.get('formats', [])
            format_info = "\n".join([f"{fmt['format_id']}: {fmt.get('format_note', 'N/A')} ({fmt['ext']})" for fmt in formats])
            log_text.delete('1.0', tk.END)
            log_text.insert(tk.END, format_info)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve formats: {e}")

# Download Functionality
def download_video():
    link = url_entry.get()
    if not link:
        messagebox.showwarning("Warning", "Please enter a valid YouTube URL!")
        return

    # Get the selected format from the Combobox
    choice = format_var.get()

    # Validate the choice
    valid_choices = ["Audio Only", "Video Only", "Best Quality", "Low Quality"]
    if choice not in valid_choices:
        messagebox.showerror("Error", f"Invalid choice: {choice}. Please select a valid format.")
        return

    download_options = {
        "Audio Only": {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        },
        "Video Only": {
            'format': 'bestvideo[ext=mp4]',
        },
        "Best Quality": {
            'format': 'bestvideo+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        },
        "Low Quality": {
            'format': 'worstvideo+worstaudio/worst',
        }
    }

    # Get the saved download location
    download_location = read_download_location()
    if not download_location:
        # Prompt user for location if not set
        download_location = filedialog.askdirectory(title="Select Download Location")
        if not download_location:
            messagebox.showwarning("Warning", "Download location not selected!")
            return
        save_download_location(download_location)  # Save the location

    ydl_opts = {
        'outtmpl': f'{download_location}/%(title)s.%(ext)s',  # Use user-selected path
        **download_options.get(choice, {})
    }

    # Use a separate thread to handle the download process
    download_thread = threading.Thread(target=perform_download, args=(link, ydl_opts))
    download_thread.start()


# Perform the actual download in a separate thread
def perform_download(link, ydl_opts):
    try:
        log_text.delete('1.0', tk.END)
        log_text.insert(tk.END, f"Downloading {format_var.get()}...\n")
        with ydl.YoutubeDL(ydl_opts) as ydl_instance:
            ydl_instance.download([link])
        log_text.insert(tk.END, "✅ Download completed successfully!\n")
    except Exception as e:
        log_text.insert(tk.END, f"❌ Error during download: {e}\n")
        messagebox.showerror("Error", f"Download failed: {e}")

# Function to change the download location
def change_location():
    new_location = filedialog.askdirectory(title="Select New Download Location")
    if new_location:
        save_download_location(new_location)
        messagebox.showinfo("Success", f"Download location changed to:\n{new_location}")

# Initialize Tkinter Window
root = tk.Tk()
root.title("YouTube Video & Audio Downloader by JD")
root.geometry("600x600")
root.resizable(False, False)

# Apply color scheme to the whole window
root.configure(bg="black")  # Set the background color of the root window

# Title Label with custom colors
title_label = tk.Label(root, text="YouTube Downloader", font=("Arial", 20, "bold"), bg="black", fg="white")
title_label.pack(pady=10)

# URL Entry Field with custom colors
url_label = tk.Label(root, text="Video URL", font=("Arial", 12), bg="black", fg="white")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=40, font=("Arial", 12),  fg="darkblue")
url_entry.pack(pady=5)


# # Format Options Dropdown with custom colors
# format_label = tk.Label(root, text="Select Format:", font=("Arial", 12), bg="lightblue", fg="darkblue")
# format_label.pack(pady=5)

format_var = tk.StringVar(value="Audio Only")
format_menu = ttk.Combobox(root, textvariable=format_var, values=["Audio Only", "Video Only", "Best Quality", "Low Quality"], font=("Arial", 12))
format_menu.pack(pady=5)

# Download Button with custom colors
download_btn = tk.Button(root, text="Download", command=download_video, bg="red", fg="white", font=("Arial", 12, "bold"))
download_btn.pack(pady=20)

# Change Download Location Button with custom colors
change_location_btn = tk.Button(root, text="Change Location", command=change_location, bg="orange", fg="white", font=("Arial", 12))
change_location_btn.pack(pady=10)

# Status/Log Textbox with custom colors
log_text = tk.Text(root, height=3, width=50, font=("Arial", 10), bg="lightgray", fg="darkblue")
log_text.pack(pady=5)

# Label with "made by JD" text in the bottom-right corner
footer_label = tk.Label(root, text="Made by JD", font=("Arial", 10), bg="black", fg="white")
footer_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Run Tkinter Mainloop
root.mainloop()