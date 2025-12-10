string = "hello"
freq = {}         

for char in string:
    if char in freq:     # if character already exists in dictionary
        freq[char] += 1  # increase its count
    else:
        freq[char] = 1   

print(freq)
