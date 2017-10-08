import sys 
import tkinter
#classes
import manualMode as M
import autoMode as A

#ボタンが押されたらそれぞれのモードをスタートさせる
def manualModeStarter():
    print("Manual mode button pushed.")

def autoModeStarter():
    print("Automatic mode button pushed.")

def mainMenu():#起動時のメニュー画面。
    root = tkinter.Tk()
    root.title("ホームメニュー")

    titleLabel = tkinter.Label(root,text="Morse Study System")
    titleLabel.grid(row=0,column=0,columnspan=2)

    manualModeButton = tkinter.Button(root,text="手動モード",command=lambda:manualModeStarter())
    manualModeButton.grid(row=1,column=0,padx=5,columnspan=1)

    autoModeButton = tkinter.Button(root,text="自動モード",command=lambda:autoModeStarter())
    autoModeButton.grid(row=1,column=1,padx=5)

    root.mainloop()

    print("Main menu opened.")

if __name__ == "__main__":#テスト用
    print("System started.")
    mainMenu()