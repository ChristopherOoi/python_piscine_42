ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
# your code here

ft_list[1] = "World!"

hello, country = ft_tuple
country = "Singapore!"

ft_tuple = hello, country

ft_set.remove("tutu!")
ft_set.add("Singapore!")

ft_dict["Hello"] = "42Singapore!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
