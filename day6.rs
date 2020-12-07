//day6.rs
use std::fs;
use std::collections::HashSet;

fn day6_1() -> usize {
    fs::read_to_string("input6.txt").unwrap()
        .split("\n\n")
        .map(|group| {
            group
            .replace("\n", "")
            .chars()
            .collect::<HashSet<_>>()
            .len()
        })
        .sum()
}

fn day6_2() -> usize {
    fs::read_to_string("input6.txt").unwrap()
        .split("\n\n")
        .map(|group| {
            group
            .split("\n")
            .map(|individual| {
                individual
                .chars()
                .collect::<HashSet<_>>()
            })
            .fold(
                ('a'..='z').collect::<HashSet<char>>(), 
                |acc, x| acc.intersection(&x).cloned().collect::<HashSet<char>>()
            )
            .len()
        }).sum()
}

fn main() {
    println!("{}", day6_1());
    println!("{}", day6_2());
}
