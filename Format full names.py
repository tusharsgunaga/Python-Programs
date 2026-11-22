first_names = ["ada", "grace", "alan"]
last_names = ["lovelace", "hopper", "turning"]
full_names = list(map(lambda f, l: (f + " " + l).title(), first_names, last_names))
print(full_names)