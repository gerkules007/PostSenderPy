import asyncio
from Telegram.Controller import tbot_controller


async def main():
    await tbot_controller()

if __name__ == '__main__':
    asyncio.run(main())
