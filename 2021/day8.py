import sys

file = open('day8_input.txt', 'r')
fileLines = file.readlines()

digits = [x.split('|') for x in fileLines]

digitsAfterList = [x[1].split() for x in digits]
digitsBeforeList = [x[0].split() for x in digits]

# count 1,4,7,8 (1 -> 2, 4 -> 4, 7 -> 3, 8 -> 7)

# we can find out which is 1, 4, 7, 8
# 0 -> _ _ 1[0] !4[2] 1[1] _ (6 chars, 1[0] in 3rd spot, 1[1] in 5th spot, 4[2] not in 4th spot)
# 1 -> 2 digits
# 2 -> _ 1[0] _ _ _ (5 chars, 1[0] in 2nd spot)
# 3 -> _ 1[0] _ 1[1] _ (5 chars, 1[0] in 2nd spot, 1[1] in 4th spot)
# 4 -> bcdf, 4 digits;
# 5 -> _ _ _ 1[1] _ (5 chars, 1[1] in 4th spot)
# 6 -> _ _ _ _ 1[1] _ (6 chars, 1[1] in 5th spot)
# 7 -> 3 digits
# 8 -> 7 digits
# 9 -> _ _ 1[0] 4[2] 1[1] _ (6 chars, 1[0] in 3rd spot, 1[1] in 5th spot, 4[2] in 4th spot)

digitsSum = 0
for i in range(len(digitsBeforeList)):
    easyDigits = dict()
    digitsBefore = digitsBeforeList[i]
    for digits in digitsBefore:
        if len(digits) == 2: # 1
            easyDigits[1] = digits
        if len(digits) == 4: # 4
            easyDigits[4] = digits

    digitsAfter = digitsAfterList[i]
    # digitsAfter = list[abc, abd]...
    # digits = abc
    numStr = ''
    for digits in digitsAfter:
        if len(digits) == 2:
            numStr += '1'
            continue
        if len(digits) == 4:
            numStr += '4'
            continue
        if len(digits) == 3:
            numStr += '7'
            continue
        if len(digits) == 7:
            numStr += '8'
            continue

        oneDigit = easyDigits[1]
        fourDigit = easyDigits[4]
        if len(digits) == 6:
            # 0, 6, 9
            # 0 -> _ _ 1[0] !4[2] 1[1] _ (6 chars, 1[0] in 3rd spot, 1[1] in 5th spot, 4[2] not in 4th spot)
            # 0 -> both oneDigits and 3 from 4
            # 6 -> _ _ _ _ 1[1] _ (6 chars, 1[1] in 5th spot)
            # 6 -> only one oneDigit
            # 9 -> _ _ 1[0] 4[2] 1[1] _ (6 chars, 1[0] in 3rd spot, 1[1] in 5th spot, 4[2] in 4th spot)
            # 9 -> both oneDigits and 4 from 4
            if oneDigit[0] in digits and oneDigit[1] in digits:
                numFromFour = 0
                for d in fourDigit:
                    if d in digits:
                        numFromFour += 1

                if numFromFour == 3:
                    numStr += '0'
                    continue
                elif numFromFour == 4:
                    numStr += '9'
                    continue
            else:
                numStr += '6'
                continue

        if len(digits) == 5:
            # 2 -> _ 1[0] _ _ _ (5 chars, 1[0] in 2nd spot)
            # 2 -> one oneDigit and 2 from 4
            # 3 -> _ 1[0] _ 1[1] _ (5 chars, 1[0] in 2nd spot, 1[1] in 4th spot)
            # 3 -> both one digits
            # 5 -> _ _ _ 1[1] _ (5 chars, 1[1] in 4th spot)
            # 5 -> one oneDigit and 3 from 4
            # 5 chars, contains 1[0] and not 1[1]
            if oneDigit[0] in digits and oneDigit[1] in digits:
                numStr += '3'
                continue
            else:
                numFromFour = 0
                for d in fourDigit:
                    if d in digits:
                        numFromFour += 1

                if numFromFour == 2:
                    numStr += '2'
                    continue
                elif numFromFour == 3:
                    numStr += '5'
                    continue

        print('test')

    print(numStr)

    digitsSum += int(numStr)

print(digitsSum)






