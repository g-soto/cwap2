from tg import create_client
import asyncio as aio
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

    
if __name__ == '__main__':
    client = create_client()
    with aio.Runner() as runner:
        try:
            runner.run(client.start())
        except KeyboardInterrupt:
            runner.run(client.stop())
