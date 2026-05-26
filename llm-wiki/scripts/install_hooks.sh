#!/usr/bin/env sh
set -eu

git config core.hooksPath llm-wiki/.githooks
echo "Git hooks installed from llm-wiki/.githooks"
