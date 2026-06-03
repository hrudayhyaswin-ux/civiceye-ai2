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
    # Ensure we are running from the project root (where this script's parent's parent is)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    os.chdir(project_root)

    print("🔍 Project Compliance Analysis\n")
    
    score = 0
    total_checks = 0
    
    print("metadata")
    # Simplistic check for description in README
    total_checks += 1
    if check_file("README.md", "Description (in README.md)"):
        score += 1
    
    # Check for Git Tags
    import subprocess
    try:
        tags = subprocess.check_output(["git", "tag"]).decode().strip()
        if tags:
            print("✅ Git Tags")
            score += 1
        else:
            print("❌ Git Tags")
            print("How to fix: git tag v1.0.0")
    except Exception:
        print("❌ Git Tags - Could not check tags")
    total_checks += 1
    
    print("\ndocumentation")
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
            
    print("\nrepository health")
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

    print("\nquality & tools")
    tools = [
        ("pyproject.toml", "Ruff/Config"),
        ("pyproject.toml", "Pytest/Config"),
        ("requirements-dev.txt", "Dev dependencies")
    ]
    for path, desc in tools:
        total_checks += 1
        if check_file(path, desc):
            if desc == "Pytest/Config":
                with open(path, 'r') as f:
                    if "pytest" in f.read().lower():
                        score += 1
                    else:
                        print(f"  ❌ {desc} not found in {path}")
            elif desc == "Ruff/Config":
                with open(path, 'r') as f:
                    if "ruff" in f.read().lower():
                        score += 1
                    else:
                        print(f"  ❌ {desc} not found in {path}")
            else:
                score += 1

    print("\nautomation & CI")
    automation = [
        (".gitlab-ci.yml", "GitLab CI Pipeline"),
        (".pre-commit-config.yaml", "Pre-commit Hooks"),
        ("cliff.toml", "Automated Changelog (Git-Cliff)")
    ]
    for path, desc in automation:
        total_checks += 1
        if check_file(path, desc):
            score += 1
    
    # Check for Ruff in CI (Lint Tool)
    ruff_integrated = False
    ci_files = [".gitlab-ci.yml", ".gitlab/ci/lint.yml"]
    for ci_file in ci_files:
        if Path(ci_file).exists():
            with open(ci_file, 'r') as f:
                content = f.read().lower()
                if "ruff" in content:
                    ruff_integrated = True
                    break
    
    total_checks += 1
    if ruff_integrated:
        print("✅ CI Pipeline — Add Ruff for linting")
        score += 1
    else:
        print("❌ CI Pipeline — Add Ruff for linting")
        print("How to fix: uv add --dev ruff && ruff check .")

    print("\ntest")
    # Check for Test Job in CI
    test_job_present = False
    ci_test_files = [".gitlab-ci.yml", ".gitlab/ci/test.yml"]
    for ci_file in ci_test_files:
        if Path(ci_file).exists():
            with open(ci_file, 'r') as f:
                content = f.read().lower()
                if "stage: test" in content or "python:test" in content:
                    test_job_present = True
                    break
    
    total_checks += 1
    if test_job_present:
        print("Job: ✅")
        score += 1
    else:
        print("Job: ❌")

    # Check for Test Tool (Pytest)
    pytest_config_found = False
    if Path("pyproject.toml").exists():
        with open("pyproject.toml", 'r') as f:
            if "pytest" in f.read().lower():
                pytest_config_found = True
    
    total_checks += 1
    if pytest_config_found:
        print("Tool: ✅")
        score += 1
    else:
        print("Tool: ❌")

    print("\nlint")
    # Check for Lint Job in CI
    lint_job_present = False
    for ci_file in ci_files:
        if Path(ci_file).exists():
            with open(ci_file, 'r') as f:
                content = f.read().lower()
                if "stage: lint" in content or "python:lint" in content:
                    lint_job_present = True
                    break
    
    total_checks += 1
    if lint_job_present:
        print("Job: ✅")
        score += 1
    else:
        print("Job: ❌")

    total_checks += 1
    if ruff_integrated:
        print("Tool: ✅")
        score += 1
    else:
        print("Tool: ❌")

    print("\nsecurity & audits")
    # Check if audit commands are present in CI or if audit reports exist
    audit_integrated = False
    if Path(".gitlab/ci/security.yml").exists():
        with open(".gitlab/ci/security.yml", 'r') as f:
            content = f.read()
            if "pip-audit" in content and "npm audit" in content and "uv audit" in content:
                audit_integrated = True
    
    total_checks += 1
    if audit_integrated:
        print("✅ Dependency Audit (uv/pip-audit/npm audit) integrated in CI")
        score += 1
    else:
        print("❌ Dependency Audit (uv/pip-audit/npm audit) - Not found in CI")

    print("\nspec-kit (SDD)")
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
        
        # Check if tags were missing in the score check
        try:
            tags = subprocess.check_output(["git", "tag"]).decode().strip()
            if not tags:
                print("❌ Git Tags — Every project must have at least one version tag (e.g., v1.0.0)")
        except:
            pass
            
        sys.exit(1)
    else:
        print("\n🎊 Project is fully compliant!")
        sys.exit(0)

if __name__ == "__main__":
    run_compliance()
