
numbers = []
for i in range(0, 100):
    numbers.append("prime")

for j in range(1, 100):
    for n  in range(j+j+1,100,j+1):
            if numbers[n] == "prime":
                numbers[n] = "normal"

for i in range(0, 100):
    numbers[i] = (f"{i+1} is {numbers[i]}")
    print(numbers[i])


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
