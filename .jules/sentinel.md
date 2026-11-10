# Sentinel's Journal

## 2026-11-10 - Prevent Credential and Secret Leakage via .gitignore
**Vulnerability:** Absence of rules ignoring local environment variables, private keys, certificates, and auth tokens in `.gitignore`, presenting a risk of accidental secret leaks in a public repository.
**Learning:** During pre-implementation and local research experiments, sensitive files (e.g., `.env`, private keys, certificates) could easily be staged accidentally by contributors if standard secret ignore rules are absent.
**Prevention:** Maintain strict repository-level ignore patterns for common secret extensions and environment configurations (`.env*`, `*.pem`, `*.key`, `*.token`, etc.).
