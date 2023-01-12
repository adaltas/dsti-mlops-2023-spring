
# Lab

Continuous Integration & Continuous Delivery (Deployment) (CI/CD)

## Objectives

1. Create an automated testing pipeline with GithHub Actions.
2. Get confortable with all the bricks we saw up to now: versioning, unit testing and defining automated workflows.

## Instructions

1. Finish the unit tests and functions you were writing. When you run `pytest` locally, all the tests should pass. 
2. `git init` your local unit testing project to make it a repository.
3. Push the repo to the GitHub.
  - **Hint**: Do you need to push everything? Is there something you need to list in **.gitignore**?
4. Use GitHub Actions to create a workflow for automated unit testing.
  - Click `Actions` in the horizontal menu
  - Select `Python application` from the template
  - Delete everything related to flake8
  - Commit
  - Fix the issues
5. Write additional test on your laptop. Push it to the repo and observe the workflow being executed.

## Extras

When you are done, you can explore the folowing topics:

- Test different branches or event triggers
- Discover linting with [flake8](https://www.blog.pythonlibrary.org/2019/08/13/an-intro-to-flake8/)
- Read about [python packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/). Try to create one and push it to PyPI. This would conclude Continuous Delivery pipeline.
