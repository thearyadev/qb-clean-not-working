# removes torrents with the "Not working" status. 
deletes files too.

tested on qbittorrent v5.1.1. 

if its not working update your python-qbittorrent package.

if its still not working the code has been killed by bit rot.

# usage

```bash
uv sync
uv run main.py <qb_url> <username> <password>
# or 
pip install -r requirements.txt
python3 main.py <qb_url> <username> <password>

```
optionally use the --dry-run flag to find the torrents it will be deleting without deleting the torrent

```bash
uv run main.py <qb_url> <username> <password> --dry-run
```

# license
wtfpl
