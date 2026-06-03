# CivicEye AI Constitution

## Principles

1. Public-interest outcomes first: features should improve complaint reporting, routing, transparency, or civic response quality.
2. Privacy by default: collect the minimum useful data, protect personally identifiable information, and avoid exposing secrets in code, logs, screenshots, or fixtures.
3. Explainable automation: AI-assisted triage should provide human-readable classifications, priorities, and summaries that can be reviewed.
4. Accessibility and language inclusion: citizen-facing workflows should remain usable across devices, bandwidth levels, and supported languages.
5. Tested change: meaningful product or safety changes should include tests, specs, or documented verification.

## Engineering Standards

- New features start from a short specification under `specs/`.
- Backend changes should pass pytest, coverage, flake8, pylint, bandit, and dependency audit checks.
- Frontend changes should build successfully for both Vite applications.
- Security-sensitive changes should include explicit notes about secrets, authentication, authorization, and data retention.
- Releases should be tagged with `vMAJOR.MINOR.PATCH` and summarized in `CHANGELOG.md`.

## Governance

This constitution is the baseline for project decisions. Amendments should be proposed as pull requests with rationale, impact, and migration notes when needed.


