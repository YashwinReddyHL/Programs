import statistics as st
import fractions as fr

nums = [1, 2, 3, 5, 7, 9]

print(st.mean(nums))

print(st.mean([-2, -4, 7]))

print(st.mean((
    fr.Fraction(3, 4),
    fr.Fraction(5, 7),
    fr.Fraction(2, 1)
)))

print(st.mean({1:"one",2:"two",3:"three"}))