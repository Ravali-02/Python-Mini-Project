# band ={
#     "vocals": "plant",
#     "guitar": "geat"

# }
# band2 = dict(vocals = "plants" , guitar= "geat")
# print(band)
# print(band2)

# print(len(band))
# print(band.items())
# print(band.values())
# print(band.keys())
# print(band.items())
# band["vocals"] = "coverdale"
# band.update({"bass" : "GPJ"})
# print(band)
#     #   remove items

# print(band.pop("bass"))
# print(band)
# band["drum"] = "bohnam"
# print(band)

# print(band.popitem())
# print(band)

# # band["drum"] = "bohnam"
# # del band["drum"]
# # print(band)

# # band2.clear()
# # print(band2)

# # del band2
# # print(band2)

# # copydict
# band2 = band #create a reference
# # print("Bad Copy!")
# # print(band2)
# # print(band)

# # band2["drum"] = 'Ravali'
# # print(band)

# # band2 = band.copy()
# # band2["drums"] = 'Ravali'
# # print(band)
# # print(band2)


# band3 = dict(band)
# print("good copy!")
# print(band3)

# # nested dictonaries

# member1 = {
#     "name": "plant",
#     "instrument": "Vocals"
# }

# member2 = {
#     "name": "thing",
#     "instrument": "guitar"
# }

# band = {
#     "member1" : member1,
#     "member2" : member2
# }

# print(band)
# print(band["member2"]["instrument"])

# # sets

# nums = {1, 2, 3, 4}

# nums2 = set((1,2,3,4))

# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums2))

# # # no duplicate allowedd
# nums = {1, 2, 2, 3}
# print(nums)

# # true is a dup 1, false is a dupe

# nums = {1, True, 2, False, 3, 4, 0}
# print(nums)

# # check if the value is in a set
# print(2 in nums)

# # but you cannot refer to a element in the set with an index postion or a key

# # add a new value to set
# nums.add(6)
# print(nums)

# morenums = {5, 7, 9, 10}
# nums.update(morenums)
# print(nums)

# # you can use update to both list and dict, tuples
# # merge two set to create a new set

# one = {1, 2, 3}
# two = {4, 5, 6}
# three = {7, 8, 9}

# # mynewset = one.union(two).union(three)
# # print(mynewset)

# # keep only the duplicates
# one = {1, 2, 3}
# two = {1, 5, 3}
# three = {7, 8, 9}

# one.intersection_update(two)
# print(one)
# # keeping everything except duplicate

# one = {1, 2, 3}
# two = {2, 5, 1}

# one.symmetric_difference_update(two)

# # print(one)
# my_list = [1, 2, 3, 2, 4, 5, 2]
# duplicates = my_list.count(2)
# print(duplicates)
Dict = {"A": 1, "B": "2", "C": [3, 3, 3], "D": (4, 4, 4), 'E': 5, 'F': 6}
print(Dict["D"])
