#########################
# Ex 1 #
#########################

prices: list[int] = [120, 45, 300, 89, 210, 15, 74]

prices_doubled: list[int] = [num * 2 for num in prices]
print(prices_doubled)

expensive: list[int] = [num for num in prices if num > 100]
print("Expensive:", expensive)

on_sale: list[int] = [num - 50 for num in prices if num > 100]
print("On sale:", on_sale)

labels: list[str] = ["pricey" if num > 100 else "cheap" for num in prices]
print("Labels:", labels)

as_text: list[str] = [f"{num} NIS" for num in prices]
print("As text:", as_text)


#########################
# Ex 2 #
#########################

battery: list[int] = [78, 92, 45, 61, 88, 30]

above_20 = [num > 20 for num in battery]
print("All above 20:", all(above_20))

below_40 = [num < 40 for num in battery]
print("Any below 40:", any(below_40))

fully_charged = [num == 100 for num in battery]
print("All full:", all(fully_charged))

ordered = sorted(battery)
print("Ordered:", ordered)
print("Original:", battery)


battery.sort(reverse=True) # battery # in-place. function
print("Sorted desc:", battery)

print("Top three:", battery[0:3])


#########################
# Ex 3 #
#########################

words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]

print("ALL uppercase:", all(word.isupper() for word in words))
print("Has a long word:", any(len(word) > 5 for word in words))
print("By length:", sorted(words, key=len))













