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

To activate debugging (traces all operators), set the `DEBUG` env var to `1` :

```bash
$ DEBUG=1 python sdes.py <8bit-message> <10bit-key>
```
