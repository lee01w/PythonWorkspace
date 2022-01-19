cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))
print(3 in cabinet)

cabinet = {"A-3":"유재석", "A-100":"김태호"}
print(cabinet["A-3"])

# Add
cabinet["C-20"] = "조세호"

# Delete
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)