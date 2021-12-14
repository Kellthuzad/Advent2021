from pathlib import Path
import os

def main():
    for num in range(1, 26, 1):
        checkForDayAndMakeIfNeeded(num)


def checkForDayAndMakeIfNeeded(num):
    my_file = Path(f"./Day{num:02}")
    if not my_file.is_dir():
        os.mkdir(f"./Day{num:02}")
        f = open(f"./Day{num:02}/Solution.py", "w")
        f.write("""
def main():
    filehandle = open("./Day14/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
        print(line)

main()
        """)
        f.close()

        i = open(f"./Day{num:02}/input.txt", "a")
        i.write("hi paul")
        i.close()

main()