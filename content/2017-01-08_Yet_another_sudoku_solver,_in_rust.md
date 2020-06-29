+++
title = "Yet another sudoku solver, in rust"
slug="Yet-another-sudoku-solver,-this-time-in-rust"
draft = false
date = 2017-01-08
[taxonomies]
categories = [ "Divers" ]
tags = [ "english","rust" ]
+++
I have been quite interested recently with the new languages [Go](https://golang.org/) and [rust](https://www.rust-lang.org/).
Go and rust have some very nice new features and their design and tooling reflects the standards of this days.
So I have been hacking with go and rust.

I share this piece of rust code that solves sudoku, in the hope it will be useful to someone.
It is not very much optimized as the algorithm is naive, but the purpose of this code was to get more comfortable with rust.

```

fn print_grid(g: [Option<i32>; 81]) {

    let mut cnt = 0;
    let mut line = 0;

    for &x in g.iter() {

        cnt = cnt + 1;

        match x {
            Some(i) => print!("{}", i),
            None => print!("_"),
        }

        if cnt == 9 {
            line = line + 1;
            println!("");
            cnt = 0;
            if line == 3 {
                line = 0;
                println!("");
            }
        } else if cnt % 3 == 0 {
            print!("   ");

        } else {
            print!(" ");
        }
    }
}

fn check_grid(g: [Option<i32>; 81]) -> bool {

    // check lines
    for x in 0..9 {
        let i = 9 * x;
        let val = [i, i + 1, i + 2, i + 3, i + 4, i + 5, i + 6, i + 7, i + 8];

        for v in 0..(val.len() - 1) {
            let valv = g[val[v]];
            if valv != None {
                for c in 1..val.len() {
                    let valc = g[val[c]];
                    if valc != None && val[v] != val[c] && valv == valc {
                        // println!("Block false at {}", x);
                        return false;
                    }
                }
            }
        }
    }

    // check columns
    for x in 0..9 {
        let val = [x, x + 9, x + 18, x + 27, x + 36, x + 45, x + 54, x + 63, x + 72];

        for v in 0..(val.len() - 1) {
            let valv = g[val[v]];
            if valv != None {
                for c in 1..val.len() {
                    let valc = g[val[c]];
                    if valc != None && val[v] != val[c] && valv == valc {
                        // println!("Block false at {}", x);
                        return false;
                    }
                }
            }
        }
    }

    // check blocks
    for x in 0..9 {
        let mut i = 3 * (x % 3);
        if x > 2 {
            i = i + 27;
        } else if x > 5 {
            i = i + 54;
        }

        let val = [i, i + 1, i + 2, i + 9, i + 10, i + 11, i + 18, i + 19, i + 20];

        for v in 0..(val.len() - 1) {
            let valv = g[val[v]];
            if valv != None {
                for c in 1..val.len() {
                    let valc = g[val[c]];
                    if valc != None && val[v] != val[c] && valv == valc {
                        // println!("Block false at {}", x);
                        return false;
                    }
                }
            }
        }
    }

    return true;
}

fn is_grid_complete(g: [Option<i32>; 81]) -> bool {
    let mut ret = true;
    for &x in g.iter() {
        match x {
            Some(_) => {}
            None => {
                ret = false;
                break;
            }
        }
    }
    return ret;
}

fn clone_grid(g: [Option<i32>; 81]) -> [Option<i32>; 81] {
    let mut new_g: [Option<i32>; 81] = [None; 81];
    for x in 0..g.len() {
        new_g[x] = g[x];
    }
    return new_g;
}


fn solve_grid(g: [Option<i32>; 81]) -> Option<[Option<i32>; 81]> {

    if is_grid_complete(g) {
        return Some(g);
    }

    for x in 0..g.len() {
        match g[x] {
            Some(_) => {}
            None => {

                let mut checked: [bool; 9] = [false; 9];

                for v in 1..10 {

                    let mut new_g = clone_grid(g);
                    new_g[x] = Some(v);

                    checked[(v - 1) as usize] = true;

                    if check_grid(new_g) {
                        match solve_grid(new_g) {
                            None => {
                                if checked == [true; 9] {
                                    // the path is a dead end
                                    return None;
                                } else {
                                    continue;
                                }
                            }

                            Some(gx) => return Some(gx),
                        }
                    }
                }

                if checked == [true; 9] {
                    // Detected a dead end
                    return None;
                }
            }
        }
    }

    return None;
}

fn parse_grid(grid_string: &str) -> [Option<i32>; 81] {
    let mut grid = [None; 81];

    let mut i = 0;
    for s in grid_string.split_whitespace() {
        match s {
            "_" => {}
            val => {
                grid[i] = Some(val.parse::<i32>().unwrap());
            }
        }
        i = i + 1;
    }

    return grid;
}

fn main() {
    let grid_string = r#"
            1 _ _   _ _ _   _ _ 3
            _ 4 _   _ _ 9   2 6 _
            _ _ _   7 _ _   _ 5 4

            _ _ _   1 7 _   9 _ _
            _ _ 2   _ _ _   6 _ _
            _ _ 3   _ 9 5   _ _ _

            2 7 _   _ _ 1   _ _ _
            _ 8 9   3 _ _   _ 7 _
            6 _ _   _ _ _   _ _ 2"#;

    let grid: [Option<i32>; 81] = parse_grid(grid_string);

    print_grid(grid);

    match solve_grid(grid) {
        Some(g) => {
            println!("Grid complete !");
            print_grid(g)
        }
        None => println!("Couldn't solve the sudoku"),
    }

}

```

You can just, given you have installed [rust](https://www.rustup.rs/).
```
cargo build
```