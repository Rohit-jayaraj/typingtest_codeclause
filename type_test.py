import time
import random

sentences = ["the quick brown fox jumps over the little lazy dog.","My sister has already made a big cake.","I have known Michael since high school.",
             "My baby has slept since all night.","I have studied at home for one hour."]

def wpm(tim , num):
    words = float(num/5)
    minutes = float(tim/60)
    wpm = int(words / minutes)
    return wpm

sen = random.choice(sentences)

print("Type the following sentence as fast as you can:")
print(sen)

start = time.time()
inp = input()
if inp==sen: 
    end = time.time()
while inp!=sen:
    inp = input("Incorrect sentence , try again")
    if inp==sen:
        end = time.time()

total_time = end - start

speed = wpm(total_time , len(sen))

print("Time taken:",total_time,"seconds")
print("Typing speed:",speed,"words per minute")

