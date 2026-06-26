"""OpenAI integration for generating the market brief."""

from collections.abc import Sequence

DEFAULT_MODEL = "gpt-4o-mini"


def generate_market_brief(
    api_key: str,
    watchlist: Sequence[str],
    model: str = DEFAULT_MODEL,
) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    tickers = ", ".join(watchlist)

    response = client.responses.create(
        model=model,
        instructions=(
            "You write short, sober market watchlist notes for retail investors. "
            "Do not provide financial advice. Do not invent live prices, breaking "
            "news, filings, social posts, options flow, or analyst actions. "
            "Frame the brief as general watch areas for the listed tickers."
        ),
        input=(
            f"Create a concise daily market brief for this watchlist: {tickers}. "
            "Format it for Discord with a short title and 3 to 5 bullets. "
            "Keep it under 900 characters."
        ),
        max_output_tokens=300,
    )

    briefing = response.output_text.strip()
    if not briefing:
        raise RuntimeError("OpenAI returned an empty briefing")

    return briefing
