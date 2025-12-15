use std::env;
use std::fs;
pub mod day1;
pub mod day10;
pub mod day11;
pub mod day12;
pub mod day2;
pub mod day3;
pub mod day4;
pub mod day5;
pub mod day6;
pub mod day7;
pub mod day8;
pub mod day9;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day: String = args[1].clone();
    let mut puzzle_file: String = String::from("input/day");
    puzzle_file.push_str(&day);
    if args.len() > 2 {
        if &args[2] == "test" {
            puzzle_file.push_str("_test");
        }
    }
    let puzzle_input = fs::read_to_string(puzzle_file).expect("could not read file ");
    match day.as_str() {
        "1" => day1::run(puzzle_input),
        "2" => day2::run(puzzle_input),
        "3" => day3::run(puzzle_input),
        "4" => day4::run(puzzle_input),
        "5" => day5::run(puzzle_input),
        "6" => day6::run(puzzle_input),
        "7" => day7::run(puzzle_input),
        "8" => day8::run(puzzle_input),
        "9" => day9::run(puzzle_input),
        "10" => day10::run(puzzle_input),
        "11" => day11::run(puzzle_input),
        "12" => day12::run(puzzle_input),
        _ => println!("no code found"),
    }
}
