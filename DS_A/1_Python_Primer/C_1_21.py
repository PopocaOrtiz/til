"""
repeteadly reads lines from standar input until EOF, then prints in reverse
order
"""

lines: list[str] = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

for index, _ in enumerate(lines):
    print(lines[-(index + 1)])
