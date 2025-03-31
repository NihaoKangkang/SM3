from SM import *

if __name__ == "__main__":
    inputData = 'tempString'
    while inputData:
        inputData = input('Input string or file location need to calculate sm3(press ENTER to abort): ')
        if inputData != '':
            print('SM3 result: ', sm3_result(inputData))