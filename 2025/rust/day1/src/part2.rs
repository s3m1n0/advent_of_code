pub fn part_2() {
    let operation_numbers = parse_file();
    count_zero_hits(&operation_numbers);
    // println!("{:?}" , numbers);
}

fn count_zero_hits(operations: &[i32]) {
    let mut solution: i32 = 0;

    let mut password: i32 = 50;

    for op in operations {
        for _ in 0..op.abs() {
            if op.is_positive() {
                password = (password + 1).rem_euclid(100);
            } else {
                password = (password - 1).rem_euclid(100);
            }

            if password == 0 {
                solution += 1;
            }
        }
    }

    println!("{}", solution);
}

fn parse_file() -> Vec<i32> {
    std::fs::read_to_string("../data/day1/data.dat")
        .unwrap()
        .lines()
        .map(|line| {
            let operator_sign = line.chars().next().unwrap();
            let number: i32 = line[1..].parse().unwrap();
            match operator_sign {
                'L' => -number,
                'R' => number,
                _ => panic!("bad data"),
            }
        })
        .collect()
}
