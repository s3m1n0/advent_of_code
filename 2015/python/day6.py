import os
def read_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "day6.dat")   
    with open(file_path) as f:
        t = []
        for instruction in f:
            if instruction.startswith("turn off"):
                op = "off"
                coords = instruction[len("turn off"):]
            elif instruction.startswith("turn on"):
                op = "on"
                coords = instruction[len("turn on"):]
            else:
                op = "switch"
                coords = instruction[len("toggle"):]
            start,end = coords.strip().split(" through ")
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            t.append((op , (x1 , y1) , (x2 , y2)))
        return t

def generate_coords(start , end):
    x1,y1 = start
    x2,y2 = end
    for i in range(x1 , x2 + 1):
        for j in range(y1, y2 + 1):
            yield (i , j)

def part1(puzzle_input):
    grid = [[False] * 1000 for _ in range(1000)]   
    for instruction in puzzle_input:
        op,start,end = instruction
        for x,y in generate_coords(start , end):
            match op:
                case "off": grid[x][y] = False
                case "on": grid[x][y] = True
                case "switch": grid[x][y] = not grid[x][y]
    return sum(row.count(True) for row in grid)
                
    

def part2(puzzle_input):
    grid = [[0] * 1000 for _ in range(1000)]   
    for instruction in puzzle_input:
        op,start,end = instruction
        for x,y in generate_coords(start , end):
            match op:
                case "off": grid[x][y] = max(0, grid[x][y] - 1)
                case "on": grid[x][y] += 1
                case "switch": grid[x][y] += 2
    return sum(sum(row) for row in grid)
                



if __name__ == "__main__":
    data = read_data()
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")