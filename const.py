import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str)
parser.add_argument('--pictures', type=str)
parser.add_argument('--access-token', type=str)
parser.add_argument('--group-id', type=int)
parser.add_argument('--post-period', type=int)
args = parser.parse_args()

DATASET_PATH = args.dataset
PICTURES_PATH = args.pictures

ACCESS_TOKEN = args.access_token
GROUP_ID = args.group_id

POST_PERIOD=args.post_period
