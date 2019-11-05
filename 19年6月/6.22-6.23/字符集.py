import re
target = 'abc acc aec agc adc a_c a66c a c a9c a4c'
print(re.findall('a[\d]c',target))
print(re.findall('a[(\d\d)\d]c',target))
print(re.findall('a[\w]c',target))
print(re.findall('a[\s]c',target))
print(re.findall('a[^b-e]c',target))
print(re.findall('a[b-e]c',target))

