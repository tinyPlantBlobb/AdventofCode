pub fn run(input: String) {
    let mut presents_and_trees: Vec<&str> = input.split("\n\n").collect();
    let trees: Vec<&str> = presents_and_trees
        .remove(presents_and_trees.len() - 1)
        .trim_end()
        .split('\n')
        .collect();
    let present: Vec<i32> = presents_and_trees
        .iter()
        .map(|i| count_chars(i, '#'))
        .collect();
    let res: i32 = trees
        .iter()
        .map(|x| {
            let mut split_area = x.trim().split(':');
            let (area, num_presents) = (
                split_area.next().expect("no area"),
                split_area.next_back().expect("no presents found"),
            );
            let area_parts: i32 = area
                .split('x')
                .collect::<Vec<&str>>()
                .iter()
                .map(|a| i32::from_str_radix(a, 10).expect("not an area "))
                .collect::<Vec<i32>>()
                .iter()
                .product();
            let present_area: i32 = num_presents
                .split_whitespace()
                .collect::<Vec<&str>>()
                .iter()
                .zip(present.clone())
                .map(|a| i32::from_str_radix(a.0, 10).expect("present number invalid") * a.1)
                .collect::<Vec<i32>>()
                .iter()
                .sum();
            println!("{} {}", area_parts, present_area);
            if area_parts >= present_area {
                println!("area bigger 1");
                return 1;
            } else {
                println!("area smaller");
                return 0;
            }
        })
        .into_iter()
        .sum();
    println!("{}", res);
}

fn count_chars(test: &str, char: char) -> i32 {
    let mut result = 0;
    for c in test.chars() {
        if c == char {
            result += 1;
        }
    }
    return result;
}
