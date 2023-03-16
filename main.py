import asyncio
import uvloop

async def main():
    print("async...")

uvloop.install()
asyncio.run(main())
