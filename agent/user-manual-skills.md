# Gemini CLI Skills Setup Guide

## Overview

This repository contains custom Gemini CLI skills designed to improve development workflows through specialized agents. Each skill is organized into its own directory and loaded automatically by Gemini CLI.

---

# Directory Structure

```text
~/.gemini/
└── skills/
    ├── frontend-engineer/
    │   └── SKILL.md
    ├── backend-engineer/
    │   └── SKILL.md
    ├── fullstack-engineer/
    │   └── SKILL.md
    ├── test-engineer/
    │   └── SKILL.md
    └── gitlab-reviewer/
        └── SKILL.md
```

---

# Prerequisites

Before creating skills ensure:

* Gemini CLI is installed
* Terminal access is available
* `~/.gemini/skills/` directory exists

Create skills directory if missing:

```bash
mkdir -p ~/.gemini/skills
```

---

# Creating a New Skill

## Step 1: Navigate to Skills Directory

```bash
cd ~/.gemini/skills
```

## Step 2: Create Skill Folder

Example:

```bash
mkdir gitlab-reviewer
cd gitlab-reviewer
```

## Step 3: Create Skill File

```bash
touch SKILL.md
```

## Step 4: Edit Skill

```bash
nano SKILL.md
```

Add your skill definition.

---

# Loading Skills

Start Gemini CLI:

```bash
gemini
```

Reload skills:

```text
/skills reload
```

List available skills:

```text
/skills list
```

Activate skill:

```text
/skill gitlab-reviewer
```

---

# Available Skills

## Frontend Engineer

Purpose:

* Build scalable user interfaces
* Improve accessibility
* Optimize performance

---

## Backend Engineer

Purpose:

* Develop APIs
* Improve security
* Build scalable services

---

## Fullstack Engineer

Purpose:

* Build end-to-end applications
* Connect frontend and backend systems

---

## Test Engineer

Purpose:

* Validate application quality
* Find bugs and edge cases

---

## GitLab Reviewer / CI Fixer

Purpose:

* Review repositories
* Analyze pipeline failures
* Fix GitLab CI/CD issues

---

# Best Practices

* Keep skills focused on one responsibility
* Use clear descriptions
* Prefer minimal instructions
* Reload skills after modifications
* Test skills before production usage

---

# Troubleshooting

### Skill Not Appearing

Run:

```text
/skills reload
```

Verify directory structure.

### Invalid Skill

Check:

* Folder name exists
* `SKILL.md` exists
* Markdown syntax is valid

---

# License

This project is intended for educational and development workflows.
