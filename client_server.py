import socket
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

PORT = 5001

class FileClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Client")

        tk.Button(root, text="Download File", command=self.download_file).pack(pady=20)

    def download_file(self):
        server_ip = simpledialog.askstring("Server IP", "Enter Server IP:")
        filename = simpledialog.askstring("Filename", "Enter filename to request:")

        if not server_ip or not filename:
            messagebox.showwarning("Warning", "Please provide valid input")
            return

        client = socket.socket()
        try:
            client.connect((server_ip, PORT))
            client.send(filename.encode())
            status = client.recv(1024).decode()

            if status == "EXISTS":
                save_path = filedialog.asksaveasfilename(defaultextension=".bin", initialfile=filename)
                if save_path:
                    with open(save_path, 'wb') as f:
                        while True:
                            data = client.recv(1024)
                            if not data:
                                break
                            f.write(data)
                    messagebox.showinfo("Success", f"File saved to: {save_path}")
            else:
                messagebox.showerror("Error", "File not found on server")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            client.close()

root = tk.Tk()
app = FileClientApp(root)
root.mainloop()
