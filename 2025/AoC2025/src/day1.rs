pub fn run(input:String){
    let rotation = input.split("\n").collect::<Vec<&str>>();
    let mut position = 50;
    println!("{}", rotation[0]);
    let mut result1 = 0;
    let mut result2 =0;
    for l in rotation {
        if l.len()>1{
            println!("{}" ,l);
            let (direction_char,clicks) = l.split_at(1);
            let direction :Result<i64, i64>= match direction_char {
                "L" => Ok(-1),
                "R"=> Ok(1),
                _ => Err(0),
            };
            let prev_position = position;
            let position_between = (position + direction.expect("no direction given") *i64::from_str_radix(clicks, 10).expect("not an int"));
            position = position_between.rem_euclid(100); 
            //print!("{}  , {}  ", position, position_between);
            if position == 0 {
            result1+=1;
            result2+=1;
            }
            if i64::from_str_radix(clicks, 10).expect("not an int") >98 {
                    result2+=i64::from_str_radix(clicks, 10).expect("not an int").div_euclid(99) -1;
            }
            //println!("{}",i64::from_str_radix(clicks, 10).expect("not an int").div_euclid(99));
            if position_between > 100 || (position_between < 0 && prev_position != 0  ) {
                result2+=1;
            }
        }
        
    }
    println!("result of part 1 is {}  part 2 is {}", result1, result2);
}
