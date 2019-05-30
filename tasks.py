from invoke import task, exceptions


@task
def test(c, branch):
    branches = ["practico_01", "practico_02", "practico_03", "practico_03a",
                "practico_04", "practico_05", "practico_06",
                ]

    if branch.lower() not in branches:
        raise exceptions.Exit(message=f"Incorrect Branch Name - The possible branch names are: {', '.join(branches[:-1])} and {branches[-1]}.", code=1)

    command = f"pipenv run pytest practica/tests/test_{branch}"

    c.run(command)
