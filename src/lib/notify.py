import os
from entities.ad import Ad


def __install_deps() -> None:
    os.system("brew install terminal-notifier")


def __has_necessary_deps() -> bool:
   # TODO get stdout
    stdout = ""
    os.system("brew list | grep terminal-notifier")

    return bool(stdout)


def __notify(
    icon: str,
    link: str,
    message: str,
    title: str
):
    app_icon = "src/imgs/olx.png"
    command = f"terminal-notifier -appIcon {app_icon} -message \"{message}\" -title \"{
        title}\" -open \"{link}\" -contentImage \"{icon}\" -sound default"

    if not __has_necessary_deps():
        __install_deps()

    os.system(command)


def notify(term: str, ads: list[Ad]):
    for ad in ads:
        __notify(
            icon=ad.thumbnail,
            link=ad.url,
            message=f"{ad.price} - {ad.title}",
            title=f"New offer for {term}"
        )
