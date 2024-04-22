import requests
import json
import tkinter as tk
import io
from PIL import Image, ImageTk

def fetch_and_display_toon_image():
    url = "http://localhost:1547/info.json"
    headers = {'User-Agent': 'TTRWeb v1 TEST'}
    
    try:
        r = requests.get(url, headers=headers)
        data = r.json()

        # Extracting necessary information from JSON response
        toon_style = data['toon']['style']

        # Constructing URL for toon portrait image
        toon_image_url = f"https://rendition.toontownrewritten.com/render/{toon_style}/portrait/1024x1024.png"

        # Fetching the image
        response = requests.get(toon_image_url)
        image_data = response.content

        # Displaying the image using Tkinter
        image = Image.open(io.BytesIO(image_data))
        image = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=image)
        label.image = image  # Keep a reference to avoid garbage collection
        label.pack()

    except Exception as e:
        print("Error fetching or displaying image:", e)

# Create Tkinter window
root = tk.Tk()
root.title("Toon Image Display")

# Fetch and display the toon image
fetch_and_display_toon_image()

# Run the Tkinter event loop
root.mainloop()
