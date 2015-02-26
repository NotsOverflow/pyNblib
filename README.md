# pyNblib

### Yet an other bytestring lib

# You can turn:

1. '010203' into '☺☻♥'
2. '☺☻♥' into 66051
3. 'abcd☺☻♥!' into 'abcd   !'
4. 'abc\x00def\x00ghe" into ['abc\x00','def\x00','ghe\x00']
5. "0000000000000000FFFFFFFFFFFFFFFFAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCC" to :

  - "0000 0000 - 0000 0000"
  - "FFFF FFFF - FFFF FFFF"
  - "AAAA AAAA - AAAA AAAA"
  - "BBBB BBBB - BBBB BBBB"
  - "CCCC CCCC - CCCC CCCC"
