//day9.rs
use std::fs;

fn sumin(prefix: &[i64], v: i64) -> Option<&i64> {
    prefix
        .iter()
        .filter(|x| prefix.contains(&(v - *x)) && (*x+*x) != v)
        .next()
}

fn part1(xmas: &Vec<i64>, preamble: usize) -> i64 {
    for i in preamble..(xmas.len()) {
        if sumin(&xmas[i-preamble..i], xmas[i]).is_none() {
            return xmas[i];
        }
    }
    0
}

fn findsum(slice: &[i64], v: i64) -> Option<&[i64]> {
    let mut s = 0;
    for i in 0..slice.len() {
        s += slice[i];
        if s == v {
            return Some(&slice[0..i+1]);
        }
        else if s > v {
            return None
        }
    }
    None
}

fn part2(xmas: &Vec<i64>, v: i64) -> i64 {
    for i in 0..xmas.len() {
        if let Some(f) = findsum(&xmas[i..], v) {
            return f.iter().min().unwrap() + f.iter().max().unwrap()
        }
    }
    0
}

fn main() {
    let xmas: Vec<i64> = 
        fs::read_to_string("input9.txt").unwrap()
        .split("\n")
        .filter_map(|v| v.parse::<i64>().ok())
        .collect();
    let p1 = part1(&xmas, 25);
    let p2 = part2(&xmas, p1);

    println!("{}", p1);
    println!("{}", p2);
}
