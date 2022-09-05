# Contributing

Thank you for you interest in contributing to the S3 metadata tagger!
To ensure a frictionless entry into our project, please have a quick look at this document before participating in its development:

## Goal of the project
s3-metadata-tagger is a library to add metadata to objects stored in s3.

Any larger code contribution probably falls into one of the two following
categories:
* Improvements to [object_tagger.py](src/metadata_tagger/object_tagger.py). It is responsible for downloading files and invoking metadata extractors. While the execution flow is largely finished, it is always open for improvements and refinements.
* Additions of new metadata extractors. Those sub-packages extract meta-information from files (like pages in a pdf). Any addition of extractors is always welcome, but if its dimensions grow above a certain size, consider moving it to a seperate repo and deploying it as a library which interfaces to this package (An example for this would be if the extractor depended on certain software being installed at the host)

## Development tools
To avoid deployment/quality issues, we are employing a wide array of tools:

### Python version management
To ensure everyone is on the same python version, we recommend using [pyenv](https://github.com/pyenv/pyenv), which reads the
local [.python-version](.python-version) file and locally provides the configured version.
We furthermore recommend to create a local virtual environment to encapsulate all installed packages to the `s3-metadata-tagger` project directory.
Please do not change the `python version` without previous communication with the projects maintainers.

### Testing
Testing is currently done with the [unittest](https://docs.python.org/3/library/unittest.html) framework.
If more complicated tests are needed in your eyes, feel free to recommend an additional framework.

### Linting
We are using [pylint](https://github.com/PyCQA/pylint) for code linting.

### Packaging
For packaging, [setuptools](https://setuptools.pypa.io/en/latest/) is used.
Since deployment is done via GitHub actions (see [deploy.yml](.github/workflows/deploy.yml)), you
do not need to install the tool locally.
If a new version of the package is released, it has to be adjusted in [pyproject.toml](./pyproject.toml)

### Security scanning
To avoid including vulnerable packages, both [trivy](https://aquasecurity.github.io/trivy/v0.31.3/) and [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) and executed on every commit to an open pull request.
They are not really cut out for our use case, but should serve so far.
If you have any better suggestions, feel free to open an issue for it!

## Git
Naturally, we use git to do version control and to manage
 source code extensions.

### Branching
When developing, please create a new branch from the `staging` branch.
The branch name starts with the class of the branch, followed by a
slash and a one- or two-worded identifier for the branch.
The classes are as follows:

| Prefix     | Description                                                               | Example                                                                |
| ---------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| feature/   | A new feature is being developed.                                         | Parametrizable placeholders                                            |
| fix/       | A bug is fixed.                                                           | `Null Pointer Exception` when resolving the same placeholder two times |
| refactor/  | We change some existing implementation for stability/performance reasons. | Use Enum-based `switch-case` for resolving in the `ReflectionResolver` |
| polishing/ | Collection branch of smaller refactoring.                                 | Switch to `instanceof` pattern matching                                |
| cicd/      | Changes are done to the CI/CD pipeline.                                   | Add testing coverage to sonarqube                                      |
| doc/       | Documentation is added or changed .                                       | Clarify examples                                                       |


### Commits
Please try to group commits so that each commit bundles a set of
joint code changes.
For example, assemble one commit `Add infrastructure` and one 
`Add tests`
The commit message should follow the guidelines described in 
[How to write a commit message](https://chris.beams.io/posts/git-commit/)
by Chris Beams.

## GitHub
We use GitHub to manage the source code, keep track of issues, and
handle pull requests.

### Issues
If your contribution requires some discussion it might be useful
to create an issue first, describing the problem you are facing.
If you already have some path of action in mind you can also open a
 `WIP:` pull request directly.

### Pull requests
Pull requests should be done to the `staging` branch.
When opening a pull request, please give it a meaningful name and
description.
Either link to the corresponding issue or describe the problem in the
pull request if it is of a size not warranting opening an issue.
Furthermore, please add the applicable tags and request a review by
a maintainer.
Each PR needs to confirm to the linting and sonarqube requirements, and should add a reasonable set of tests for any added code.
Please also add appropriate logging, so that issues further down the roead can be triaged faster.
If any issues arise with trivy or owasp, please check back with the project maintainers.

## Versioning and Release Policy
The S3 metadata tagger follows the [Semantic Versioning](https://semver.org/) versioning scheme.
In short, the version is given as `x.y.z`
* Bug fixes, which do not change anything about the interface and introduce no new features increase `z`
* Versions containing new features, which do not influence the existing interfaces increase the `y`
* Releases introducing breaking changes increase the `z`.

There is no fixed release schedule, new versions are released whenever a contained set of changes can be deployed.
Each new version is first deployed on the `staging` branch, which releases a new package version to 
[test.pypi.org](https://test.pypi.org/).
After successful testing, the`staging` branch is merged into the `production` branch, which pushes the package to
[pypi.org](https://pypi.org/).

The releases to [test.pypi.org](https://test.pypi.org/) and [pypi.org](https://pypi.org/) are done via github 
actions (see [deploy.yml](.github/workflows/deploy.yml)).

## Dependabot
Dependabot is enabled for this repository to keep the github actions and the python dependencies up-to-date.

## Maintainers
* [@alexpartsch](https://github.com/alexpartsch)
* [@AntonOellerer](https://github.com/AntonOellerer)

## Further links
* The projects [README.md](README.md)
* The projects [ARCHITECTURE.md](ARCHITECTURE.md)
* [pyenv](https://github.com/pyenv/pyenv)
* The [python packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* The [setuptools guide](https://setuptools.pypa.io/en/latest/userguide/)