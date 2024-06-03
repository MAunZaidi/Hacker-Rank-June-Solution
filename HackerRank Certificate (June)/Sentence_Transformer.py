#!/bin/python3

import math
import os
import random
import re
import sys

def transformSentence(sentence):
    sentence = sentence.strip()
    result = ""
    for index, current_word in enumerate(sentence):
        if(index==0):
            result+=current_word
        elif current_word==' ':
            result += current_word
        else:
            previous_value = sentence[index-1]            
            if(previous_value==' '): 
                result+=current_word    
            elif(previous_value.lower()<current_word.lower()): 
                result+=current_word.upper()
            elif(previous_value.lower()>current_word.lower()): 
                result += current_word.lower()
            else:
                result += current_word 
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()