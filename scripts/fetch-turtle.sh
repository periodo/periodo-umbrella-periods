#!/usr/bin/env bash

PERIODO_DEFINITION_URL="https://test.perio.do/d.json"

if [[ -d "./data" ]]
then
  echo "Deleting local dataset cache...";
  rm -r ./data;
fi

mkdir ./data

echo "Creating local dataset cache...";

curl -L -o ./data/periodo-data.jsonld ${PERIODO_DEFINITION_URL}

if ! type "riot" > /dev/null
then

    echo "No local version of riot found. Trying with docker...";

    docker run stain/jena \
        riot --formatted=turtle --syntax=jsonld ${PERIODO_DEFINITION_URL} > ./data/periodo-data.ttl

    docker run stain/jena \
        riot --formatted=turtle --syntax=jsonld ${PERIODO_DEFINITION_URL} > ./data/periodo-data.staging.ttl
else

    riot --formatted=turtle --syntax=jsonld ${PERIODO_DEFINITION_URL} > ./data/periodo-data.ttl

    rriot --formatted=turtle --syntax=jsonld ${PERIODO_DEFINITION_URL} > ./data/periodo-data.staging.ttl

fi

echo "Local dataset cache created successfully!";