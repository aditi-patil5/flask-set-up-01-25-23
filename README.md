# flask-set-up-01-25-23

## Set up
``pipenv --python 3.11``
Creates a pipfile

To get into virtual environment run: <br>
``pipenv shell``

``pipenv install`` Once to install the dependencies of the `Pipfile` and creates/updates `Pipfile.lock`.

``pipenv run pip freeze > requirements.txt`` to get the requirements into a legacy file system. 

To run the server <br>
`flask --app server run`

To exit virtual environment:<br>
`exit`

