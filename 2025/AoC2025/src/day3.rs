pub fn run(input: String) {
    let battery_lines = input.split_whitespace();
    println!("joltage sum {}", part1(battery_lines.clone()));
    println!("more joltalge {}", part2(battery_lines.clone()));
}
fn part1(battery_lines: std::str::SplitWhitespace) -> i64 {
    let mut joltage_sum: i64 = 0;
    for i in battery_lines {
        let mut result = String::from("");
        let mut start_input = i.to_string();
        start_input.truncate(i.len() - 1);
        let largest_char = largest_first(start_input);
        let mut remainder = String::from(i);
        remainder = remainder.split_off(largest_char.1 + 1);
        let second = largest_first(remainder);

        result.push(largest_char.0);
        result.push(second.0);

        joltage_sum += i64::from_str_radix(&result, 10).expect("no number");
    }

    return joltage_sum;
}

fn part2(battery_lines: std::str::SplitWhitespace) -> i64 {
    let mut joltage_sum: i64 = 0;
    for i in battery_lines {
        let mut result = String::from("");
        let mut start_input = i.to_string();
        let remain = start_input.split_off(start_input.len() - 11);
        let mut remainder = remain.chars();
        for k in (1..12).rev() {
            let currentpart = start_input.clone();
            let largest_char = largest_first(currentpart);
            start_input.push(remainder.next().expect("index error"));

            start_input = start_input.split_off(largest_char.1 + 1);
            result.push(largest_char.0);
        }
        let largest_char = largest_first(start_input);
        result.push(largest_char.0);
        println!("{}", result);
        joltage_sum += i64::from_str_radix(&result, 10).expect("no number");
    }

    return joltage_sum;
}

fn largest_first(input: String) -> (char, usize) {
    let mut largest = ('0', 0);
    for c in input.chars().enumerate() {
        if c.1 > largest.0 {
            largest = (c.1, c.0);
        }
    }
    return (largest.0, largest.1);
}
