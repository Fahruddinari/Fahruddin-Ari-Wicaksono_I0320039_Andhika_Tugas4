x = 4   #4 = 0000 0100
y = 11  #11 = 0000 1011

#output dari 4 | 11
a = x | y;
print("Nilai: ", a,"binary: ",format(a,'08b'))

#output dari 4 >> 11
a = x >> y;
print("Nilai: ", a,"binary: ",format(a,'08b'))

#output dari 4 ^ 11
a = x ^ y;
print("Nilai: ", a,"binary: ",format(a,'08b'))

#output dari ~4
a = ~x;
print("Nilai: ", a,"binary: ",format(a,'08b'))

#output dari 11 & 4
a = y & x
print("Nilai: ", a,"binary: ",format(a,'08b'))