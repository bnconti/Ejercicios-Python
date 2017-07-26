# Exercise 2.22: Interpret a code

"""
SAMPLE RUN:
....I like while loops!
....I like while loops!
....I like while loops!
....I like while loops!
....I like while loops!
Oh, no - the loop is over.
"""

import time
t0 = time.time()
while time.time() - t0 < 10:
    print("....I like while loops!")
    time.sleep(2)
print("Oh, no - the loop is over.")

# THE PROGRAM SAVES THE TIME WHEN IT STARTS RUNNING ON t0, AND LATER IT STARTS A LOOP THAT LASTS WHILE
# THE ACTUAL TIME MINUS t0 IS LESS THAN 10.

# time.sleep(2) PAUSES THE PROGRAM FOR 2 SECONDS.

# IF WE CHANGE THE "<" SIGN FOR THE ">" SIGN THE LOOP NEVER STARTS BECAUSE THE DIFFERENCE IS NEVER GREATER THAN
# 10 ON THESE CONDITIONS. BUT IF WE MADE THE COMPUTER WAIT FOR 10 SECONDS AND THEN EXECUTE THE LOOP IT WILL RUN
# INDEFINITELY.

