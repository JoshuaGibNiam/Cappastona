import ttkbootstrap as ttk
import json
import tkinter.messagebox
import tkinter as tk


class TitleScreen:
    def __init__(self, root):
        self.root = root



        #initializing other stuff
        self.logged_in_state = ttk.StringVar()
        self.logged_in_state.set('Logged In as Guest')

        self.title_screen()
        self.root.mainloop()
    def title_screen(self):
        self.root = root
        self.root.title("Cappastona")
        self.root.geometry("750x750")

        ## 1. Title Label
        self.title_style = ttk.Style()
        self.title_style.configure("Title.TLabel", font="Verdana 25 bold", foreground="white", background="#3b3a3a",
                                   relief="flat")

        self.title_frame = ttk.Frame(self.root)
        self.title_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.title_label = ttk.Label(self.title_frame, style="Title.TLabel", text="Cappastona", anchor="center", justify="center")
        self.title_label.pack(fill="both", expand=True, padx=5, pady=5)

        ## 2. Sign up or log in if logged out
        if self.logged_in_state.get() == 'Logged In as Guest':
            self.option_frame = ttk.Frame(self.root)
            self.option_frame.pack(fill="both", expand=True, padx=5, pady=5)

            self.login_button_1 = ttk.Button(self.option_frame, text="Log In", command=self.login_screen, bootstyle="primary")
            self.login_button_1.pack(side="left", expand=True, padx=5, pady=5, ipadx=200, ipady=100)

            self.signup_button_1 = ttk.Button(self.option_frame, text="Sign Up", bootstyle="secondary", command=self.signup_screen)
            self.signup_button_1.pack(side="left", expand=True, padx=5, pady=5, ipadx=200, ipady=100)

        ## 3. label that displays account that is logged in
        self.logged_in_state_label = ttk.Label(self.title_frame, textvariable=self.logged_in_state, bootstyle="primary", anchor="center", justify="center")
        self.logged_in_state_label.pack(fill="x", expand=True, padx=5, pady=5)

        if self.logged_in_state.get() != "Logged In as Guest":
            self.launch_button = ttk.Button(self.root, text="Launch Cappastona", bootstyle="success")
            self.launch_button.pack(expand=True, padx=5, pady=5, ipadx=200, ipady=100)

            self.logout_button = ttk.Button(self.root, text="Log Out", bootstyle="danger", command=self.logout)
            self.logout_button.pack(expand=True, padx=5, pady=5, ipadx=50, ipady=20, side="bottom")





    def login_screen(self):
        """login screen"""
        ## 1. clear previous option buttons
        self.login_button_1.pack_forget()
        self.signup_button_1.pack_forget()
        self.option_frame.pack_forget()

        ## 2. Login widgets
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.login_style = ttk.Style()
        self.login_style.configure("Login.TLabel", font="Verdana 15 normal", foreground="white", background="#3b3a3a",
                                   relief="raised")

        self.username_label = ttk.Label(self.login_frame, style="Login.TLabel", text="Username:", anchor="center", justify="center")
        self.username_label.pack(expand=True, padx=5, pady=5, ipadx=500, ipady=20)

        self.username = ttk.StringVar()
        self.username.set("Enter Username Here")
        self.username_entry = ttk.Entry(self.login_frame, textvariable=self.username, bootstyle="primary")
        self.username_entry.pack(fill="y", expand=True, padx=20, pady=20, ipadx=500, ipady=10)

        self.password_label = ttk.Label(self.login_frame, style="Login.TLabel", text="Password:", anchor="center", justify="center")
        self.password_label.pack(expand=True, padx=5, pady=5, ipadx=500, ipady=20)

        self.password = ttk.StringVar()
        self.password_entry = ttk.Entry(self.login_frame, textvariable=self.password, show="*", bootstyle="primary")
        self.password_entry.pack(fill="y", expand=True, padx=20, pady=20, ipadx=500, ipady=10)

        self.bottom_frame = ttk.Frame(self.login_frame)
        self.bottom_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.login_button_2 = ttk.Button(self.bottom_frame, command=self.login, bootstyle="primary", text="Log In")
        self.login_button_2.pack(expand=True, padx=5, pady=5, ipadx=500, ipady=20, side="left")

        self.back_button = ttk.Button(self.bottom_frame, bootstyle="secondary", text="Back", command=self.back)
        self.back_button.pack(side="left", expand=True, padx=5, pady=5, ipadx=500, ipady=10)

    def login(self):
        """logs user in"""

        ## 1. load data
        with open("accounts.json", "r") as file:
            accounts = json.load(file)

        ## 2. conditional statements
        if self.username.get() in accounts:
            ## 2.a if everything is right
            if self.password.get() == accounts[self.username.get()]["password"]:
                self.logged_in_state.set(f"Logged in as {self.username.get()}")
                tkinter.messagebox.showinfo("Success", f"Successfully logged in as {self.username.get()}!")


                # back to home
                self.back()

            ## 2.b if something's wrong
            else:
                tkinter.messagebox.showerror("Failure", "Invalid username or password!")
        else:
            tkinter.messagebox.showerror("Failure", "Invalid username or password!")

        ## 3. clearing stringvar
        self.password.set("")
        self.username.set("")




    def signup_screen(self):
        ## 1. clear previous option buttons
        self.login_button_1.pack_forget()
        self.signup_button_1.pack_forget()
        self.option_frame.pack_forget()

        ## 2. sign up widgets
        self.signup_frame = ttk.Frame(self.root)
        self.signup_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.signup_style = ttk.Style()
        self.signup_style.configure("Signup.TLabel", font="Verdana 15 normal", foreground="white", background="#3b3a3a",
                                   relief="raised")

        self.username_label = ttk.Label(self.signup_frame, style="Signup.TLabel", text="Username:", anchor="center",
                                        justify="center")
        self.username_label.pack(expand=True, padx=5, pady=5, ipadx=500, ipady=20)

        self.username = ttk.StringVar()
        self.username.set("Enter Username Here")
        self.username_entry = ttk.Entry(self.signup_frame, textvariable=self.username, bootstyle="primary")
        self.username_entry.pack(fill="y", expand=True, padx=20, pady=20, ipadx=500, ipady=10)

        self.password_label = ttk.Label(self.signup_frame, style="Signup.TLabel", text="Password:", anchor="center",
                                        justify="center")
        self.password_label.pack(expand=True, padx=5, pady=5, ipadx=500, ipady=20)

        self.password = ttk.StringVar()
        self.password_entry = ttk.Entry(self.signup_frame, textvariable=self.password, show="*", bootstyle="primary")
        self.password_entry.pack(fill="y", expand=True, padx=20, pady=20, ipadx=500, ipady=10)

        self.bottom_frame = ttk.Frame(self.signup_frame)   #for aesthetic purposes
        self.bottom_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.signup_button_2 = ttk.Button(self.bottom_frame, command=self.signup, bootstyle="primary", text="Sign Up")
        self.signup_button_2.pack(expand=True, padx=5, pady=5, ipadx=500, ipady=20, side="left")

        self.back_button = ttk.Button(self.bottom_frame, bootstyle="secondary", text="Back", command=self.back)
        self.back_button.pack(side="left", expand=True, padx=5, pady=5, ipadx=500, ipady=10)

    def signup(self):
        """signup stuff"""
        ## 1. Dump into json file
        account_data = {self.username.get(): {"password" : self.password.get()}}
        with open("accounts.json", "w") as file:
            json.dump(account_data, file, indent=4)

        ## 2. Messagebox
        tkinter.messagebox.showinfo(title="Success", message=f"You have successfully signed up as {self.username.get()}!")

        ## 3. clearing stringvar
        self.username.set('')
        self.password.set('')

        ## 4. back to title screen
        self.back()

    def back(self):
        """Gets user back to the title screen"""
        self.unpack_all(self.root)
        self.title_screen()



    def unpack_all(self, container):
        """pack_forget() s all widget except the title widget"""

        for widget in container.winfo_children():

            if isinstance(widget, tk.Widget):
                widget.pack_forget()
            elif isinstance(widget, tk.Frame):
                self.unpack_all(widget)
                widget.pack_forget()

    def logout(self):

        confirm = tkinter.messagebox.askyesno("Confirmation", "Do you really want to log out?")
        if confirm:
            self.logged_in_state.set("Logged In as Guest")

        self.back()




if __name__ == "__main__":
    root = ttk.Window(themename="cyborg")
    TitleScreen(root)