def parse_range(range_str):
    first_range, second_range = range_str.split('-')
    first_start, first_end = map(int, first_range.split(','))
    second_start, second_end = map(int, second_range.split(','))
    return (range(first_start, first_end + 1), range(second_start, second_end + 1))

def find_intersection(range1, range2):
    intersection = range(max(range1[0], range2[0]), min(range1[-1], range2[-1]) + 1)
    return intersection

if __name__ == "__main__":
    N = int(input("Enter the number of ranges: "))
    longest_intersection = None
    longest_intersection_length = float('-inf')

    for _ in range(N):
        range_str = input().strip()
        range1, range2 = parse_range(range_str)
        intersection = find_intersection(range1, range2)
        intersection_length = len(intersection)
        if intersection_length > longest_intersection_length:
            longest_intersection = intersection
            longest_intersection_length = intersection_length

    print(f"Longest intersection is {list(longest_intersection)} with length {longest_intersection_length}")
