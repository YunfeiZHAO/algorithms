""" hash table related questions"""


def peopleIndexes(favoriteCompanies: list[list[str]]) -> list[int]:
    # Turn lists into sets once
    sets = [set(companies) for companies in favoriteCompanies]
    n = len(sets)

    # Sort indices by size (small -> large): a set can only be a subset of an equal or larger set
    order = sorted(range(n), key=lambda i: len(sets[i]))

    is_subset = [False] * n
    for pos, i in enumerate(order):
        if is_subset[i]:
            continue
        si = sets[i]
        # Only need to compare against sets with size >= len(si), i.e. those after `pos`
        for j in order[pos + 1:]:
            if is_subset[j]:
                continue
            if si <= sets[j]:  # subset or equal
                is_subset[i] = True
                break

    return [i for i in range(n) if not is_subset[i]]


if __name__ == "__main__":
    favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
    print(peopleIndexes(favoriteCompanies))