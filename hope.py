# print('hello ABDULROQEEB')
# name = input('HOW MAY I HELP YOU GUY?\n')


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input

print(fizz_buzz(15))


def fizz_buzz(input):
    if input % 3 == 0:
        result = "fizz"
    else:
        result = "buzz"
    return result

print(fizz_buzz(5))


stundent_count = 1000
rating = 4.99
is_published = True
course_name = "python programming"



numbers = [3,3,34,5,6,2]
numbers.sort(reverse=True)
print(numbers)


numbers = [3,3,34,5,6,2]
# numbers.sort(reverse=True)
print(sorted(numbers))
print(numbers)


numbers = [3,3,34,5,6,2]
# numbers.sort(reverse=True)
print(sorted(numbers,reverse=True))
print(numbers)

items = [
    ("product",10),
    ("product",10),
    ("product",10),
    ("product",10),
]


# def sort_item(item):
#     return item[1]

items.sort(key=lambda item: item[1])
print(items)

students_count = 1000
rating = 4.99
is_published = True
course_name = "python programming"

items= [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

items= [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
]
prices = []
for item in items:
    prices.append(item[1])

print(prices)


items= [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
]
# prices = []
# for item in items:
#     prices.append(item[1])

x = map(lambda item: item[1], items)
print(x)

items= [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
]
# prices = []
# for item in items:
#     prices.append(item[1])

x = map(lambda item: item[1], items)
for item in x:
    print(item)


items= [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
    ("product3", 12),
]
# prices = []
# for item in items:
#     prices.append(item[1])
prices = list(map(lambda item: item[1], items))
print(prices)

# set in pyhton

numbers = [1,1,2,3,4,5,7,8]
uniques = set (numbers)
second = {1,3,4}
second.add(5)
second.remove(5)
len(second)
print(uniques)


numbers = [1,1,2,3,4,5]
first = set(numbers)
second = {1,5}
print(first | second)


numbers = [1,1,2,3,4,5]
first = set(numbers)
second = {1,5}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 2 in first:
    print("YES")



# stacks

browser_session = []
browser_session.append(1)
browser_session.append(2)
browser_session.append(3)
browser_session.append(4)
print(browser_session)

browser_session = []
browser_session.append(1)
browser_session.append(2)
browser_session.append(3)
browser_session.append(4)
print(browser_session)

browser_session = []
browser_session.append(1)
browser_session.append(2)
browser_session.append(3)
browser_session.append(4)
print(browser_session)
last = browser_session.pop()
print(last)
print(browser_session)
print("redirect", browser_session[-1])
if not browser_session:
    print("disable")

# browser_session = []
# browser_session.append()
# browser_session.pop()
# if not browser_session:
#     browser_session[-1]

# strings
course = "my feelings for you"
print(course)
message = """
if life is all about the money you spent and not about the life you live than you need a tharapist maybe you 
feel life is a game
"""
print(message)

course = "python programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

course = "python \"programming"
print(course)


course = "python \'programming"
print(course)


course = "python\\programming"
print(course)


course = "python \nprogramming"
print(course)

first = "ABDULROQEEB"
last = " AKINDELE"
full = first + "" + last
print(full)


first = "ABDULROQEEB"
last = "AKINDELE"
full =f"{len(first)} {last}"
print(full)

first = "ABDULROQEEB"
last = "AKINDELE"
full =f"{len(first)} {2 + 2}"
print(full)

course = "  man of research"
print(course.upper())
print(course)


course = "  man of research"
print(course.lower())

course = "  man of research"
print(course.title())

course = "  man of research"
print(course.strip())


course = "  man in research"
print(course.lstrip())

course = "  man of research"
print(course.rstrip())


course = "  man of research"
print(course.find("res"))


course = "  man of research"
print(course.find("Res"))

course = "  man of research"
print(course.replace("r", "b"))

course = "  man of research"
print("pro" in course)

course = "  man of research"
print("man" in course)

course = "  man of research"
print("people" not in course)

course = "conclusion is more then decision"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course.find("more"))
print(course.replace("is", "can be"))
print("more" in course)
print("love" in course)
print("mankind" not in course)
