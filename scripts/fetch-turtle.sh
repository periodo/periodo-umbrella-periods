#!/usr/bin/env bash

if [ -d "./data" ]
then
  echo "Deleting local dataset cache...";
  rm -r ./data;
fi

mkdir ./data

echo "Creating local dataset cache...";

if ! type "riot" > /dev/null
then

    echo "No local version of riot found. Trying with docker...";

    docker run stain/jena \
        riot --formatted=turtle http://n2t.net/ark:/99152/p0d.jsonld > ./data/periodo-data.ttl

    docker run stain/jena \
        riot --formatted=turtle https://staging.perio.do/d.jsonld > ./data/periodo-data.staging.ttl
else

    riot --formatted=turtle http://n2t.net/ark:/99152/p0d.jsonld > ./data/periodo-data.ttl

    riot --formatted=turtle https://staging.perio.do/d.jsonld > ./data/periodo-data.staging.ttl

fi

echo "Local dataset cache created successfully!";
