Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 2 + 3j
>>> type(a)
<class 'complex'>
>>> a = complex(2, 3)
>>> a
(2+3j)
>>> b = 3 + 3j
>>> a + b
(5+6j)
>>> a - b
(-1+0j)
>>> a * b
(-3+15j)
>>> a / b
(0.8333333333333334+0.16666666666666666j)
>>> z = 2 + 3j
>>> z.real
2.0
>>> z.imag
3.0
>>> 