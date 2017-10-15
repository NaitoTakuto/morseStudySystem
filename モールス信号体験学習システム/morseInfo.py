def getMorse(wannaConvList):#アルファベットをモールス信号に変換して返す
    print("Using the getMorse.")
    morseDict = {
        'a':"・－",       'b':"ー・・・",
        'c':"ー・－・",    'd':"ー・・",
        'e':"・",         'f':"・・－・",
        'g':"ーー・",     'h':"・・・・",
        'i':"・・",       'j':"・－－－",
        'k':"ー・－",     'l':"・－・・",
        'm':"ーー",       'n':"ー・",
        'o':"ーーー",     'p':"・－－・",
        'q':"ーー・－",   'r':"・－・",
        's':"・・・",     't':"ー",
        'u':"・・－",     'v':"・・・－",
        'w':"・－－",     'x':"ー・・－",
        'y':"ー・－－",   'z':"ーー・・",
        '1':"・－－－－", '2':"・・－－－",
        '3':"・・・－－", '4':"・・・・－",
        '5':"・・・・・", '6':"ー・・・・",
        '7':"ーー・・・", '8':"ーーー・・",
        '9':"ーーーー・", '0':"ーーーーー",
        ' ':"・・・・・・",':':"－－－・・・",
        ';':"・・・・・－",',':"－－・・－－",
        '(':" －・－－・", ')':"－・－－・－",
        '^':"・・・・・－－"
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
            return 'e'
        elif typingWord[0] == '-':
            return 't'
    elif wordLength2 == 2:
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                return 'i'
            elif typingWord[1] == '-':
                return 'a'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                return 'n'
            elif typingWord[1] == '-':
                return 'm'
    elif wordLength2 == 3:
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    return 'c'
                elif typingWord[2] == '-':
                    return 'u'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    return 'r'
                elif typingWord[2] == '-':
                    return 'w'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    return 'd'
                elif typingWord[2] == '-':
                    return 'k'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    return 'g'
                elif typingWord[2] == '-':
                    return 'o'
    elif wordLength2 == 4:#----------------------------------
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'h'
                elif typingWord[2] == '-':
                    if typingWord[3] == '.':
                        return 'f'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'l'
                elif typingWord[2] == '-':
                    if typingWord[3] == '.':
                        return 'p'
                    elif typingWord[3] == '-':
                        return 'j'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'b'
                    elif typingWord[3] == '-':
                        return 'x'
                elif typingWord[2] == '-':
                    if typingWord[3] == '.':
                        return 'c'
                    elif typingWord[3] == '-':
                        return 'y'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        return 'z'
                    elif typingWord[3] == '-':
                        return 'q'
        
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
                elif typingWord[2] == '-':
                    if typingWord[3] == '-':
                        if typingWord[4] == '.':
                            return '('
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
    elif wordLength2 == 6:#----------------------------------
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            if typingWord[5] == '.':
                                return ' '
                            elif typingWord[5] == '-':
                                return ';'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            if typingWord[5] == '.':
                                return '\n'
        elif typingWord[0] == '-':
            if typingWord[1] == '.':
                if typingWord[2] == '-':
                    if typingWord[3] == '-':
                        if typingWord[4] == '.':
                            if typingWord[5] == '-':
                                return ')'
            elif typingWord[1] == '-':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        if typingWord[4] == '-':
                            if typingWord[5] == '-':
                                return ','
                elif typingWord[2] == '-':
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            if typingWord[5] == '.':
                                return ':'
    elif wordLength2 == 7:#----------------------------------
        if typingWord[0] == '.':
            if typingWord[1] == '.':
                if typingWord[2] == '.':
                    if typingWord[3] == '.':
                        if typingWord[4] == '.':
                            if typingWord[5] == '-':
                                if typingWord[6] == '-':
                                    return '^'                                            
    else:
        return '?'