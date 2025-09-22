from qbittorrent import  Client
import argparse

args = argparse.ArgumentParser()
args.add_argument("qb_url")
args.add_argument("username")
args.add_argument("password")
args.add_argument("--dry-run", default=False, action="store_true" )
args =args.parse_args()

qb = Client(args.qb_url)
qb.login(args.username, args.password)
for torrent in qb.torrents():
    torrent_hash = torrent.get("infohash_v1") or torrent.get("infohash_v2")
    trackers = qb.get_torrent_trackers(torrent_hash)[-1]
    if (trackers["status"] == 4): # not working
        print(f"[{'DRY' if args.dry_run else ''}]deleting torrent: {torrent['name']}tracker: {trackers['url']}; status: {trackers['msg']}")
        
        if not args.dry_run:
            qb.delete_permanently(torrent_hash)




