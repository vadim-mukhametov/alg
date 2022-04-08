package main

import (
	"fmt"
	"strings"
)

func duplicate_count(s1 string) int {
	var result int
	mapping := make(map[string]int)

	for _, char := range s1 {
		mapping[string(strings.ToLower(string(char)))] += 1
	}

	for _, item := range mapping {
		if item > 1 {
			result += 1
		}
	}

	return result
}

func main() {
	fmt.Println(duplicate_count("indivisibility"))
}
