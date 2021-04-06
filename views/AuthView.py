from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.AuthController import AuthController

class AuthView:

    next  = None
    def load(self):
        self.window = Tk()
        self.window.title("Text Deection Application")
        self.window.geometry = ("400x300")
        tab_control = ttk.Notebook(self.window)


        self.login_tab = Frame(tab_control,bg="grey",padx=25,pady=25)
        self.register_tab = Frame(tab_control,bg="grey",padx=25,pady=253)

        tab_control.add(self.login_tab, text="Login")
        tab_control.add(self.register_tab, text = "Register")

        self.login()
        self.register()

        tab_control.grid()

        self.window.mainloop()

    def register(self):
        window = self.register_tab

        # Name label and entry
        nl = Label(window, text="Name",  font = ("Monotype Corsiva Bold", 12))
        nl.grid(row=0, column=0)

        ne = Entry(window, width=20)
        ne.grid(row=0, column=2)

        # username label and entry
        ul = Label(window, text="Username", font = ("Monotype Corsiva Bold", 12))
        ul.grid(row=1, column=0)

        ue = Entry(window, width=20)
        ue.grid(row=1, column=2)

        #  password name and entry
        pl = Label(window, text="Password", font = ("Monotype Corsiva Bold", 12))
        pl.grid(row=2, column=0)

        pe = Entry(window, show="*", width=20)
        pe.grid(row=2, column=2)

        # email label and entry
        el = Label(window, text="Email", font = ("Monotype Corsiva Bold", 12))
        el.grid(row=3, column=0)

        ee = Entry(window, width=20)
        ee.grid(row=3, column=2)

        # Phone label and entry
        phl = Label(window, text="Phone", font = ("Monotype Corsiva Bold", 12))
        phl.grid(row=4, column=0)

        phe = Entry(window, width=20)
        phe.grid(row=4, column=2)

        b1 = Button(window, text="Register",command = lambda: self.registerControl(ne.get(),
                                                                              phe.get(),ee.get(),
                                                                              ue.get(),pe.get()
                                                                              ),  bg = "black", fg = "white", padx=5, pady=5)
        b1.grid(row=5, column=1,padx = 5, pady = 20)

    def login(self):
        window = self.login_tab

        ul = Label(window,text="Username",font = ("Monotype Corsiva Bold", 12))
        ul.grid(row=0,column=0)

        ue = Entry(window,width=20)
        ue.grid(row=0,column=2)

        pl = Label(window, text="Password",font = ("Monotype Corsiva Bold", 12))
        pl.grid(row=1, column=0)

        pe = Entry(window, show="*", width=20)
        pe.grid(row=1, column=2)

        b1 = Button(window,text="Login",command=lambda: self.loginControl( ue.get() ,pe.get()),  bg = "black", fg= "white" ,padx=5,pady=5)
        b1.grid(row=2,column=1,pady=5)

    def loginControl(self,username,password):
        ac = AuthController()
        message = ac.login(username,password)
        if message == 1:
            self.window.destroy()
            # print("window destroyed")
            self.next()
        else:
            messagebox.showinfo('Message',message)

    def registerControl(self,name,phone,email,username,password):

        ac = AuthController()
        message = ac.register(name,phone,email,username,password)
        messagebox.showinfo('Message', message)

if __name__ == '__main__':
    av = AuthView()