import tkinter as tk


class MyApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("650x400")
        self.root.resizable(False, False)
        self.root.title("حدس عدد")

        self.lblTitle = tk.Label(self.root, text="عدد را حدس بزنید")
        self.lblTitle.pack(pady=(60, 20))

        self.ent = tk.Entry(self.root, justify="right")
        self.ent.pack()

        self.lblStatusVar = tk.StringVar()
        self.lblStatus = tk.Label(self.root, textvariable=self.lblStatusVar)
        self.lblStatus.pack()

        self.calcBtn = tk.Button(self.root, text="!!!حدس بزن")
        self.calcBtn.pack()

    def run(self):
        self.root.mainloop()


app = MyApp()

app.run()
