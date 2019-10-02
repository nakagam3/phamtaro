from slackbot.bot import Bot
import logging

logging.basicConfig(level=logging.INFO)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
