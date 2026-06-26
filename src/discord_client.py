"""Discord webhook integration."""


def send_briefing(webhook_url: str, briefing: str) -> None:
    import requests

    if not briefing.strip():
        raise ValueError("Cannot send an empty briefing to Discord")

    response = requests.post(
        webhook_url,
        json={"content": briefing},
        timeout=15,
    )
    response.raise_for_status()
