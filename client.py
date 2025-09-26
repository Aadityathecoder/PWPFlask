import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import requests 
import json  

root = tk.Tk()
root.title("API System My Robot")
root.geometry("1920x1080")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

TopLeft = tk.Frame(root, bg="black", bd=2, relief="ridge")
TopLeft.grid(row=0, column=0, sticky="nsew")
VideoLabel1 = tk.Label(TopLeft, text="Video Stream 1 Placeholder", fg="white", bg="black")
VideoLabel1.pack(expand=True)

BottomLeft = tk.Frame(root, bg="black", bd=2, relief="ridge")
BottomLeft.grid(row=1, column=0, sticky="nsew")
VideoLabel2 = tk.Label(BottomLeft, text="Video Stream 2 Placeholder", fg="white", bg="black")
VideoLabel2.pack(expand=True)

TopRight = tk.Frame(root, bg="lightgray", bd=2, relief="ridge")
TopRight.grid(row=0, column=1, sticky="nsew")
ControlFrame = tk.Frame(TopRight, bg="lightgray")
ControlFrame.place(relx=0.5, rely=0.5, anchor="center")

BottomRight = tk.Frame(root, bg="white", bd=2, relief="ridge")
BottomRight.grid(row=1, column=1, sticky="nsew")
LogLabel = tk.Label(BottomRight, text="User Log", font=("Arial", 14))
LogLabel.pack(anchor="nw")
UL = scrolledtext.ScrolledText(BottomRight, wrap=tk.WORD, font=("Arial", 12))
UL.pack(expand=True, fill="both")
api_link = "http://127.0.0.1:5000/move"


def WriteUL(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    UL.insert(tk.END, f"[{ts}] {msg}\n")
    UL.see(tk.END)


def handle_get_request(direction):
    """Simulates sending a GET request and logs the response."""
    try:
       
        response = requests.get(f"{api_link}?direction={direction}")
        response.raise_for_status()  
        log_message = f"GET request sent for '{direction}'. Status: {response.status_code}. Response: {response.text}"
    except requests.exceptions.RequestException as e:
        log_message = f"GET request failed for '{direction}': {e}"

    WriteUL(log_message)

def handle_post_request(direction):
    """Simulates sending a POST request with a JSON body and logs the response."""
    try:
        data = {"command": "move_robot", "direction": direction}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(api_link, data=json.dumps(data), headers=headers)
        response.raise_for_status()  
        log_message = f"POST request sent for '{direction}'. Status: {response.status_code}. Response: {response.text}"
    except requests.exceptions.RequestException as e:
        log_message = f"POST request failed for '{direction}': {e}"

    WriteUL(log_message)

UpButton = tk.Button(ControlFrame, text="↑", width=5, height=2, command=lambda: handle_post_request("Up"))
LeftButton = tk.Button(ControlFrame, text="←", width=5, height=2, command=lambda: handle_post_request("Left"))
RightButton = tk.Button(ControlFrame, text="→", width=5, height=2, command=lambda: handle_post_request("Right"))
DownButton = tk.Button(ControlFrame, text="↓", width=5, height=2, command=lambda: handle_post_request("Down"))
PlayButton = tk.Button(ControlFrame, text="▶ Play", width=8, height=2, command=lambda: handle_get_request("Play"))
StopButton = tk.Button(ControlFrame, text="■ Stop", width=8, height=2, command=lambda: handle_get_request("Stop"))

UpButton.grid(row=0, column=1, padx=5, pady=5)
LeftButton.grid(row=1, column=0, padx=5, pady=5)
PlayButton.grid(row=1, column=1, padx=5, pady=5)
RightButton.grid(row=1, column=2, padx=5, pady=5)
DownButton.grid(row=2, column=1, padx=5, pady=5)
StopButton.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()

