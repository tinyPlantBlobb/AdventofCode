pub fn run(input:String){
    let rotation = input.split("\n").collect::<Vec<&str>>();
    let mut position = 50;
    println!("{}", rotation[0]);
    let mut result1 = 0;
    let mut result2 =0;
    for l in rotation {
        if l.len()>1{
            let (direction_char,clicks) = l.split_at(1);
            let direction = match direction_char {
                "L" => Ok(-1),
                "R"=> Ok(1),
                _ => Err(()),
            }.expect("no direction given");
            let turn = i64::from_str_radix(clicks, 10).expect("not an int");
            let prev_position = position;
            let mut position_between : i64= (position + direction * turn);
            let overflow_turns = i64::abs(turn.div_euclid(100));
            position = position_between.rem_euclid(100); 
            //print!("{}  , {}  ", position, position_between);
            if position == 0 {
            result1+=1;
            if overflow_turns >0 {
                    result2+=i64::abs(overflow_turns);
                    //println!("pos 0 and overflow");
                    result2+=1;
            } else {
                result2+=1;
                 //println!("pos 0 and no overflow");
            }
            } else {
            if overflow_turns >0 {
                //println!("pos diff and overflow");
                    result2+=i64::abs(overflow_turns);
                    position_between -= direction *overflow_turns * 100;
                    if  ((position_between > 100 )|| (position_between < 0 && prev_position != 0)){
                    result2 += 1; 
                    }
            }else {
                //println!("pos diff and no overflow");
            if  ((position_between > 100 )|| (position_between < 0 && prev_position != 0)) {
                result2+=1;
            }
        }
            }
        println!("start {} turn {}  pre mod {} post mod {} div {} result {}", prev_position,turn, position_between, position,overflow_turns, result2);
        }

    }
    println!("result of part 1 is {}  part 2 is {}", result1, result2);
}
