cd "$(dirname "$0")" || exit
source venv/bin/activate
python app.py --datasets dataset_b dataset_tp --weights 1 1 --pictures pictures_b --access-token <insert_token_here> --group-id 201226651 --post-period 30
