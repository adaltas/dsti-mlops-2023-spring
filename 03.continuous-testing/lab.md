
# Lab

Continuous testing

## Objectives

Learn how to write and run unit tests for your functions

## Lab context

Imagine you are developing an application, where users need to register. They need to fill in their get username, email and password.

Your job is to write the functions that will accept those parameters from the user input (in command line) and test if they follow the criteria:

- user name:
  - not empty
  - no spaces
- password:
  - at least 8 characters
  - at least one number
  - at least one letter
  - at least one special character
- email:
  - contains `@` and `.`

Copy the text in the file `sample_code.py` (or clone or download the repository). Rename the file to `test_sample_code.py`,
since naming conventions need to be respected in order for pytest to run.   

Run tests by running `pytest` in the Anaconda terminal from the directory with your file.

Help yourself with the [pytest documentation](https://docs.pytest.org/en/7.0.x/getting-started.html).
