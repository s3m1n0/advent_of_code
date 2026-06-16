fn main() {
    part_1();
    part_2();
}


pub fn part_1() {
    let operations = parse_file();

    let mut solution = 0;

    let mut password = 50;

    for i in operations {
        password = (password + i).rem_euclid(100);

        if password == 0 {
            solution += 1;
        }
    }

    println!("{}", solution)
}

pub fn part_2() {
    let operations = parse_file();

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
pub fn parse_file() -> Vec<i32> {
    std::fs::read_to_string("../data/day1.dat")
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
