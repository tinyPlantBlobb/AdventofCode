pub fn run(input: String) {
    let lines = input.split_whitespace();
    for i in lines {
        let (x, y) = i.split_once(',').expect("nothing to split");

        println!("{} {}", x, y);
    }
}
