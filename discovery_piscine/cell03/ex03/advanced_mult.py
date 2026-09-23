import sys
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i<= 10:
        line = f"Table de {i}:"
        j = 0
        while j <= 10:
            line += f" {i * j}"
            j += 1
        print(line)
        i+=1