import specviewer_engine as engine
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


class SetApp(tk.Tk):
    def __init__(self, title, app_x, app_y):
        super().__init__()

        # Basic window setup
        self.title(title)

        # Get screen size and calculate window position
        screen_x = self.winfo_screenwidth()
        screen_y = self.winfo_screenheight()
        x_position = int((screen_x / 2) - (app_x / 2))
        y_position = int((screen_y / 2) - (app_y / 2))
        self.geometry(f'{app_x}x{app_y}+{x_position}+{y_position}')

        # Prevent resizing the window
        self.resizable(False, False)

        # Create a home frame and assign it to the grid
        self.home = tk.Frame(self)
        self.home.grid(row=0, column=0, sticky="n")  # Frame placed in the grid

        # Images loader - poprawiamy ładowanie obrazów i ich rozmiary
        spec_logo_img = Image.open('images/specviewer_logo1.png').resize((310, 100))
        spec_logo_img = ImageTk.PhotoImage(spec_logo_img)

        os_logo_img = Image.open('images/os.png').resize((150, 100))
        os_logo_img = ImageTk.PhotoImage(os_logo_img)

        cpu_logo_img = Image.open('images/cpu.png').resize((150, 100))
        cpu_logo_img = ImageTk.PhotoImage(cpu_logo_img)

        ram_logo_img = Image.open('images/ram.png').resize((150, 100))
        ram_logo_img = ImageTk.PhotoImage(ram_logo_img)

        gpu_logo_img = Image.open('images/gpu.png').resize((150, 100))
        gpu_logo_img = ImageTk.PhotoImage(gpu_logo_img)

        mb_logo_img = Image.open('images/mb.png').resize((150, 100))
        mb_logo_img = ImageTk.PhotoImage(mb_logo_img)

        dsc_logo_img = Image.open('images/hdd.png').resize((150, 100))
        dsc_logo_img = ImageTk.PhotoImage(dsc_logo_img)

        def exit_app():
            self.destroy()

        def cpu_details():
            messagebox.showinfo("CPU Details", engine.SpecView('cpu_d'))

        def ram_details():
            messagebox.showinfo("RAM Details", engine.SpecView('ram_d'))

        def gpu_details():
            messagebox.showinfo("GPU Details", engine.SpecView('gpu_d'))

        def mb_details():
            messagebox.showinfo("MOBO Details", engine.SpecView('mb_d'))

        def dsc_details():
            messagebox.showinfo("Discs Details", engine.SpecView('dsc_d'))

        # Title label + logo
        title_label = tk.Label(self.home, image=spec_logo_img)  # Użycie załadowanego obrazu
        title_label.grid(row=0, column=1)

        # Version banner
        version_label = tk.Label(self.home, text="v.1.0 EA", font=('Utah Bold', 15))
        version_label.grid(row=1, column=1)

        # Exit button
        exit_button = tk.Button(self.home, text="Exit", fg="red", font=('Utah Bold', 20), command=exit_app)
        exit_button.grid(row=0, column=3)

        # CPU
        cpu_button = tk.Button(self.home, image=cpu_logo_img, command=cpu_details)
        cpu_label = tk.Label(self.home, text=engine.SpecView('cpu'))
        cpu_button.grid(row=3, column=1, pady=3)
        cpu_label.grid(row=3, column=2, pady=3)

        # RAM
        ram_button = tk.Button(self.home, image=ram_logo_img, command=ram_details)
        ram_label=tk.Label(self.home, text=engine.SpecView('ram'))
        ram_button.grid(row=4, column=1, pady=15)
        ram_label.grid(row=4, column=2, pady=3)

        # GPU
        gpu_button = tk.Button(self.home, image=gpu_logo_img, command=gpu_details)
        gpu_label = tk.Label(self.home, text=engine.SpecView('gpu'))
        gpu_button.grid(row=5, column=1, pady=15)
        gpu_label.grid(row=5, column=2, pady=3)

        # MB
        mb_button = tk.Button(self.home, image=mb_logo_img, command=mb_details)
        mb_label = tk.Label(self.home, text=engine.SpecView('mb'))
        mb_button.grid(row=6, column=1, pady=15)
        mb_label.grid(row=6, column=2, pady=3)

        # DISC
        dsc_button = tk.Button(self.home, image=dsc_logo_img, command=dsc_details)
        dsc_label = tk.Label(self.home, text=engine.SpecView('dsc'))
        dsc_button.grid(row=7, column=1, pady=15)
        dsc_label.grid(row=7, column=2, pady=3)

        # Aby obrazy nie zniknęły, trzeba je przypisać do atrybutu obiektu
        self.spec_logo_img = spec_logo_img
        self.os_logo_img = os_logo_img
        self.cpu_logo_img = cpu_logo_img
        self.ram_logo_img = ram_logo_img
        self.gpu_logo_img = gpu_logo_img
        self.mb_logo_img = mb_logo_img
        self.dsc_logo_img = dsc_logo_img


app = SetApp("SPECViewer", 850, 800)
app.mainloop()