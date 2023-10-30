from dataclasses import dataclass
import sqlite3
from uuid import UUID
from datetime import datetime
from enum import Enum, auto


class StrategyStatus(Enum):
    INITIALIZED = auto()
    OPENING = auto()
    OPENED = auto()
    CLOSING = auto()
    CLOSED = auto()
    CANCELLED = auto()


@dataclass
class Strategy:
    id: UUID
    created_at: datetime
    op_id: UUID
    currency_ticker: str
    op_initial_contribution: int
    status: StrategyStatus


@dataclass
class Contribution:
    id: UUID
    created_at: datetime
    strategy_id: UUID
    user_id: UUID
    value: int


@dataclass
class Trade:
    id: UUID
    created_at: datetime
    strategy_id: UUID
    sell_volume: int
    buy_volume: int


class DatabaseController:
    def __init__(self) -> None:
        self.con = sqlite3.connect("database.db")
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self) -> None:
        self.cur.executescript(
            """
                CREATE TABLE IF NOT EXISTS "strategies" (
                    "id" TEXT PRIMARY KEY NOT NULL, -- assuming you'll use UUID strings
                    "created_at" TIMESTAMP NOT NULL, -- you'll have to set this in your application
                    "op_id" TEXT NOT NULL,
                    "currency_ticker" TEXT NOT NULL,
                    "op_initial_contribution" INTEGER,
                    "status" TEXT NOT NULL -- changed from ENUM to TEXT
                );

                CREATE TABLE IF NOT EXISTS "contributions" (
                    "id" TEXT PRIMARY KEY NOT NULL, -- assuming you'll use UUID strings
                    "created_at" TIMESTAMP NOT NULL, -- you'll have to set this in your application
                    "strategy_id" TEXT NOT NULL,
                    "user_id" TEXT NOT NULL,
                    "value" INTEGER,
                    FOREIGN KEY ("strategy_id") REFERENCES "strategies" ("id")
                );

                CREATE TABLE IF NOT EXISTS "trades" (
                    "id" TEXT PRIMARY KEY NOT NULL, -- assuming you'll use UUID strings
                    "created_at" TIMESTAMP NOT NULL, -- you'll have to set this in your application
                    "strategy_id" TEXT NOT NULL,
                    "sell_volume" INTEGER,
                    "buy_volume" INTEGER,
                    FOREIGN KEY ("strategy_id") REFERENCES "strategies" ("id")
                );
            """
        )

    def get_all_strategies(self) -> list[Strategy]:
        pass

    def get_strategy_by_id(self, id) -> Strategy:
        pass
