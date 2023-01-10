## Prerequisites:

- Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Create [GitHub account](https://github.com/) if you don't have it yet
- Install Conda (Anaconda/[Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- Create a virtual environment: `env_mlops`:
  `conda create --name env_mlops python=3.9`
- Activate the virtual environment in Anaconda Prompt:
  `conda activate env_mlops`

How do you know what environment is activated?

```bash
# Nothing activated, base environment
(base) ➜  ~
# An env_mlops virtual environment is activated
(env_mlops) ➜  ~
```

**Windows users:**

- Run the following code in Anaconda Prompt in activated virtual environment `env_mlops`.
- Install: `conda install pywin32`, `conda install m2-base`
- `m2-base` will enable you to use Linux commands in Anaconda Prompt. It is very useful for the future to get used to them :)
- If you cannot install `m2-base` and you need to use Windows commands, replace `ls` by `dir`, change `/` to `\` and `cp` to `copy` in the code below.

[Conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

**Note:** Everything will be installed and run in this virtual environment `env_mlops` or Databricks notebooks.
