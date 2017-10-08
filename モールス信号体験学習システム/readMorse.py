import time
import wiringpi as wipi
import tkinter
import sys
#classes
import morseInfo as mI
    

def readMain():#手動モードのメニュー。
    #短い文でオンオフするための関数
    def onSingleLED():
        wipi.digitalWrite(singleLed_pin,1)
    def offSingleLED():
        wipi.digitalWrite(singleLed_pin,0)
    def onSecondLED():
        wipi.digitalWrite(secondLed_pin,1)
    def offSecondLED():
        wipi.digitalWrite(secondLed_pin,0)
    def onBuzer():
        wipi.digitalWrite(buzer_pin,1)
    def offBuzer():
        wipi.digitalWrite(buzer_pin,0)

    singleLed_pin = 19
    secondLed_pin = 26
    buzer_pin = 13
    check_pin = 6

    wipi.pinMode(singleLed_pin,1)
    wipi.pinMode(secondLed_pin,1)
    wipi.pinMode(buzer_pin,1)
    wipi.pinMode(check_pin,0)

    wipi.wiringPiSetupGpio()

    started = False
    typingWord = []
    typedWord = []

    #未使用機能。読み取った信号を表示するためのウィンドウを用意。
    root = tkinter.Tk()
    root.title("手動発信中！")

    titleLabel = tkinter.Label(root,text="Morse Study System")
    titleLabel.grid(row=0,column=0)

    typeStartButton = tkinter.Label(root,text="Typed word comes in here.")
    typeStartButton.grid(row=1,column=0)

    root.mainloop()

    while True:#この部分でボタンの判定を行う。
        if check_pin == 1:
            #On--------------
            if started == False:
                #firstTimeOfOn----------------
                onTime = round(time.time()*100)
                started = True
                onSecondLED()
                onBuzer()
            else:
                nowTime = round(time.time()*100)
                pushingTime = nowTime - onTime
                if 50 < pushingTime:
                    onSecondLED()
            if check_pin == 0:
                #Off-----------------
                offSingleLED()
                offSecondLED()
                offBuzer()
                started = False
                offTime = round(time.time()*100)
                pushedTime = offTime - onTime
                #押されてた時間を調べる
                if pushedTime < 50:
                    #・
                    typingWord.append('.')
                elif pushedTime < 100:
                    #ー
                    typingWord.append('-')
                else:
                    #wordEnd
                    print(typingWord)
                    typedWord.append(mI.morseReader(typingWord))
                    typedWordLabel = tkinter.Label(root,text=typedWord)
                    typedWordLabel.grid(row=1,column=0)
                    