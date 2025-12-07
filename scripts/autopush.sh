#!/usr/bin/env bash
# Simple autopush script: stages, commits, and pushes.
# Usage: ./scripts/autopush.sh [commit-message]

set -euo pipefail
MSG=${1:-rez3}

# Find repo root
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
if [ -z "$REPO_ROOT" ]; then
  echo "Not a git repository (or git not installed)."
  exit 1
fi
cd "$REPO_ROOT"

BRANCH=$(git rev-parse --abbrev-ref HEAD)
REMOTE=$(git remote | head -n1 || true)
if [ -z "$REMOTE" ]; then
  echo "No git remote configured. Please add a remote first."
  exit 1
fi

STATUS=$(git status --porcelain)
if [ -z "$STATUS" ]; then
  echo "No changes to commit."
  exit 0
fi

echo "Staging changes..."
git add .

echo "Committing with message: '$MSG'"
git commit -m "$MSG"

echo "Pushing to $REMOTE/$BRANCH..."
git push "$REMOTE" "$BRANCH"

echo "Push complete."
