import sys
import tkinter
#class
import readMorse as rM
import morseInfo as mI


def manualModeMenu():
    def gpioController():#この関数を経由してTkinterとGPIOを組み合わせる
        print("Turn on the gpioController.")
        rM.readMain()

    def quit():#閉じる。
        root.destroy()
        print("Manual mode menu closed.")

    print("Opening the menu of manual mode.")

    root = tkinter.Tk()
    root.title("手動モード")

    titleLabel = tkinter.Label(root,text="Morse Study System")
    titleLabel.grid(row=0,column=0)

    typeStartButton = tkinter.Button(root,text="スタート",command=lambda:gpioController())
    typeStartButton.grid(row=1,column=0)

    closeButton = tkinter.Button(root,text="戻る",command=lambda:quit())
    closeButton.grid(row=2,column=0)

    root.mainloop()

    print("Menu of manual mode opened.")
