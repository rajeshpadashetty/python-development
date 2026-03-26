def concat(*args,separator="/"):
    return separator.join(args)

print(concat("earth","mars","venus"))
print(concat("ram,raj,gang,durdhargirl",separator=","))
print(list(range(3,8)))
args=(4,10)
print(list(range(*args)))