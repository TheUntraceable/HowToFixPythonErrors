# **How To Fix Python Errors**

**This repo will contain a README with an explanation as to why the error is happening and how to fix it.**

1. **NameError**

    - This error is usually occuring because you haven't defined the variable and are just using it.

    - To fix it you should define it like `VariableName = AnythingHere`.

        > - **Note. You mustn't define VariableName as another non existant variable. This will get you back to step one.**

    - Examples can be found in [`./Examples`](https://github.com/TheUntraceable/HowToFixPythonErrors/tree/main/Examples)

2. **IndexError**
    - This error is usually raised when attempting to retrieve an index from a sequence and the index isn't found in the sequence.

    - To fix make sure the index is a number inside the sequence

        > - **Note. in python counts from 0 therefore one will be 0, two will be 1, three will be 2 and so on.**

    - Examples can be found in [`./Examples`](https://github.com/TheUntraceable/HowToFixPythonErrors/tree/main/Examples)

3. **IndentationError**
    - This error occurs when the code expects an indent or you indented a line too much than expected.

    - To fix it, get everything under a `:` in the same indent

        > - **Note: lines below a `:` need to be indented. If there is no `:` in the line above then it should be in the same indentation level as the line above**

    - Examples can be found in [`./Examples`](https://github.com/TheUntraceable/HowToFixPythonErrors/tree/main/Examples)

    - Note that using both tabs and spaces when indenting will raise TabError. stick to either spaces or tabs, not both

4. **ImportError**
    - This specific error is raised when you try to import a module that is not installed / doesnt exist.

    -  To fix it, search in [pypi.org](https://pypi.org) and see if it actually exists, and install it

       > -  **First, make sure you dont have anyy spelling mistakes in the import statement**

    - Examples can be found in [`./Examples`](https://github.com/TheUntraceable/HowToFixPythonErrors/tree/main/Examples)
