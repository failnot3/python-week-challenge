# Methods are just functions.
# METHODS automatically have access to the object they are called on!

# EXAMPLE: thing.method()
name = "Petar"
name.capitalize()
# for HELP page - name.capitalize?
# another example
name.lower()

# .strip() return a copy of our string by default it removes spaces, new line etc.
" hello \t Mike".strip()
# If we provide a argument to it, it can remove a char we type.
"....Hello ....".strip(".")

# another method is replace(old, new, [count]) OLD and NEW is req. arguments!
races = " 3kilometers 5kilometers"
races.replace("kilometers", "km")
