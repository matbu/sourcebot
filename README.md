# SourceBot
Chat bot which takes as entry our own sources and generate content from our sources


## Install sourcebot

You just have to git clone this repository and then create a python3 virtualenv in order to install the dependencies:

```
python3 -m venv venv
source venv/bin/activate
# Then clone the project
git clone https://github.com/matbu/sourcebot
pushd sourcebot
make install
```

## Run sourcebot

Once it's installed correctly you can start to use it with your own personnal documents or whatever documents online such as this example:

```
sourcebot --ingest https://en.m.wikipedia.org/wiki/Banksy  --chat
```

Then ask whatever you need to the sourcebot, enjoy !


## Quick demo

Here is a quick asciinema demo:

[![asciicast](https://asciinema.org/a/m42xHvdqLHfmkcYKRI4RA4R3D.svg)](https://asciinema.org/a/m42xHvdqLHfmkcYKRI4RA4R3D)