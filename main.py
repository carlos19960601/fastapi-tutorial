import os

import click
import uvicorn

from core.config import config


@click.command()
@click.option("--env", default="dev", help="运行环境", type=click.Choice(["dev", "prod"], case_sensitive=False))
@click.option("--debug", default=False, help="是否debug", type=click.BOOL, is_flag=True)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)

    print(config.APP_HOST, config.APP_PORT)

    uvicorn.run(
        "app.server:app", 
        host=config.APP_HOST, 
        port=config.APP_PORT, 
        reload=True if config.ENV != "prod" else False,
        workers=1
    )

if __name__ == "__main__":
    main()