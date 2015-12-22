# Yoyo Python Behave Template

A template repo for behave tests

## Requirements

* python 2.7.6+
* pip
* virtualenv
* virtualenvwrapper (optionally)


## Installing

Create a virtualenv and install the dependencies:

If you have virtualenvwrapper, then:

    $ mkvirtualenv behave
    (behave) $ pip install -r requirements.txt


Otherwise:

    $ virtualenv ./.env
    $ .env/bin/activate
    (behave) $ pip install -r requirements.txt


## Executing

To run all scenarios:

    (behave) $ behave

To run selected feature file:

    (behave) $ behave features/selected_feature_file.feature

To run selected scenario from a feature file:

    (behave) $ behave -k features/selected_feature_file.feature -n "name of the selected scenario"

Or

    (behave) $ behave -k -n "name of the selected scenario"

To run scenario(s) with specific tag:

    (behave) $ behave -k -t YOUR_TAG
