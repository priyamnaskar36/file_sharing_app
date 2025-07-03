# File Sharing App (Python)

A simple Python-based file sharing application with a graphical user interface (GUI) using `tkinter` and socket programming.

## 📦 Features

- 🔁 Transfer files from server to client over a local network
- 🖥️ GUI interface for both client and server
- 🗂️ Server allows folder selection for sharing
- 🧾 Client can request specific files and save them locally

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (for GUI)
- Sockets (for networking)
- Threading (for handling multiple connections)

---

## 🚀 How It Works

### Server

1. Run `server_file.py`.
2. Use the "Browse Folder" button to select a directory containing files you want to share.
3. Click "Start Server" to listen for incoming requests.

### Client

1. Run `client_server.py`.
2. Enter the **Server IP Address** and the **filename** you want to download.
3. Choose where to save the file when prompted.

---


---

## 📝 Example

- Run `server_file.py` on one machine (or the same machine).
- Note the IP address (e.g., `192.168.1.10`).
- Run `client_server.py` on another device in the same network.
- Enter the server IP and filename when prompted.

---

## ⚠️ Limitations

- Works only on local networks (LAN/Wi-Fi)
- No encryption used — for learning/demo purposes only
- Basic error handling

---

## ✅ To Do / Future Improvements

- Add encryption (SSL/TLS)
- Allow file listing on the client side
- Support multiple simultaneous client downloads
- Add progress bar

---

## 📂 Project Structure

