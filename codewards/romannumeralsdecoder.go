package main

func decode(roman string) int {
	var result int
	numbers := make([]int, len(roman))
	mapping := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	for idx, letter := range roman {
		numbers[idx] = mapping[string(letter)]
	}

	for idx, num := range numbers {
		for _, i := range numbers[idx:] {
			if num < i {
				numbers[idx] = -num
			}
		}

	}

	for _, item := range numbers {
		result += item
	}

	return result
}
