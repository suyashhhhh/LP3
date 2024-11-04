# Practical-2 : Huffman encoding using greedy strategy

import heapq

def calculate_frequency(s):
	frequency = {}
	for char in s:
		if char not in frequency:
			frequency[char] = 0
		frequency[char] += 1
	return frequency

def huffman_encode(frequency):
	heap = [[weight, [char, ""]] for char, weight in frequency.items()]
	heapq.heapify(heap)

	while len(heap) > 1:
		lo = heapq.heappop(heap)
		hi = heapq.heappop(heap)
		for pair in lo[1:]:
			pair[1] = '0' + pair[1]
		for pair in hi[1:]:
			pair[1] = '1' + pair[1]
		heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

	return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

s =input("Enter the string or words to generate their huffman encoding:")
frequency = calculate_frequency(s)
huff = huffman_encode(frequency)
print(f"frequency of the chars of given string is: {frequency}")
print("Char | Huffman code ")
print(" ")
for char, huffman_code in huff:
	print(f" {char} | {huffman_code}")