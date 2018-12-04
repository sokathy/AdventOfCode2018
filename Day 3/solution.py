def find_distance(s1, s2):
    """Computes diff from s1 & s2"""
    count = 0
    for i, c in enumerate(s1):
        if s1[i] != s2[i]:
            count += 1
    return count

def main():
    print(find_distance("Drew", "Brew"))

if __name__ == "__main__":
    main()
