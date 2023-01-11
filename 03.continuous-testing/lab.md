
# Lab

Continuous testing

## Objectives

1. Learn how to write and run unit tests for your functions
2. Use test-driven development (TDD)

## Before starting

1. Create and activate virtual environment: `env_mlops`
2. In this virtual environment install `pytest`: `pip install pytest`
3. Set PYTHONPATH otherwise the modules will not be found (instructions)[https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html]. This is a temporary setting and you need to do it each time you open the terminal.

```
$ export PYTHONPATH="$PWD/src"
$ echo $PYTHONPATH
```

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

Run tests by running `pytest` in the terminal from the directory you defined as PWD before.

Help yourself with the [pytest documentation](https://docs.pytest.org/en/7.0.x/getting-started.html).

## Adding Redis database

The user data will be saved to the database.

We need to test:
- the integration with Redis
- existence of the users in the database

Installation instructions:

- **Windows:** https://redis.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/
- **MacOS:** `brew install redis` or https://redis.io/topics/quickstart
- **Linux or MacOS:** https://redis.io/topics/quickstart

After installation, start Redis server:

- **Windows:** double click on `redis-server.exe` file (keep it open)
- **MacOS and Linux:** `redis-server`

Test if the Redis server is running:

- **Windows:** double click on `redis-cli.exe` and run the `ping` command inside the REPL
- **MacOS and Linux:** run in a new terminal window `redis-cli ping` (should answer with "PONG")

## Test-driven development (TDD)

Develop a function that will test if the input string is a palindrom. Use TDD to do that.
