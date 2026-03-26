# docker-image-integrity-check

Detect stale Docker build cache layers by comparing source tree hashes against image contents.

## The problem

Docker buildx with `--cache-from type=gha` can serve a stale `COPY . /app` layer from a previous build. The source files change, but the cached layer doesn't invalidate. The image ships with old code. CI reports success.

I hit this in production — the source code had a new field in a pydantic Settings class, but the Docker image didn't. The `BUILD_COMMIT` env var was correct (set in an earlier stage) but the actual files were from a previous build. The only reason I caught it was that the app crashed on the missing field. A subtler change would have gone unnoticed.

## The check

`verify-image-integrity.sh` hashes all files in the source tree and compares against the same files inside the built image. If they don't match, the cache served stale code.

```bash
./verify-image-integrity.sh myapp:latest /app .
```

```
  Source hash: a1b2c3d4...
  Image hash:  a1b2c3d4...

✅ Image contents match source tree
```

If the hashes don't match:

```
  Source hash: a1b2c3d4...
  Image hash:  e5f6g7h8...

❌ Image contents DO NOT match source tree

The Docker build cache may have served stale COPY layers.
Rebuild with --no-cache to verify.
```

## Usage

### As a post-build step in your workflow

```yaml
- name: Verify image integrity
  run: ./verify-image-integrity.sh ${{ steps.build.outputs.imageid }} /app backend/src
```

### Arguments

| Arg | Description | Default |
|-----|-------------|---------|
| `image` | Image to verify (required) | — |
| `app-dir-in-image` | Path where COPY lands inside the image | `/app` |
| `source-dir` | Path to the source tree on disk | `.` |

## Reproducing the bug

The `repro.yml` workflow attempts to reproduce the stale cache issue:

1. Builds an image with GHA cache (primes the cache)
2. Modifies a source file
3. Rebuilds with GHA cache (cache may serve the old file)
4. Runs the integrity check
5. Rebuilds without cache (control — always matches)

Run it with: `gh workflow run repro.yml`

The bug is intermittent and may depend on the buildx version, cache backend, and platform configuration. The repro attempts to trigger it but may not always succeed.

## License

MIT
