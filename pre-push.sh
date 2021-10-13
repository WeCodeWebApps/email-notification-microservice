# update requirement if any new added
echo "1. Updating requirments.txt ..."
poetry export --without-hashes -o requirements.txt

# run black to format code
echo "2. formatting code ..."
poetry run black .
