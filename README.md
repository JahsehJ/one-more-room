# One More Room

Simplest solution to messy voice chats

## How it works

If no more empty channel is presented, a new one will be created. (Auto-scaling)  
This means there will always be 1 extra room for other members!

## Run it

### Requirements
- python >= 3.11
- discord.py >= 2.3

```
# Using a venv is always preferred
python3 bot.py
```

## Important notes
- Stage channels are ignored
- Manage channel permission is required (Channels bot has no access to are ignored)
- Bot has to be up for 24/7, if not, channel duplication is expected