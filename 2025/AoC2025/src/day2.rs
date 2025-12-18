use fancy_regex::Regex;
pub fn run(input: String) {
    let ranges: Vec<&str> = input.trim().split(",").collect();

    let mut res: i64 = 0;
    for range in ranges {
        let start_end: Vec<&str> = range.trim().split("-").collect();
        let start: &str = start_end.first().expect("no start");
        let end: &str = start_end.last().expect("no end");
        let range_iter = i64::from_str_radix(start, 10).expect("no number in start")
            ..(i64::from_str_radix(end, 10).expect("no int in end") + 1);

        res += range_iter
            .map(|x| {
                let id = &x.to_string();
                if id.len() % 2 != 0 {
                    return 0;
                };
                let regex = Regex::new(r"^(\d+)(\1)$").unwrap();
                if regex.is_match(id).expect("regex error") {
                    return x;
                }
                return 0;
            })
            .sum::<i64>();
    }
    println!("{}", res);
}
