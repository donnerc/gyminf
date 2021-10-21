class StringPermutation:

    def __init__(self, perm, name=None):
        self.perm = perm
        self.name = name
        self.mapping = dict()

    def permutate(self, string):
        return ''.join([string[i-1] for i in self.perm])

    def __call__(self, x):
        result = self.permutate(x)
        if debug:
            print(f"{self.name}: {x} => {result}")
        return result


def chain_funcs(seq_of_funcs):
    def combination(x):
        for f in reversed(seq_of_funcs):
            x = f(x)
        return x
    return combination


def Si(matrix):
    mapping = ["00", "01", "10", "11"]

    def f(x):
        if len(x) % 4 > 0:
            raise ValueError(
                "word length must be multiple of 4, '{}' given".format(x))
        bit_pairs = [x[i:i+2] for i in range(0, len(x), 2)]
        indices = [int(bit_pair, 2) for bit_pair in bit_pairs]
        result = ''.join([
            mapping[matrix[j][i]] for (i, j) in [
                (indices[k], indices[k+1]) for k in range(0, len(indices), 2)
            ]
        ])
        print(f"Si: {x} => {result}")
        return result
    return f


def string_xor(word1, word2):

    result = ''.join([str(int(x) ^ int(y)) for x, y in zip(word1, word2)])
    if debug:
        print(f"XOR({word1}, {word2}) => {result}")
    return result


def split_in_two(word):
    if len(word) % 2 > 0:
        raise ValueError(
            "Word length must be multiple of 2, '{}' given".format(word))
    middle = len(word) // 2
    return word[:middle], word[middle:]


def S0_S1(word):
    r_left, r_right = split_in_two(word)
    return S0(r_left) + S1(r_right)


def EP_S0_S1_P4(word, key):
    left, right = split_in_two(word)
    left = string_xor(left, P4(S0_S1(string_xor(EP(right), key))))
    return left + right


def sdes(m, key):
    if not len(m) == 8 == m.count("1") + m.count("0"):
        raise ValueError(f"m must be a 8-bit binary string, given '{m}'")
    if not len(key) == 10 == key.count("1") + key.count("0"):
        raise ValueError(f"key must be a 10-bit binary string, given '{key}'")

    k1 = compute_K1(key)
    k2 = compute_K2(key)

    return IP_inverse(EP_S0_S1_P4(SW(EP_S0_S1_P4(IP(m), k1)), k2))


S0 = Si([
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
])
S1 = Si([
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
])


IP = StringPermutation(perm=(2, 6, 3, 1, 4, 8, 5, 7), name="IP")
IP_inverse = StringPermutation(
    perm=(4, 1, 3, 5, 7, 2, 8, 6), name="IP_inverse")
P10 = StringPermutation(perm=(3, 5, 2, 7, 4, 10, 1, 9, 8, 6), name="P10")
P8 = StringPermutation(perm=(6, 3, 7, 4, 8, 5, 10, 9), name="P8")
P4 = StringPermutation(perm=(2, 4, 3, 1), name="P4")
R1 = StringPermutation(perm=(2, 3, 4, 5, 1, 7, 8, 9, 10, 6), name="R1")
R2 = StringPermutation(perm=(3, 4, 5, 1, 2, 8, 9, 10, 6, 7), name="R2")
SW = StringPermutation(perm=(5, 6, 7, 8, 1, 2, 3, 4), name="SW")
EP = StringPermutation(perm=(4, 1, 2, 3, 2, 3, 4, 1), name="EP")

compute_K1 = chain_funcs([P8, R1, P10])
compute_K2 = chain_funcs([P8, R2, R1, P10])

key = "0110011011"
m = "00101010"
debug = True

print(sdes(m, key))
