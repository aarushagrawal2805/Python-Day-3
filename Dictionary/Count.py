string = "hello"
freq = {}         # empty dictionary to store result

for char in string:
    if char in freq:     # if character already exists in dictionary
        freq[char] += 1  # increase its count
    else:
        freq[char] = 1   

print(freq)
