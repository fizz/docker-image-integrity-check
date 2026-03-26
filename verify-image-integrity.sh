#!/usr/bin/env bash
# verify-image-integrity.sh — detect stale Docker build cache layers
#
# Compares the source tree on disk against the files inside a built image.
# If the hashes don't match, the build cache served stale COPY layers.
#
# Usage:
#   verify-image-integrity.sh <image> [app-dir-in-image] [source-dir]
#
# Examples:
#   verify-image-integrity.sh myapp:latest /app .
#   verify-image-integrity.sh 835661413200.dkr.ecr.us-east-1.amazonaws.com/nistapp-apiserver:abc123 /app backend/src
#
# Exit codes:
#   0 — image contents match source tree
#   1 — mismatch detected (stale cache)
#   2 — usage error

set -euo pipefail

IMAGE="${1:-}"
APP_DIR="${2:-/app}"
SOURCE_DIR="${3:-.}"

if [ -z "$IMAGE" ]; then
  echo "Usage: verify-image-integrity.sh <image> [app-dir-in-image] [source-dir]"
  exit 2
fi

echo "Verifying image integrity..."
echo "  Image:      $IMAGE"
echo "  App dir:    $APP_DIR"
echo "  Source dir:  $SOURCE_DIR"
echo ""

# Hash the source tree — all non-hidden files, sorted for determinism
SOURCE_HASH=$(find "$SOURCE_DIR" \
  -not -path '*/.git/*' \
  -not -path '*/.github/*' \
  -not -path '*/__pycache__/*' \
  -not -path '*/.venv/*' \
  -not -name '*.pyc' \
  -type f | sort | xargs sha256sum | sha256sum | cut -d' ' -f1)

# Hash the same files inside the image
IMAGE_HASH=$(docker run --rm --entrypoint sh "$IMAGE" -c "find $APP_DIR \
  -not -path '*/.git/*' \
  -not -path '*/.github/*' \
  -not -path '*/__pycache__/*' \
  -not -path '*/.venv/*' \
  -not -name '*.pyc' \
  -type f | sort | xargs sha256sum | sha256sum | cut -d' ' -f1")

echo "  Source hash: $SOURCE_HASH"
echo "  Image hash:  $IMAGE_HASH"
echo ""

if [ "$SOURCE_HASH" = "$IMAGE_HASH" ]; then
  echo "✅ Image contents match source tree"
  exit 0
else
  echo "❌ Image contents DO NOT match source tree"
  echo ""
  echo "The Docker build cache may have served stale COPY layers."
  echo "Rebuild with --no-cache to verify."
  exit 1
fi
