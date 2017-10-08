def getMorse(wannaConvList):#アルファベットをモールス信号に変換して返す
    print("Using the getMorse.")
    morseDict = {
        'a':"・－",     'b':"ー・・・",
        'c':"ー・－・",  'd':"ー・・",
        'e':"・",       'f':"・・－・",
        'g':"ーー・",   'h':"・・・・",
        'i':"・・",     'j':"・－－－",
        'k':"ー・－",   'l':"・－・・",
        'm':"ーー",     'n':"ー・",
        'o':"ーーー",   'p':"・－－・",
        'q':"ーー・－", 'r':"・－・",
        's':"・・・",   't':"ー",
        'u':"・・－",   'v':"・・・－",
        'w':"・－－",   'x':"ー・・－",
        'y':"ー・－－", 'z':"ーー・・",
        '1':"・－－－－",'2':"・・－－－",
        '3':"・・・－－",'4':"・・・・－",
        '5':"・・・・・",'6':"ー・・・・",
        '7':"ーー・・・",'8':"ーーー・・",
        '9':"ーーーー・",'0':"ーーーーー"
    }
    wordlength = len(wannaConvList)
    resultList = [0 for i in range(wordlength)]
    count = 0
    for i in wannaConvList:
        resultList[count] = morseDict[i]
        count = count + 1
    print(resultList)

    return resultList

def morseReader(typingWord):#未使用機能。モールス信号をアルファベットに変換して返す.
    wordLength2 = len(typingWord)
    if wordLength2 == 1:
        if typingWord[0] == '.':
            return 'E'
        elif typingWord[0] == '-':
            return 'T'
    elif wordLength2 == 2:
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                return 'I'
            elif typingWord[1] == '-':
                return 'A'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                return 'N'
            elif typingWord[1] == '-':
                return 'M'
    elif wordLength2 == 3:
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    return 'C'
                elif typingWord[2] == '-':
                    return 'U'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    return 'R'
                elif typingWord[2] == '-':
                    return 'W'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    return 'D'
                elif typingWord[2] == '-':
                    return 'K'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    return 'G'
                elif typingWord[2] == '-':
                    return 'O'
    elif wordLength2 == 4:#----------------------------------
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'H'
                elif typingWord[2] == '-':
                    if typingWord[3] == '.':
                        return 'F'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'L'
                elif typingWord[2] == '-':
                    if typingWord[3] == '.':
                        return 'P'
                    elif typingWord[3] == '-':
                        return 'J'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'B'
                    elif typingWord[3] == '-':
                        return 'X'
                elif typingWord[2] == '-':
                    if typingWord[3] == '.':
                        return 'C'
                    elif typingWord[3] == '-':
                        return 'Y'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'Z'
                    elif typingWord[3] == '-':
                        return 'Q'
        
    elif wordLength2 == 5:#----------------------------------
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            return '5'
                        elif typingWord[4] == '-':
                            return '4'
                    elif typingWord[3] == '-':
                        if typingWord[4] == '-':
                            return '3'
                elif typingWord[2] == '-':
                    if typingWord[3] == '-':
                        if typingWord[4] == '-':
                            return '2'
            elif typingWord[1] == '-':
                if typingWord[2] == '-':
                    if typingWord[3] == '-':
                        if typingWord[4] == '-':
                            return '1'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            return '6'
            elif typingWord[1] == '-':#'--'
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            return '7'
                    elif typingWord[3] == '-':
                        if typingWord[4] == '-':
                            return '0'
                elif typingWord[2] == '-':#'---'
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            return '8'
                    elif typingWord[3] == '-':
                        if typingWord[4] == '.':
                            return '9'
