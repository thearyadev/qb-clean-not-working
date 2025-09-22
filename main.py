from qbittorrent import  Client
import argparse

args = argparse.ArgumentParser()
args.add_argument("qb_url")
args.add_argument("username")
args.add_argument("password")
args =args.parse_args()

qb = Client(args.qb_url)
qb.login(args.username, args.password)
for torrent in qb.torrents():
    trackers = qb.get_torrent_trackers(torrent["infohash_v1"])[-1]
    if (trackers["status"] == 4):
        print(f"tracker: {trackers['url']}; status: {trackers['msg']}")
        qb.delete_permanently(torrent["infohash_v1"])



