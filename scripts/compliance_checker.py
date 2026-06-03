# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

import os
import sys
from pathlib import Path

def check_file(path, description):
    exists = Path(path).exists()
    status = "✅" if exists else "❌"
    print(f"{status} {description} ({path})")
    return exists

def check_dir(path, description):
    exists = Path(path).is_dir()
    status = "✅" if exists else "❌"
    print(f"{status} {description} ({path}/)")
    return exists

def run_compliance():
    print("🔍 Project Compliance Analysis\n")
    
    score = 0
    total_checks = 0
    
    print("📝 Metadata")
    # Simplistic check for description in README
    total_checks += 1
    if check_file("README.md", "Description (in README.md)"):
        score += 1
    
    # Check for Git Tags
    import subprocess
    try:
        tags = subprocess.check_output(["git", "tag"]).decode().strip()
        if tags:
            print("✅ Git Tags found")
            score += 1
        else:
            print("❌ Git Tags - No tags found in repository")
    except Exception:
        print("❌ Git Tags - Could not check tags")
    total_checks += 1
    
    print("\n📄 Documentation Files")
    docs = [
        ("README.md", "README.md"),
        ("CONTRIBUTING.md", "CONTRIBUTING.md"),
        ("USER_MANUAL.md", "USER_MANUAL.md"),
        ("AGENTS.md", "AGENTS.md")
    ]
    for path, desc in docs:
        total_checks += 1
        if check_file(path, desc):
            score += 1
            
    print("\n🗂 Repository Health Files")
    health_files = [
        (".gitignore", ".gitignore"),
        (".editorconfig", ".editorconfig"),
        ("CHANGELOG.md", "CHANGELOG.md"),
        ("SECURITY.md", "SECURITY.md"),
        ("CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.md"),
        (".env.example", ".env.example"),
        ("Dockerfile", "Dockerfile"),
        (".dockerignore", ".dockerignore"),
        ("LICENSE", "License (LICENSE)")
    ]
    for path, desc in health_files:
        total_checks += 1
        if check_file(path, desc):
            if path == "LICENSE":
                with open(path, 'r') as f:
                    content = f.read()
                    if "AFFERO GENERAL PUBLIC LICENSE" in content:
                        print("  ✅ License is AGPLv3")
                    else:
                        print("  ❌ License is NOT AGPLv3")
            score += 1

    print("\n🛠 Quality & Tools")
    tools = [
        ("pyproject.toml", "Ruff/Config"),
        ("requirements-dev.txt", "Dev dependencies")
    ]
    for path, desc in tools:
        total_checks += 1
        if check_file(path, desc):
            score += 1

    print("\n🤖 Automation & CI")
    automation = [
        (".gitlab-ci.yml", "GitLab CI Pipeline"),
        (".pre-commit-config.yaml", "Pre-commit Hooks"),
        ("cliff.toml", "Automated Changelog (Git-Cliff)")
    ]
    for path, desc in automation:
        total_checks += 1
        if check_file(path, desc):
            score += 1

    print("\n🛡️ Security & Audits")
    # Check if audit commands are present in CI or if audit reports exist
    audit_integrated = False
    if Path(".gitlab/ci/security.yml").exists():
        with open(".gitlab/ci/security.yml", 'r') as f:
            content = f.read()
            if "pip-audit" in content and "npm audit" in content:
                audit_integrated = True
    
    total_checks += 1
    if audit_integrated:
        print("✅ Dependency Audit (pip-audit/npm audit) integrated in CI")
        score += 1
    else:
        print("❌ Dependency Audit (pip-audit/npm audit) - Not found in CI")

    print("\n📐 Spec-Kit (Spec-Driven Development)")
    spec_kit = [
        (".specify", ".specify/ setup"),
        ("constitution.md", "constitution.md"),
        (".specify/templates", "Templates"),
        ("specs", "specs/ directory")
    ]
    for path, desc in spec_kit:
        total_checks += 1
        if Path(path).exists():
            score += 1
            print(f"✅ {desc}")
        else:
            print(f"❌ {desc}")

    final_score = int((score / total_checks) * 100)
    print(f"\n📊 Score Breakdown — {score}/{total_checks} checks passed ({final_score}%)")
    
    if final_score < 100:
        print("\n📌 Actionable Compliance Suggestions")
        if not Path(".editorconfig").exists():
            print("❌ Missing .editorconfig — Enforces consistent code style across editors")
        if not Path(".dockerignore").exists():
            print("❌ Missing .dockerignore — Keeps Docker images lean and safe")
        if not Path(".specify").exists():
            print("❌ Spec-Kit Setup — No .specify/ directory found.")
        if not Path("specs").exists():
            print("❌ Spec-Kit Feature Specs — No feature specs found.")
        if not Path("LICENSE").exists():
            print("❌ License — Project must be licensed under AGPLv3.")

if __name__ == "__main__":
    run_compliance()
