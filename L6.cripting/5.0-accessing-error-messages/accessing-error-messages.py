# Accessing Error Messages
'''When we handle an exception, we can still access its error message ike this:
try:
# some code
#except ZeroDivisionError as e:
# some code
print("ZeroDivisionError occurred: {}".format(e))'''

# output:
'''
ZeroDivisionError occurred: integer division or modulo by zero
If we don't have specific error to handle, we can still access error message by using except Exception:

try:
    # some code
except Exception as e:
# some code
print("Exception occurred: {}".format(e))
Exception is just the base class for all built-in exceptions. Learn more at Built-in Exceptions — Python 3.8.3 documentation'''
