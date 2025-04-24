def get_discrete_log_mapping_for(base, mod):
    """This creates a dictionary that maps `base**i` to `i`"""
    d = {}
    # Subtract 1 from the modulus since both 0 and 28 (see Fermat's Little Thm) will result in '1',
    # but only 0 is in our 0-indexed alphabet
    for i in range(mod - 1):
        d[(base**i % 29)] = i
    return d


# `7**i * 4**i` is equivalent to `28**i`
# Because `28**i` has an order of `2`, these are the only 2 values it can assume
options = [1, 28]
discrete_log_mapping_of_3 = get_discrete_log_mapping_for(3, 29)


def decrypt(c):
    val = ord(c) - 97
    # 3**m + option = val
    candidate_characters = []
    for option in options:
        result = (val - option) % 29

        if result in discrete_log_mapping_of_3:
            candidate = discrete_log_mapping_of_3[result]
            candidate_characters.append(chr(candidate + 97))

    print(candidate_characters)


# Taken from the first line of `dlp-0-output.txt`
ciphertext = "ihl|{q{cyp|bwicdym{qvgtnuypeydhwoykti|u"
for c in ciphertext:
    # Eyeball the output to guess the message
    decrypt(c)
