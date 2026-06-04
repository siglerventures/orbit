# Orbit — working agreement

## Branch & PR workflow (STRICT — do not violate)

A PR number, once given to the user, is treated as **immediately merged/pulled**.
Therefore:

1. **One change = one fresh branch = one new PR.** Never reuse a branch whose PR
   has already been handed to the user.
2. **Never push new commits to a branch after its PR number has been shared.**
   That PR is done. Start over.
3. For every new piece of work: cut a **brand-new branch off the latest `origin/main`**
   (`git fetch origin main` first), commit there, push, and open a **new PR**.
4. **Never reuse a PR number.** Each deliverable gets its own number.
5. Bump `<meta name="app-rev">` in `index.html` once per change (single source of truth
   for the cache-bust version).

If unsure whether a branch/PR is still "open" for more commits: assume it is NOT.
Make a new branch.

## App facts
- Single-file app: `index.html`. Version lives in `<meta name="app-rev">`.
- Satellite data snapshots live in `data/*.txt` (TLE) + `data/stars.json`, refreshed
  by the `update-tle.yml` GitHub Action (daily + manual dispatch).
- The bulk satellite cloud is one `THREE.Points`; `SAT_GROUPS` defines each
  constellation's color/size. Starlink (~10.5k) dominates by count.
