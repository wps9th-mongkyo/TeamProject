#!/usr/bin/env bash
git add -f .secrets/
eb deploy --profile eb --staged &
sleep 3
git reset HEAD .secrets/