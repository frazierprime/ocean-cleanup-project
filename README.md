# ocean-cleanup-project
Notebooks and utilities for the [ocean cleanup project](https://resources.kili-technology.com/the-ocean-cleanup-challenge).

# Links
## Kili SDK
https://github.com/kili-technology/kili-python-sdk
https://pypi.org/project/kili/

## automl
https://github.com/kili-technology/automl

## Dependencies
python version = ^3.9
Create a kili community account [here](https://cloud.kili-technology.com/label/).
Create a kili client api key [here](https://docs.kili-technology.com/docs/creating-an-api-key).
set api key in your env:
```bash
export KILI_API_KEY='<you_api_key_here>'
```

Assumes usage of conda for managing the env.
Create an env and install dependencies:
```bash
conda create -n ocean-cleaup python=3.9.11
conda activate ocean-cleanup
poetry config virtualenvs.create false
poetry install
```