cd "$(dirname "$0")" || exit
source venv/bin/activate
python app.py --datasets dataset_wolf --weights 1 --pictures pictures_wolf --access-token <insert_token_here> --group-id 201211851 --post-period 30
