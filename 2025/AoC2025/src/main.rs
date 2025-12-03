use std::env;
use std::fs;
pub mod day1; pub mod day2;pub mod day3;
fn main() {
    let args: Vec<String> = env::args().collect();
    let day :String = args[1].clone();
    let mut puzzle_file : String = String::from("input/day");
    puzzle_file.push_str(&day);
    if args.len() > 2{
        if &args[2] == "test"{
         puzzle_file.push_str("_test");
        }
    }
    let puzzle_input= fs::read_to_string(puzzle_file).expect("could not read file ");
    match day.as_str() {
        "1"=> day1::run(puzzle_input),
        "2"=> day2::run(puzzle_input),
        _=>println!("no code found"),
    }
}
