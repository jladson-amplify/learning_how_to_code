print ("1, 2, 3, 4")
print ("one", "two", "three", "Four" )
print ("True", "False", "False", "True")
print ("%r", "%r", "%r", "%r")
print ("I had this thing.",
       "That you could type up right.",
       "But it didn't sing.",
       "So I said goodnight."
       )

formatter = "%r selenium %r %r %r"
print formatter
print formatter % (1, 2, 3, 4)
print formatter % (1, 2.0, "3 three things", 4)
print formatter % (1, 2, 3, 4)
