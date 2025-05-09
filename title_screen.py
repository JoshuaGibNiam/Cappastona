import ttkbootstrap as ttk

class TitleScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Cappastona")
        self.root.geometry("750x750")

        ## 1. Title Label
        self.title_style = ttk.Style()
        self.title_style.configure("Title.TLabel", font="Verdana 25 bold", foreground="white", background="#696969",
                                   relief="groove")

        self.title_frame = ttk.Frame(self.root)
        self.title_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.title_label = ttk.Label(self.title_frame, style="Title.TLabel", text="Cappastona", anchor="center", justify="center")
        self.title_label.pack(fill="both", expand=True, padx=5, pady=5)


        ## Mainloop
        self.root.mainloop()


if __name__ == "__main__":
    root = ttk.Window(themename="cyborg")
    TitleScreen(root)