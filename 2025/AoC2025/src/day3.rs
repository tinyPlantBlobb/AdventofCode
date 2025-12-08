pub fn run(input: String) {
    let battery_lines = input.split_whitespace();
    println!("{:?}", battery_lines);
    let mut joltage_sum: i64 = 0;
    for i in battery_lines {
        let mut result = String::from("");
        let largest_char = largest_first(i.to_string());
        let remainder = String::from(i);
        String::from(i).remove(largest_char.1);
        let second = largest_first(remainder);
        if largest_char.1 > second.1 {
            result.push(second.0);
            result.push(largest_char.0);
        } else {
            result.push(largest_char.0);
            result.push(second.0);
        }
        println!("{}, {:?} , {:?} ", result, largest_char, second);
        joltage_sum += i64::from_str_radix(&result, 10).expect("no number");
    }
    println!("{}", joltage_sum);
}

fn largest_first(input: String) -> (char, usize) {
    println!("{}", input);
    let mut largest = ('0', 0);
    for c in input.chars().enumerate() {
        if c.1 > largest.0 {
            largest = (c.1, c.0);
        }
    }
    return (largest.0, largest.1);
}
