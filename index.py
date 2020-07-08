from selenium.webdriver.firefox.options import Options
from assets.script import Shortcuts
from selenium import webdriver
from assets import script
from time import sleep
import yaml
import os

with open("assets/config.yaml", "r") as config:
    config = yaml.safe_load(config)

options = Options()
if config.get("settings").get("headless"):
    options.headless = True

for login in config.get("accounts"):
    profile = webdriver.Firefox(executable_path=config.get("settings").get("firefox"), service_log_path=os.path.devnull if not config.get("settings").get("log") else config.get("settings").get("log"), options=options)
    script.log(login, "Created a firefox profile")
    profile.implicitly_wait(5)

    profile.get(Shortcuts.DISCORD_LOGIN)
    script.log(login, "Redirecting to discord login page")
    profile.execute_script(script.text.format(login))
    script.log(login, "Executed javascript to login to account")

    profile.get(Shortcuts.TOP_GG_LOGIN)
    profile.find_element_by_xpath(Shortcuts.AUTHORIZE_BUTTON).click()
    script.log(login, "Top.gg has been logged into")

    profile.get(Shortcuts.TOP_GG_VOTE)
    profile.find_element_by_xpath(Shortcuts.VOTE_BUTTON).click()
    script.log(login, f"Attempted to vote for {Shortcuts.DISCORD_BOT}")

    sleep(3)

    profile.quit()
    script.log(login, "Closed browser\n")
