import hashlib


def same_bytes(left_filename, right_filename):
    return open(left_filename, "rb").read() == open(right_filename, "rb").read()


def find_duplicates_old(filenames):
    matches = []

    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_bytes(left, right):
                matches.append((left, right))

    return matches


def find_duplicates_new(filenames):
    past_hashes = set()
    duplicates = []
    hasher = hashlib.sha256()

    for file in filenames:
        hasher.update(open(file, "rb").read())
        current_hash = hasher.hexdigest()
        duplicates.append(file) if current_hash in past_hashes else past_hashes.add(current_hash)
        hasher = hashlib.sha256()

    return duplicates


if __name__ == "__main__":
    filepaths = ["tests/a1.txt", "tests/a2.txt",
                 "tests/a3.txt", "tests/b1.txt",
                 "tests/b2.txt", "tests/c1.txt"]

    for d in find_duplicates_new(filepaths):
        print(d)
