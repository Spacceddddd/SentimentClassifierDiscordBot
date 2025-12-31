# Discord Sentiment Analysis Bot

A Discord bot that asks thought-provoking questions and analyzes the sentiment of user responses using machine learning.

## Features

- **Random Question Generator**: Asks users one of 14 diverse questions on politics, ethics, and social issues
- **Sentiment Analysis**: Uses HuggingFace transformers to classify responses as positive or negative
- **Slash Commands**: Modern Discord interactions including:
  - `/yello` - Say hello
  - `/mirror` - Echo user messages
  - `/embed` - Display formatted embeds with content
  - `/button` - Interactive buttons with responses
- **Message Tracking**: Logs edited and deleted messages
- **Reaction Handling**: Responds when users react to messages

## Prerequisites

- Python 3.8+
- Discord.py library
- HuggingFace Transformers library

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Or install manually:
```bash
pip install discord.py transformers torch
```

## Setup

1. Create a Discord application and bot at [Discord Developer Portal](https://discord.com/developers/applications)
2. Get your bot token
3. Update the bot token in the script (last line):
   ```python
   client.run('YOUR_BOT_TOKEN_HERE')
   ```
4. Update the Guild ID to your server's ID:
   ```python
   GUILD_ID = discord.Object(id=YOUR_GUILD_ID)
   ```

## Running the Bot

```bash
python "discordbot copy.py"
```

The bot will log in and start listening for messages.

## Usage

### In Discord:

- Type `hello` - Bot responds with a greeting
- Type `ask me a question` - Bot asks a random thought-provoking question and waits for your response
- Reply to the question - Bot analyzes sentiment (positive/negative) of your answer
- Use slash commands:
  - `/yello` - Get a hello message
  - `/mirror [text]` - Echo text back
  - `/embed` - View a formatted message
  - `/button` - See interactive buttons

## Questions Asked

The bot asks about:
- Political figures and positions
- Weapons and nuclear policy
- Taxes and economics
- AI regulation
- Climate change
- Social media in politics
- Universal basic income
- Healthcare systems
- Education costs
- Cancel culture
- Privacy vs Security

## Example Output

```
Bot: Do you think nuclear weapons should be banned and why?
User: Yes, they're too dangerous
Bot: Your results
[{'label': 'NEGATIVE', 'score': 0.99}]
```

## Architecture

- **Client Class**: Custom Discord bot with event handlers
- **Sentiment Pipeline**: Pre-trained model for text classification
- **Views & Buttons**: UI components for interactive responses

## Notes

- ⚠️ Keep your bot token private! Do not share it or commit it to public repositories
- The sentiment analysis uses a pre-trained DistilBERT model
- First run will download the model (~250MB)

## Troubleshooting

- **"Timeout context manager" error**: Remove `nest_asyncio` when running as a standalone script
- **Token errors**: Verify your token is valid and hasn't been regenerated
- **Guild not syncing**: Ensure the Guild ID matches your Discord server

## Future Improvements

- Add a database to store sentiment results
- Create analytics dashboard
- Add more diverse questions
- Implement user profiles and stats
- Add moderation features

---

Made as part of "100 Days of ML" challenge
