# How To Fix Python Errors

**This repo contains a README with an explanation as to why the error is happening and how to fix it.**

## Contents

- [How To Fix Python Errors](#how-to-fix-python-errors)
  - [Contents](#contents)
      - [NameError](#nameerror)
      - [IndexError](#indexerror)
      - [IndentationError](#indentationerror)
      - [ModuleNotFoundError](#modulenotfounderror)
      - [KeyError](#keyerror)
      - [ZeroDivisionError](#zerodivisionerror)
      - [AttributeError](#attributeerror)
      - [UnboundLocalError](#unboundlocalerror)
      - [RecursionError](#recursionerror)
      - [ImportError](#importerror)
      - [TypeError](#typeerror)
      - [ValueError](#valueerror)
      - [StopIteration](#stopiteration)
      - [KeyboardInterrupt](#keyboardinterrupt)

#### NameError

- This error is usually occuring because you haven't defined the variable and are just using it.

- To fix it you should define it like `VariableName = AnythingHere`.

    > - **Note. You mustn't define VariableName as another non existant variable. This will get you back to step one.**

- Examples can be found in [`/Examples`](./Examples/NameErrorSolve.py)

- Official Documentation of [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError)

#### IndexError

- This error is usually raised when attempting to retrieve an index from a sequence and the index isn't found in the sequence.

- To fix make sure the index is a number inside the sequence

    > - **Note. in python counts from 0 therefore one will be 0, two will be 1, three will be 2 and so on.**

- Examples can be found in [`/Examples`](./Examples/IndexErrorSolve.py)

- Official Documentation of [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError)

#### IndentationError

- This error occurs when the code expects an indent or you indented a line too much than expected.

- To fix it, get everything under a `:` in the same indent

    > - **Note: lines below a `:` need to be indented. If there is no `:` in the line above then it should be in the same indentation level as the line above**

- Examples can be found in [`/Examples`](./Examples/IndentationErrorSolve.py)

- Note that using both tabs and spaces when indenting will raise TabError. stick to either spaces or tabs, not both

- Official Documentation of [`IndentationError`](https://docs.python.org/3/library/exceptions.html#IndentationError)

#### ModuleNotFoundError

- This specific error is raised when you try to import a module that is not installed / doesnt exist.

- To fix it, search in [pypi.org](https://pypi.org) and see if it actually exists, and install it

   > - **First, make sure you dont have any spelling mistakes in the import statement**

- Examples can be found in [`/Examples`](./Examples/ModuleNotFoundErrorSolve.py)

- Official Documentation of [`ModuleNotFoundError`](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError)

#### KeyError

- This type of error is usually raised when trying to access a non-existent key of a [dict](https://docs.python.org/3/library/stdtypes.html#dict)

- To fix this,

  - make sure you have no spelling error in the key name

  - Add the key when creating the dict

  - If the above is not possible, try adding the key manually

  - If adding the key is not a choice, avoid the error by using  [`dict.get`](https://docs.python.org/3/library/stdtypes.html#dict.get) which would return None if not found

- Examples can be found in [`/Examples`](./Examples/KeyErrorSolve.py)

- Official Documentation of [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError)

#### ZeroDivisionError

- The error is kind of self-explanatory. You tried to divide something by 0 which is impossible.

- This usually happens when you divide something with a user input and the user inputs

- To fix this, use an if statement to check if the number is 0 and dont divide if it is.

- Examples can be found in [`/Examples`](./Examples/ZeroDivisionErrorSolve.py)

- Official Documentation of [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError)

#### AttributeError

- AttributeError is raised when you try to access an attribute of an object that doesnt exist.

- Fixing this error needs a proper understanding of classes and attributes.

- To fix this, check for spelling errors and see if that attribute actually exists

- Examples can be found in [`/Examples`](./Examples/AttributeErrorSolve.py)

- Official Documentation of [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError)

#### UnboundLocalError

- This is raised when you reference a variable inside a function or method but no value is bound to that variable

- To fix it, see if you are using it before assigning something to it

- Examples can be found in [`/Examples`](./Examples/UnboundLocalErrorSolve.py)

- Official Documentation of [`UnboundLocalError`](https://docs.python.org/3/library/exceptions.html#UnboundLocalError)

#### RecursionError

- Recursion error is raised when the maximum recursion depth AKA [`sys.getrecursionlimit`](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit) exceeds

- To fix it, add a base case to return early and not do any more recursion

- Examples can be found in [`/Examples`](./Examples/RecursionErrorSolve.py)

- Official Documentation of [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError)

#### ImportError

- Is raised when the “from list” in `from ... import` has a name that cannot be found.

- To fix it, check for spelling errors. Also check if the module exists by checking the relevent documentation

- Examples can be found in [`/Examples`](./Examples/ImportErrorSolve.py)

- Official Documentation of [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError)

#### TypeError

- Raised when an operation or function is applied to an object of inappropriate type.

- To fix it, read the relevant documentation and find which type of object you should be passing in.

- Examples can be found in [`/Examples`](./Examples/TypeErrorSolve.py)

- Official Documentation of [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError)

#### ValueError

- Raised when an operation or function receives an argument that has the right type but an inappropriate value

- To fix it, read the relevant documentation and see which kind of value is accepted.

- Examples can be found in [`/Examples`](./Examples/ValueErrorSolve.py)

- Official Documentation of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)

#### StopIteration

- This exception is raised to signal that there are no further items produced by the iterator or the generator is [`closed`](https://docs.python.org/3/reference/expressions.html#generator.close)

- This is not fixable. You would have to create a new generator object in order to bypass this

- Examples can be found in [`/Examples`](./Examples/StopIterationSolve.py)

- Official Documentation of [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration)

#### KeyboardInterrupt

- Raised when the user pressed <kbd>ctrl</kbd> + <kbd>c</kbd> on their keyboard

- There is no way of "fixing" this but you can bypass this by using a [`try-except`](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) block

- Examples can be found in [`/Examples`](./Examples/KeyboardInterruptSolve.py)

- Official Documentation of [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt)
