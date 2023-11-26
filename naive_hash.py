def naive_hash(data):
    return sum(data) % 13


def same_bytes(left_filename, right_filename):
    return open(left_filename, "rb").read() == open(right_filename, "rb").read()


def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = naive_hash(data)
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


if __name__ == "__main__":
    filepaths = ["tests/a1.txt", "tests/a2.txt",
                 "tests/a3.txt", "tests/b1.txt",
                 "tests/b2.txt", "tests/c1.txt"]
    group = find_groups(filepaths)
    for filepaths in group.values():
        duplicates = find_duplicates(list(filepaths))
        for (left, right) in duplicates:
            print(left, right)
