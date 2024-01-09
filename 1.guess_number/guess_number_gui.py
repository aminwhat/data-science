import tkinter as tk
import random


class MyApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.title("حدس عدد")

        self.resetGameBtn = tk.Button(
            self.root,
            text="+ بازی جدید",
            command=self.newGame,
        )
        self.resetGameBtn.pack()

        self.lblTitle = tk.Label(self.root, text="عدد را حدس بزنید")
        self.lblTitle.pack(pady=(60, 0))

        self.entVar = tk.StringVar()
        self.ent = tk.Entry(self.root, justify="right", textvariable=self.entVar)
        self.ent.pack()

        self.lblStatusVar = tk.StringVar()
        self.lblStatus = tk.Label(self.root, textvariable=self.lblStatusVar)
        self.lblStatus.pack()

        self.calcBtn = tk.Button(
            self.root,
            text="!!!حدس بزن",
            command=self.calcBtnOnPressed,
        )
        self.calcBtn.pack()

        self.exitBtn = tk.Button(self.root, text="خروج", command=exit)
        self.exitBtn.pack(pady=(10, 0))

    def calcBtnOnPressed(self):
        if len(self.entVar.get()) != 0:
            insertedVal: int = -1
            try:
                insertedVal = int(self.entVar.get())
            except:
                self.lblStatusVar.set("مقدار ورودی باید به صورت عددی باشد")
                insertedVal = -1

            if insertedVal >= 0:
                if insertedVal < 1 or insertedVal > 100:
                    self.lblStatusVar.set(
                        "مقدار ورودی باید بین بازه عددی 1 تا 100 باشد"
                    )
                else:
                    if insertedVal == self.randomNumber:
                        self.win()
                    elif insertedVal != self.randomNumber:
                        self.turnsToPlay = self.turnsToPlay - 1
                        if self.turnsToPlay <= 0:
                            self.lose()
                        else:
                            status: str = "کوچکتر"
                            if insertedVal > self.randomNumber:
                                status = "بزرگتر"

                            self.lblStatusVar.set(
                                "حدس غلط- عدد وارد شده "
                                + str(status)
                                + " از عدد مورد نظر میباشد"
                                + "\n شما"
                                + str(self.turnsToPlay)
                                + " فرصت دیگر برای بازی دارید"
                            )
            else:
                self.lblStatusVar.set("مقدار ورودی نمیتواند منفی باشد")
        else:
            self.lblStatusVar.set("مقدار ورودی نمیتواند خالی باشد")

    def newGame(self):
        self.randomNumber = random.randrange(1, 101)
        self.turnsToPlay = 5
        print(self.randomNumber)
        self.calcBtn.config(command=self.calcBtnOnPressed)
        self.lblStatusVar.set(
            "بازی شروع شد, " + str(self.turnsToPlay) + " فرصت دارید\nشروع کنید"
        )

    def win(self):
        self.calcBtn.config(command=self.win)
        self.lblStatusVar.set(
            "شما بردید :) \n عدد مورد نظر " + str(self.randomNumber) + " بود"
        )

    def lose(self):
        self.calcBtn.config(command=self.lose)
        self.lblStatusVar.set(
            "شما باختید :( \n عدد مورد نظر " + str(self.randomNumber) + " بود"
        )

    def run(self):
        self.newGame()
        self.root.mainloop()


app = MyApp()

app.run()
