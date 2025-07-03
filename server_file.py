import socket
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
import os

HOST = '0.0.0.0'
PORT = 5001

class FileServerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Server")

        self.label = tk.Label(root, text="Selected folder:")
        self.label.pack(pady=5)

        self.folder_path = tk.StringVar()
        tk.Entry(root, textvariable=self.folder_path, width=50).pack(pady=5)
        tk.Button(root, text="Browse Folder", command=self.browse_folder).pack(pady=5)

        tk.Button(root, text="Start Server", command=self.start_server).pack(pady=10)
        self.status = tk.Label(root, text="")
        self.status.pack(pady=5)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def start_server(self):
        threading.Thread(target=self.run_server, daemon=True).start()
        self.status.config(text="Server started...")

    def run_server(self):
        server = socket.socket()
        server.bind((HOST, PORT))
        server.listen(5)
        while True:
            client_socket, addr = server.accept()
            filename = client_socket.recv(1024).decode()
            filepath = os.path.join(self.folder_path.get(), filename)
            if os.path.exists(filepath):
                client_socket.send(b'EXISTS')
                with open(filepath, 'rb') as f:
                    while (chunk := f.read(1024)):
                        client_socket.send(chunk)
            else:
                client_socket.send(b'NOFILE')
            client_socket.close()

root = tk.Tk()
app = FileServerApp(root)
root.mainloop()
