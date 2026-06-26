"""Generate a daily market brief and send it to Discord."""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import WATCHLIST, ConfigError, load_settings
from src.discord_client import send_briefing
from src.openai_client import generate_market_brief


def main() -> int:
    try:
        settings = load_settings()
        briefing = generate_market_brief(settings.openai_api_key, WATCHLIST)
        send_briefing(settings.discord_webhook_url, briefing)
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Daily brief failed: {exc}", file=sys.stderr)
        return 1

    print("Daily brief sent to Discord.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
