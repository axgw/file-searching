import hashlib


# Write a function that calculate the SHA-256 hash code of each unique line of a text file.
#
# Convert the hex digests of those hash codes to integers.

def unique_line_hashing(filename):
    with open(filename, "rb") as file:
        seen_hashes = set()
        unique_hashes = []
        for line in file:
            line = line.rstrip(b'\r\n')
            hasher = hashlib.sha256()
            hasher.update(line)
            current_hash = hasher.hexdigest()
            (seen_hashes.add(current_hash) if current_hash not in seen_hashes else
             unique_hashes.append(int(current_hash, 16)))
    return unique_hashes


unique_values = unique_line_hashing('tests/the_eyes_have_it.txt')
# print(unique_values[:10])