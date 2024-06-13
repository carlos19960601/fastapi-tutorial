import os

import click


def main(env: str):
    os.environ["ENV"] = env

if __name__ == "__main__":
    main()