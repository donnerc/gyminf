# Simple DES

The Python 3 script `sdes.py` implements the simple DES algorithm presented in the first course.

## Usage

```bash
$ python sdes.py <8bit-message> <10bit-key>
```

The example from slide 4 would therefore give the following execution:

```bash
$ python sdes.py <8bit-message> <10bit-key>
Message: 00101010
Key: 0110011011
Cyphered text: 01000110
```

By the way, the result obtained is different from the answer of the whole
development on the slides, which is wrong. On the slides, there is a mistake on
slide 17, because `S1(1100) = 11` and not `01`.

## Debug mode

The whole trace can be printed by activating the debug mode. To activate
debugging (traces all operators), set the `DEBUG` env var to `1` :

```bash
$  DEBUG=1 python sdes.py 00101010 0110011011
Message: 00101010
Key: 0110011011
==============================
P10: 0110011011 => 1011010101
R1: 1011010101 => 0110101011
P8: 0110101011 => 01100111
P10: 0110011011 => 1011010101
R1: 1011010101 => 0110101011
R2: 0110101011 => 1010101101
P8: 1010101101 => 01101110
==============================
K1 = 01100111 and K2 = 01101110
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
S1: 1100 => 11
P4: 1111 => 1111
XOR(0011, 1111) => 1100
IP_inverse: 11000001 => 01000110
Cyphered text: 01000110
```
