import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class GmGameApp:

  def __init__(self, root):
    self.root = root
    self.root.title("GmGame - Game Launcher")
    self.root.geometry("650x450")

    self.games = []

    # Title Label
    self.title_label = ttk.Label(
        root, text="GmGame Library", font=("Arial", 16, "bold")
    )
    self.title_label.pack(pady=10)

    # Game Listbox with Scrollbar
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

    self.game_listbox = tk.Listbox(frame, font=("Arial", 11), selectmode=tk.SINGLE)
    self.game_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(
        frame, orient="vertical", command=self.game_listbox.yview
    )
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    self.game_listbox.config(yscrollcommand=scrollbar.set)

    # Buttons Frame
    btn_frame = ttk.Frame(root)
    btn_frame.pack(fill=tk.X, padx=15, pady=15)

    self.add_btn = ttk.Button(
        btn_frame, text="Add Game", command=self.add_game
    )
    self.add_btn.pack(side=tk.LEFT, padx=5)

    self.launch_btn = ttk.Button(
        btn_frame, text="Launch Game", command=self.launch_game
    )
    self.launch_btn.pack(side=tk.LEFT, padx=5)

    self.remove_btn = ttk.Button(
        btn_frame, text="Remove Game", command=self.remove_game
    )
    self.remove_btn.pack(side=tk.LEFT, padx=5)

  def add_game(self):
    file_path = filedialog.askopenfilename(
        title="Select Game Executable or File",
        filetypes=[("Executables & Files", "*.exe *.bat *.lnk"), ("All Files", "*.*")],
    )
    if file_path:
      game_name = os.path.basename(file_path)
      self.games.append({"name": game_name, "path": file_path})
      self.game_listbox.insert(tk.END, game_name)
      messagebox.showinfo(
          "Success", f"Added '{game_name}' to your GmGame library!"
      )

  def launch_game(self):
    try:
      selected_idx = self.game_listbox.curselection()[0]
      game = self.games[selected_idx]
      path = game["path"]

      if os.path.exists(path):
        subprocess.Popen([path], shell=True)
      else:
        messagebox.showerror(
            "Error", "The game file could not be found at the specified path."
        )
    except IndexError:
      messagebox.showwarning(
          "Warning", "Please select a game from the list to launch."
      )

  def remove_game(self):
    try:
      selected_idx = self.game_listbox.curselection()[0]
      self.game_listbox.delete(selected_idx)
      removed = self.games.pop(selected_idx)
      messagebox.showinfo(
          "Removed", f"Removed '{removed['name']}' from library."
      )
    except IndexError:
      messagebox.showwarning(
          "Warning", "Please select a game from the list to remove."
      )


if __name__ == "__main__":
  root = tk.Tk()
  app = GmGameApp(root)
  root.mainloop()