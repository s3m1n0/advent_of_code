import os
def read_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "day5.dat")   
    with open(file_path) as f:
        return [line.strip() for line in f]

BAD_COMBOS = ("ab" , "cd" , "pq" , "xy")
VOWELS = set("aeiou")



def part1(puzzle_input):    
    nice_word_count = 0
    for word in puzzle_input:
        word_length = len(word)
        at_least_3_vowels = (1 for char in word if char in VOWELS) 
        forbidden_combos = (word[i] + word[i+1] in BAD_COMBOS for i in range(word_length - 1))
        letter_appears_twice = (word[i] == word[i+1] for i in range(word_length - 1))

        if not any(forbidden_combos) and sum(at_least_3_vowels) >= 3 and any(letter_appears_twice):
            nice_word_count += 1
        
    return nice_word_count
            
                




def part2(puzzle_input):
    nice_word_count = 0
    for word in puzzle_input:
        word_length = len(word)
        has_sandwiched_letter = (word[i] == word[i + 2] for i in range(word_length - 2))
        has_repeated_pair = False
        seen = {}
        for i in range(len(word) - 1):
            pair = word[i:i+2]
            if pair in seen and i - seen[pair] > 1:
                has_repeated_pair = True
            seen.setdefault(pair, i)
        if has_repeated_pair and any(has_sandwiched_letter):
            nice_word_count += 1

    return nice_word_count
    



if __name__ == "__main__":
    data = read_data()
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")