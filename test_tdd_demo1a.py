"""
    MARKETING REQUEST FOR DEVELOPMENT:
        We want a function called "backwards",
        that returns its input reversed.
        e.g. "ABC" becomes "CBA"
"""

"""
    ENGINEERING FUNCTIONAL REQUIREMENTS:
        1. The identifier "backwards" must point to a function.
        2. The function must accept a string as input.
        3. The output value from the function must be the input reversed.
"""

"""
    THE TDD PROCESS (Repeat for each functional requirement):
        - Red       =   Make a failing test; see it FAIL.
        - Green     =   Do the minimum required to make it pass; see it PASS.
        - Refactor  =   Make it work well; see it still passes.
"""


# def backwards(): pass


# def backwards(text): return True


# def backwards(text): return text[::-1]
def backwards(text):
  letters = list(text)
  letters.reverse()
  return "".join(letters)


suite: dict = {
    "1. Is Function": lambda: callable(backwards),
    "2. Accepts String": lambda: backwards("ABC"),
    "3. Is Reversed": lambda: "ZYX" == backwards("XYZ"),
    }

# SIMPLE TEST FRAMEWORK
red, green = (u"\u001b[31mFAIL-RED:    ", u"\u001b[32mPASS-GREEN:  ")
for name, test in suite.items():
  try:
    print(f"{green if test() else red} : {name}")
  except Exception as message:
    print(f"{red}{name} MESSAGE: {message}")
''
