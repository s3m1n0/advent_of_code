
def read_data():
    data = []
    with open("../data/day1/data.dat" , "r") as f:
        for operator in f:
            if operator[:1] == "L":
                data.append(-int(operator[1:]))
            else:
                data.append(int(operator[1:]))
    return data

def part1(operator_list):
    
    password = 50
    solution = 0

    for operator in operator_list:
        password = (password + operator) % 100
        if password == 0:
            solution += 1

    print(solution)

def part2(operator_list):
    
    password = 50
    solution = 0

    for operator in operator_list:
        for _ in range(abs(operator)):

            step = 1 if operator > 0 else -1       

            password = (password + step) % 100

            if password == 0:
                solution += 1

    print(solution)




if __name__ == "__main__":
    data = read_data()
    part1(data)
    part2(data)