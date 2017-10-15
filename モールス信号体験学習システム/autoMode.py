import sys
import tkinter
import time
#classes
import morseInfo as mI

def autoModeMenu():#自動モードのメニュー。
    def morseConverter():#入力されたアルファベットを外部でモールス信号にして来て表示する
        print("Turn on the morseConverter.")
        #共通処理
        wannaConv = inputArea.get()
        wannaConvList = list(wannaConv)
        morseWordList = mI.getMorse(wannaConvList)
        rowCount = 3
        for m in range(len(wannaConvList)):
            labelText = wannaConvList[m] + "：" + morseWordList[m]
            morseLabel = tkinter.Label(text=labelText)
            morseLabel.grid(row=rowCount,column=0,columnspan=2)
            rowCount = rowCount +1
        print("morseConverter finished.")

    def morseTransmitter():#上に加え、自動で発信させる
        print("Turn on the morseTransmitter.")
        #共通処理
        wannaConv = inputArea.get()
        wannaConvList = list(wannaConv)
        morseWordList = mI.getMorse(wannaConvList)
        rowCount = 3
        howManyWords = len(wannaConvList)
        for m in range(howManyWords):
            labelText = wannaConvList[m] + "：" + morseWordList[m]
            morseLabel = tkinter.Label(text=labelText)
            morseLabel.grid(row=rowCount,column=0,columnspan=2)
            rowCount = rowCount +1
        #自動で発信する処理
        #まずGPIOのセットアップを行う
        #短い文でオンオフするための関数
        def onLED():
            wipi.digitalWrite(singleLed_pin,1)
        def offLED():
            wipi.digitalWrite(singleLed_pin,0)
        def onBuzer():
            wipi.digitalWrite(buzer_pin,1)
        def offBuzer():
            wipi.digitalWrite(buzer_pin,0)
        singleLed_pin = 19
        buzer_pin = 13
        
        for n in morseWordList:
            nowMorse = list(n)#１文字分のモールス信号を一文字ごとに配列に格納。
            #wannaConvList->["S","O"]
            #morseWordList->["・・・","ーーー"]
            #nowMorse->["・","・","・"]
            #n->"・・・"
            #h->"・"
            for h in nowMorse:
                if h == '・':
                    onLED()
                    onBuzer()
                    time.sleep(0.2)
                    offLED()
                    offBuzer()
                elif h== 'ー':
                    onLED()
                    onBuzer()
                    time.sleep(0.6)
                    offLED()
                    offBuzer()
                elif h == '_':
                    time.sleep(1.2)#単語間の空白。1.2+0.2秒待機する。
                time.sleep(0.2)#点か棒同士の間の空白。
            time.sleep(0.6)#１文字同士の間の空白。
        print("morseConverter finished.")

    def quit():#閉じる・戻るボタン用
        root.destroy()
        print("Auto mode menu closed.")

    root = tkinter.Tk()
    root.title("自動モード")

    explanatoryLabel = tkinter.Label(root,text="モールス信号に変換したい文字を入力してください")
    explanatoryLabel.grid(row=0,column=0,columnspan=2)
    inputArea = tkinter.Entry(root,width=50)
    inputArea.grid(row=1,column=0,columnspan=2)
    enterButton = tkinter.Button(root,text="変換",command=lambda:morseConverter())
    enterButton.grid(row=2,column=0,columnspan=1)
    callOutButton = tkinter.Button(root,text="発信",command=lambda:morseTransmitter())
    callOutButton.grid(row=2,column=1,columnspan=1)
    
    morseLabel = tkinter.Label(root,text="")

    root.mainloop()

if __name__ == "__main__":#テスト用
    autoModeMenu()
