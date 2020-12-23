import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--datasets', nargs='+', type=str)
parser.add_argument('--weights', nargs='+', type=float)
parser.add_argument('--pictures', nargs='+', type=str)
parser.add_argument('--access-token', type=str)
parser.add_argument('--group-id', type=int)
parser.add_argument('--post-period', type=int)
args = parser.parse_args()

DATASET_PATHS = args.datasets
DATASET_WEIGHTS = args.weights
PICTURES_PATHS = args.pictures

ACCESS_TOKEN = args.access_token
GROUP_ID = args.group_id

POST_PERIOD=args.post_period
