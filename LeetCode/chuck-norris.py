"""
Here is the encoding principle:

The input message consists of ASCII characters (7-bit)
The encoded output message consists of blocks of 0
A block is separated from another block by a space
Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
  - First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
  - Second block: the number of 0 in this block is the number of bits in the series
"""

def encode(message):
  asci_code = ''
  for s in message:
      c_str = ''
      ascii_code = ord(s)
      while ascii_code > 0:
          bit = ascii_code % 2
          ascii_code = ascii_code // 2
          c_str = str(bit) + c_str
      asci_code += c_str.zfill(7)

  print(message, asci_code)

  t_str = []
  old_v = ''
  for v in asci_code:
      if v == old_v:
          t_str[-1][1] += 1
      else:
          t_str.append(['0' if v == '1' else '00', 1])
          old_v = v

  return ' '.join([ v + ' ' + '0'*count for v, count in t_str ])

assert encode('C') == '0 0 00 0000 0 00'
assert encode('CC') == '0 0 00 0000 0 000 00 0000 0 00'
