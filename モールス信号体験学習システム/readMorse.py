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

    #root.mainloop()

    while True:#この部分でボタンの判定を行う。
        if check_pin == 1:#オン
            #On--------------
            if started == False:#押し始めの時間を記録する。
                #firstTimeOfOn----------------
                onTime = round(time.time()*100)
                offedTime = round(time.time()*100)#エラー回避
                started = True
            else:#押されている時間を記録する
                nowTime = round(time.time()*100)
                if 60 < nowTime - onTime:#棒の長さ分押された時
                    onSecondLED()#二つ目のLEDを点灯させる
            onSecondLED()
            onBuzer()
            if check_pin == 0:#オフ
                #Off-----------------
                offSingleLED()
                offSecondLED()
                offBuzer()
                started = False
                offedTime = round(time.time()*100)
                #押されてた時間を調べる
                if offedTime - onTime < 60:#・
                    typingWord.append('.')
                elif 60 <= offedTime - onTime:#ー                    
                    typingWord.append('-')
        elif check_pin == 0:
        #押されていなかった時間を調べる
            nowTime = round(time.time()*100)
            if nowTime - offedTime > 60:#１文字分の空白が空いた時
                typedWord = mI.morseReader(typingWord)#判定
                with open("data.txt",'a') as file:
                    file.write(typedWord)
                typingWord = []#次の文字の判定用に初期化
