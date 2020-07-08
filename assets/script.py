text = """
setInterval(() => {{
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{}"`
}}, 50);

setTimeout(() => {{
    location.reload();
}}, 2500);
"""

import yaml

with open("assets/config.yaml", "r") as config:
    config = yaml.safe_load(config)

class Shortcuts:
    DISCORD_LOGIN = "https://discord.com/login"
    TOP_GG_LOGIN = "https://top.gg/login"
    TOP_GG_VOTE = config.get("bot").get("page")
    AUTHORIZE_BUTTON = '//button[normalize-space()="Authorize"]'
    VOTE_BUTTON = '//span[normalize-space()="Vote"]'
    DISCORD_BOT = config.get("bot").get("name")

def log(login, message):
    print(f"[{login}] {message}")
