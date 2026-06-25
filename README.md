# Market Signal Engine

Smallest working pipeline:

1. Generate a short AI market brief for `NVDA`, `TSLA`, `PLTR`, `AMD`, and `AAPL`.
2. Send the brief to a Discord webhook.

This version intentionally does not include SEC data, Reddit, X, Schwab, options data, databases, trading, dashboards, or Discord bot commands.

## Run locally

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set the required environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export DISCORD_WEBHOOK_URL="your-discord-webhook-url"
```

Run the job:

```bash
python jobs/daily_brief.py
```

## Run with Docker

Build the image:

```bash
docker build -t market-signal-engine .
```

Run the container:

```bash
docker run --rm \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  -e DISCORD_WEBHOOK_URL="$DISCORD_WEBHOOK_URL" \
  market-signal-engine
```

## Deploy later to Google Cloud Run Jobs

Build and submit the container:

```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/market-signal-engine
```

Create the Cloud Run Job:

```bash
gcloud run jobs create market-signal-engine \
  --image gcr.io/PROJECT_ID/market-signal-engine \
  --region REGION \
  --set-env-vars OPENAI_API_KEY=YOUR_OPENAI_API_KEY,DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL
```

Execute the job:

```bash
gcloud run jobs execute market-signal-engine --region REGION
```

For production, store secrets in Google Secret Manager instead of passing raw values in commands.
