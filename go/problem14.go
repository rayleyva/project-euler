package main

import (
    "fmt"
)

func next(n int64) int64 {
    if n % 2 == 0 {
        n = n / 2
    } else {
        n = (3*n) + 1
    }
    return n
}

func main() {
    var largest, largest_i, i, ct, curr int64
    seq_memo := make(map[int64] int64, 1000000)
    for i = 1; i < 1e6; i++ {
        curr = i
        ct = 0
        for ; curr != 1; {
            if val, ok := seq_memo[curr]; ok {
                ct += val
                break
            } else {
                ct++
                curr = next(curr)
            }
        }
        seq_memo[i] = ct
        if ct > largest {
            largest = ct
            largest_i = i
        }
    }
    fmt.Printf("%v\n", largest_i)
}
