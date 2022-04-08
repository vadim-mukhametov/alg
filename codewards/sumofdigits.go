package main

import (
	"strconv"
)

func DigitalRoot(n int) int {
	var sum int
	s := strconv.Itoa(n)

	if len(s) == 1 {
		return n
	}

	for _, item := range s {
		num, _ := strconv.Atoi(string(item))
		sum += num
	}

	return DigitalRoot(sum)
}

func main() {
	println(DigitalRoot(493193))
}
