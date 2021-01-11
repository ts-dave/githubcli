# githubcli
githubcli is a command line utility written in Python which takes a string as an argument, logs into github account and create empty repository. Then  clones the repository into the directory where the utility was called.

It was created to help help speed up the development process. It automates the process of creating github repo and cloning unto local device.

## Prerequisites
* python >= 3.7
* click == 7.1.2


* Chrome browser
* chrome webdriver

## Installing and using githubcli

* Download and install Chrome browser
* Download chromedriver.exe and add to path

Installation:

* clone repository
    ```git clone <link>```
* change directory into project folder
    ```cd githubcli```
* run setuptools in development mode
    ```pip install --editable .```


Usage:

    github --name <repo_name>
    
    or
    
    github -n <repo_name>


## Contributing to WebSearchCLI
To contribute to WebSearchCLI, follow these steps:

1. Fork this repository.
2. Create a branch: git checkout -b <branch_name>.
3. Make your changes and commit them: git commit -m '<commit_message>'
4. Push to the original branch: git push origin <project_name>/<location>
5. Create the pull request.
6. Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors
* [@ts-dave](https://github.com/ts-dave)

## Contact
You can contact me via email at [emsonjunior@gmail.com](emsonjunior@gmail.com).

## License
This project uses the [MIT License](https://opensource.org/licenses/MIT)
