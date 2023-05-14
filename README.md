# QUICKER  #

This framework can we used for testing of UI feature with selenium, we can also extent this for API 
test using request package

We are using [poetry](https://python-poetry.org/) here as dependency management tool

All the libraries which this framework is dependent on are listed [here](/Users/rahulvats/Documents/Automation/Pytestframwork/PycharmProjects/Quicker/pyproject.toml)


Please follow below steps to get the execution going
**pre-requisite**
1. Need Python version 3.9 or more
2. we should have poetry installed which can be installed using command "pip install poetry"

**Steps to run**
1. Execute below command to install dependencies
    poetry install
2. RUn command  poetry run pytest  --html-report=./report/report.html   --browser = chrome

3. results can be checked at Quicker/report/report.html

