import hashlib
import os

def read_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "day4.dat")
    with open(file_path) as f:
        return f.read().strip(  )

def solve(puzzle_input, zeros):
    target = "0" * zeros
    encoded_input = puzzle_input.encode()
    i = 0
    while True:
        h = hashlib.md5(encoded_input + str(i).encode()).hexdigest()

        if h.startswith(target):
            return i
        
        i += 1



if __name__ == "__main__":
    data = read_data()
    print(f"part1: {solve(data , 5)}")
    print(f"part2: {solve(data , 6)}")

# TODO: optimize!