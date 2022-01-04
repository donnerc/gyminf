# Simple DES

The Python 3 script `sdes.py` implements the simple DES algorithm presented in the first course.

## Usage to encrypt

```bash
$ python sdes.py -e <8bit-message> <10bit-key>
```

## Usage to decrypt

```bash
$ python sdes.py -d <8bit-cipher> <10bit-key>
```

The example from slide 4 would therefore give the following execution:

```bash
$  python sdes.py -e 00101010 0110011011
Plaintext: 00101010
key: 0110011011
Ciphertext: 01100110
```

To decrypt a ciphertext, use the `-d` option instead of `-e``

```bash
$  python sdes.py -d 01100110 0110011011
Ciphered: 01100110
key: 0110011011
Plaintext: 00101010
```

## Debug mode

The whole trace can be printed by activating the debug mode. To activate
debugging (traces all operators), use the `-D` option:

```bash
$  python sdes.py -D -e 00101010 0110011011
Plaintext: 00101010
key: 0110011011
########################################
Compute partial keys
P10: 0110011011 => 1011010101
R1: 1011010101 => 0110101011
P8: 0110101011 => 01100111
P10: 0110011011 => 1011010101
R1: 1011010101 => 0110101011
R2: 0110101011 => 1010101101
P8: 1010101101 => 01101110
K1 = 01100111 and K2 = 01101110
########################################
IP: 00101010 => 00100011
EP: 0011 => 10010110
XOR(10010110, 01100111) => 11110001
S0: 1111 => 10
S1: 0001 => 10
P4: 1010 => 0011
XOR(0010, 0011) => 0001
SW: 00010011 => 00110001
EP: 0001 => 10000010
XOR(10000010, 01101110) => 11101100
S0: 1110 => 11
S1: 1100 => 01
P4: 1101 => 1101
XOR(0011, 1101) => 1110
IP_inverse: 11100001 => 01100110
Ciphertext: 01100110
```
