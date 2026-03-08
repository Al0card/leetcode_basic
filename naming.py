import sys

text = sys.argv[1]   # first argument after the script name


namo = (text.replace(" ", "_")).lower()
print(namo)