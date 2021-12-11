
def main():
    filehandle = open("./Day03/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    
    parseBinary(lines)
        

def parseBinary(input):
    tracker = [0] * len(input[0])

    for line in input:
        x = 0
        for char in line:
            if char == '1':
                if tracker[x]:
                    tracker[x] += 1
                else:
                    tracker[x] = 1
            else:
                tracker[x] += 0
            x += 1
    gamma = ""
    epsilon = ""
    for num in tracker:
        
        if len(input) - num <= num:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"


    gamma_list = input
    for i in range(len(line)):
        one_list  = []
        zero_list = []
        for line in gamma_list:
            if line[i] == "0":
                zero_list.append(line)
            else:
                one_list.append(line)
        
        if len(one_list) >= len(zero_list):
            gamma_list = one_list
        else:
            gamma_list = zero_list

        if len(gamma_list) == 1:
            print(gamma_list)

    eps_list = input
    for i in range(len(line)):
        one_list  = []
        zero_list = []
        for line in eps_list:
            if line[i] == "0":
                zero_list.append(line)
            else:
                one_list.append(line)
        
        if len(one_list) < len(zero_list):
            eps_list = one_list
        else:
            eps_list = zero_list

        if len(eps_list) == 1:
            print(eps_list)
            
            break

    print(int(eps_list[0],2) * int(gamma_list[0], 2))
            



 

main()