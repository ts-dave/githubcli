from decouple import config
from selenium import webdriver
import click

# Github login credentials from .env
EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

@click.command()
@click.option('--name', '-n', help='Name for github repo', prompt="Enter name for github repository")
@click.option('--privacy', '-p', help='Private or Public repo', prompt='Private or Public')
def main(name, privacy):
    """ A command line tool that takes a string as argument, logs into github and creates a repo (with a readme and gitignore file) with the string argument as the name. It then clones the empty repo to the current working directory where the command line tool was called. 

    Eg: github -n < repo_name >"""

    # configuring selenium and chrome browser with incognito option
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    # option.add_argument("disable-gpu")
    browser = webdriver.Chrome()
    browser.get("https://github.com/")
    browser.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()
    email = browser.find_element_by_xpath('//*[@id="login_field"]')
    email.send_keys(EMAIL)
    password = browser.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(PASSWORD)
    browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]').click()
    browser.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
    repo_name = browser.find_element_by_xpath('//*[@id="repository_name"]')
    repo_name.send_keys(name)
    
    if privacy == 'Public' or privacy == 'public':
        browser.find_element_by_xpath('//*[@id="repository_visibility_public"]').click()
    else:
        browser.find_element_by_xpath('//*[@id="repository_visibility_private"]').click()

    browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()
    







if __name__ == '__main__':
    main()