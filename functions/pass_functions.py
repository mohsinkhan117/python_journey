'''
The pass statement in Python is a placeholder that does nothing when executed.

It is used to keep code blocks valid where a statement is required but no logic is needed yet.
Examples situations where pass is used are empty functions, classes, loops or conditional blocks.
In Functions
The pass keyword in a function is used when we define a function but don't want to implement its 
logic immediately. It allows the function to be syntactically valid, even though it doesn't perform any actions yet.
'''

# As python is an interpreted language, so we need to must execute any statement at
# each line, pass is the statement which we can use for no execution
def fun():
    pass

fun() # Call the function