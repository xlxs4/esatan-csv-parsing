## Description

To run the script you're going to need:

- The [Python](https://www.python.org/) programming language
- [Poetry](https://python-poetry.org/docs/#installation)

To generate a plot (or plots) for your CSV, [clone](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#clone-a-repository) this repository, copy or paste the CSV in the repository (`utilities` folder), then:

- Navigate to the `utilites` folder
- If it's the first time you're doing this, run `poetry install` in your terminal
- Run `poetry shell` in your terminal
- Edit `src/config.toml` and add the filename of your CSV there
- Execute the script by running `python3 src/main.py` in your terminal