//day1.rs
use std::fs;
use std::collections::HashSet;

fn day1_1() -> i64 {
    let expenses: HashSet<i64> = 
        fs::read_to_string("input1.txt").unwrap()
        .split("\n")
        .filter_map(|amount| amount.parse::<i64>().ok())
        .collect();

    // expenses
    //     .iter()
    //     .map(|amount| 2020-amount)
    //     .filter(|expense| expenses.contains(expense))
    //     .take(1)
    //     .map(|x| x * (2020-x))
    //     .next()
    //     .unwrap()

    expenses
        .iter()
        .filter_map(|amount| {
            if let Some(expense) = expenses.get(&(2020-amount)) {
                Some(amount * expense)
            } else {
                None
            }
        })
        .next()
        .unwrap()
}

fn day1_2() -> i64 {
    let expenses: HashSet<i64> = 
        fs::read_to_string("input1.txt").unwrap()
        .split("\n")
        .filter_map(|amount| amount.parse::<i64>().ok())
        .collect();

    let mut v: Vec<i64> = expenses.iter().cloned().collect();

    while let Some((amount, tail))  = v.split_first() {
        for second in tail {
            if let Some(expense) = expenses.get(&(2020-amount-second)) {
                return amount * second * expense;
            }
        }
        v = tail.to_vec();
    }
    0
}

fn main() {
    println!("{}", day1_1());
    println!("{}", day1_2());
}
