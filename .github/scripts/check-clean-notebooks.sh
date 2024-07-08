#!/usr/bin/env bash

set -e

# Install jq if necessary
if ! command -v jq &> /dev/null
then
    sudo apt-get update && sudo apt-get install -y jq
fi

for f in ./notebooks/*.ipynb; do
  echo "Checking $f"
  if jq -e 'any(.cells[]; .cell_type == "code" and .execution_count != null)' "$f" &>/dev/null; then
    echo "Error: Executed cells found in $f. Please clear all execution counts and commit again."
    exit 1
  fi
  echo "🎉 OK! No executed cells found in $f"
done

echo "🎉🎉🎉 All notebooks have no executed cells."
