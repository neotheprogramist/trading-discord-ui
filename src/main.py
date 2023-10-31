import asyncio
from db import DatabaseController, Strategy, StrategyStatus
from uuid import uuid4
from datetime import datetime


async def main():
    controller = DatabaseController()

    example_strategy = Strategy(
        uuid4(), datetime.now(), 1, 1, "BTCUSDT", 100, StrategyStatus.INITIALIZED
    )
    controller.add_strategy(example_strategy)

    fetched_strategy = controller.get_strategy_by_discord_id(1)
    print(fetched_strategy)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
