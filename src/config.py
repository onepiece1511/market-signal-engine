"""Configuration for the market signal engine."""

import os
from dataclasses import dataclass


WATCHLIST = ("NVDA", "TSLA", "PLTR", "AMD", "AAPL")


class ConfigError(RuntimeError):
    """Raised when required configuration is missing or invalid."""


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    discord_webhook_url: str


def load_settings() -> Settings:
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
    discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL", "").strip()

    missing = []
    if not openai_api_key:
        missing.append("OPENAI_API_KEY")
    if not discord_webhook_url:
        missing.append("DISCORD_WEBHOOK_URL")

    if missing:
        raise ConfigError(f"Missing required environment variable(s): {', '.join(missing)}")

    valid_discord_prefixes = (
        "https://discord.com/api/webhooks/",
        "https://discordapp.com/api/webhooks/",
    )
    if not discord_webhook_url.startswith(valid_discord_prefixes):
        raise ConfigError("DISCORD_WEBHOOK_URL does not look like a Discord webhook URL")

    return Settings(
        openai_api_key=openai_api_key,
        discord_webhook_url=discord_webhook_url,
    )
