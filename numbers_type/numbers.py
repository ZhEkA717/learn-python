# Int, Float, Complex

#Int
cat = 4
dogs = 2
shots = 19
data_population = -200
k = int(16)

#Float
volume = 1.5
area = 42.8
salary = 2523.3
p = float(2)

#Complex
a = 4 + 6j
b = 8 - 2.3j
c = complex(4, -2)


int_to_float = float(dogs)
float_to_int = int(volume)
float_to_complex = complex(area)

print(int_to_float, float_to_int, float_to_complex)

# complex_to_float = float(b)

# print(complex_to_float) #TypeError: float() argument must be a string or a real number, not 'complex'

s1 = a + b
s2 = volume - area
s3 = p * dogs # -> float
s4 = salary / cat
S5 = volume ** 2

s6 = shots // dogs # -> 9
s7 = shots % dogs # 1

attention = 42.2 - 20 
print(attention) # -> 22.200000000000003