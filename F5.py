# write a function that greets the user.if no name is provided , it shoild greets with default name


def name(n="user"):
    return "hello "+ n + " !"


print(name("vivek"))
print(name())