import odd_even_f
import odd_even_w
import odd_even_r
import odd_even_enum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
even_number_list = []
odd_number_list = []

odd_even_w.w_numbers(
    numbers, counter, even_number_list, odd_number_list)

odd_even_f.f_numbers(
    numbers, counter, even_number_list, odd_number_list)

odd_even_r.r_numbers(
    numbers, counter, even_number_list, odd_number_list)

odd_even_enum.e_numbers(
    numbers, counter, even_number_list, odd_number_list)
