import customtkinter
import specviewer_engine as engine
import tooltip_engine as tip
from PIL import Image
from CTkMessagebox import CTkMessagebox


class SetApp(customtkinter.CTk):

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

        # Configure grid for layout management
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a home frame and assign it to the grid
        self.home = customtkinter.CTkFrame(self, fg_color='transparent')
        self.home.grid(row=0, column=0, sticky="n")  # Frame placed in the grid

        # Configure rows for home frame
        self.home.grid_rowconfigure(0, weight=4)

        # Images loader
        spec_logo = customtkinter.CTkImage(Image.open(
            'images/specviewer_logo1.png'), size=(300, 100))
        os_logo = customtkinter.CTkImage(Image.open(
            'images/os.png'), size=(200, 150))
        cpu_logo = customtkinter.CTkImage(Image.open(
            'images/cpu.png'), size=(200, 150))
        ram_logo = customtkinter.CTkImage(Image.open(
            'images/ram.png'), size=(200, 150))
        gpu_logo = customtkinter.CTkImage(Image.open(
            'images/gpu.png'), size=(200, 150))

        def os_details():
            return CTkMessagebox(self.home, title="OS Details",
                                 message="UNDER CONSTRUCTION",
                                 option_1="Close",
                                 fg_color="transparent",
                                 title_color="red",
                                 button_color="transparent",
                                 button_hover_color="red",
                                 font=("Utah Bold", 15),
                                 button_text_color="black",
                                 button_width=350,
                                 sound=True)

        def cpu_details():
            return CTkMessagebox(self.home, title="CPU Details",
                                 message="UNDER CONSTRUCTION",
                                 option_1="Close",
                                 fg_color="transparent",
                                 title_color="red",
                                 button_color="transparent",
                                 button_hover_color="red",
                                 font=("Utah Bold", 15),
                                 button_text_color="black",
                                 button_width=350,
                                 sound=True)

        def ram_details():
            return CTkMessagebox(self.home, title="RAM Details",
                                 message="UNDER CONSTRUCTION",
                                 option_1="Close",
                                 fg_color="transparent",
                                 title_color="red",
                                 button_color="transparent",
                                 button_hover_color="red",
                                 font=("Utah Bold", 15),
                                 button_text_color="black",
                                 button_width=350,
                                 sound=True
                                 )

        def gpu_details():
            return CTkMessagebox(self.home, title="GPU Details",
                                 message="UNDER CONSTRUCTION",
                                 option_1="Close",
                                 fg_color="transparent",
                                 title_color="red",
                                 button_color="transparent",
                                 button_hover_color="red",
                                 font=("Utah Bold", 15),
                                 button_text_color="black",
                                 button_width=350,
                                 sound=True
                                 )

        # Title label + logo
        title_label = customtkinter.CTkLabel(self.home, text="", image=spec_logo)
        title_label.grid(row=0, column=1)

        # Version banner
        version_label = customtkinter.CTkLabel(self.home, text="v.0.1", font=('Utah Bold', 15))
        version_label.grid(row=1, column=1)

        # Exit button
        exit_button = customtkinter.CTkButton(master=self.home, text="Exit", fg_color="transparent", hover_color="red",
                                              font=('Utah Bold', 45), text_color="black")
        exit_button.grid(row=0, column=3)
        tip.ToolTip(exit_button, "Close this app")

        # OS
        os_button = customtkinter.CTkButton(master=self.home, image=os_logo, text="", fg_color="transparent",
                                            hover_color="red", command=os_details)
        os_label = customtkinter.CTkLabel(self.home, text='OPERATING SYSTEM:', font=('Chiller', 35), text_color="red", compound="top")
        os_value = customtkinter.CTkLabel(self.home, text=engine.SpecView('os'), font=('Utah Bold', 22), compound="top")
        os_button.grid(row=2, column=1, pady=3)
        #os_label.grid(row=1, column=2)
        os_value.grid(row=2, column=3, pady=3)
        tip.ToolTip(os_button, "Click for OS details...")

        # CPU
        cpu_button = customtkinter.CTkButton(master=self.home, image=cpu_logo, text="", fg_color="transparent",
                                             hover_color="red", command=cpu_details)
        cpu_label = customtkinter.CTkLabel(self.home, text='CPU:', font=('Chiller', 35), text_color="red", compound="top")
        cpu_value = customtkinter.CTkLabel(self.home, text=engine.SpecView('cpu'), font=('Utah Bold', 22), compound="top")
        cpu_button.grid(row=3, column=1, pady=3)
        #cpu_label.grid(row=2, column=2)
        cpu_value.grid(row=3, column=3, pady=3)
        tip.ToolTip(cpu_button, "Click for CPU details...")

        # RAM
        ram_button = customtkinter.CTkButton(master=self.home, image=ram_logo, text="", fg_color="transparent",
                                             hover_color="red", command=ram_details)
        ram_label = customtkinter.CTkLabel(self.home, text='RAM:', font=('Chiller', 35), text_color="red", compound="top")
        ram_value = customtkinter.CTkLabel(self.home, text=engine.SpecView('ram'), font=('Utah Bold', 22), compound="top")
        ram_button.grid(row=4, column=1, pady=3)
        #ram_label.grid(row=3, column=2)
        ram_value.grid(row=4, column=3, pady=3)
        tip.ToolTip(ram_button, "Click for RAM details...")

        # GPU
        gpu_button = customtkinter.CTkButton(master=self.home, image=gpu_logo, text="", fg_color="transparent",
                                             hover_color="red", command=gpu_details)
        gpu_label = customtkinter.CTkLabel(self.home, text='GPU:', font=('Chiller', 35), text_color="red",  compound="top")
        gpu_value = customtkinter.CTkLabel(self.home, text=engine.SpecView('gpu'), font=('Utah Bold', 22), compound="top")
        gpu_button.grid(row=5, column=1, pady=3)
        #gpu_label.grid(row=4, column=2)
        gpu_value.grid(row=5, column=3, pady=3)
        tip.ToolTip(gpu_button, "Click for GPU details...")


if __name__ == "__main__":
    # Set the appearance and theme
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")

    # Create an instance of the SetApp class
    app = SetApp("SPECViewer", 1100, 800)

    # Start the main loop
    app.mainloop()