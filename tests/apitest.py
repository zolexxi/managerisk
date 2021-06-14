from pprint import pprint
import asyncio
from panoramisk import Manager


async def extension_status():
    manager = Manager(loop=asyncio.get_event_loop(),
                      host='192.168.0.106', port=5038,
                      username='hello', secret='world')
    await manager.connect()
    extension = await manager.send_action({'Action': 'PJSIPShowEndpoints',})
    manager.close()
    pprint(extension)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(extension_status())
    loop.close()


if __name__ == '__main__':
    main()