#!/usr/bin/env bash
set -euo pipefail

PROJECT="chefpp"
REGION="us-central1"
REPO="chefplusplus"
IMAGE="chefplusplus"
TAG="${1:-latest}"

REGISTRY="${REGION}-docker.pkg.dev/${PROJECT}/${REPO}/${IMAGE}:${TAG}"

echo "==> Authenticating Docker with Artifact Registry..."
gcloud auth configure-docker "${REGION}-docker.pkg.dev" --quiet

echo "==> Building image..."
docker build -t "${IMAGE}" .

echo "==> Tagging: ${REGISTRY}"
docker tag "${IMAGE}" "${REGISTRY}"

echo "==> Pushing to Artifact Registry..."
docker push "${REGISTRY}"

echo "==> Done! Image pushed to ${REGISTRY}"
