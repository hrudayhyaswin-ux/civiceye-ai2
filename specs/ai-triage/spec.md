# Feature Spec: AI-Powered Civic Complaint Triage

## Status
Implemented Successfully

## Problem
Citizens report diverse issues that require manual sorting, leading to delays in response time and inconsistent prioritization.

## Goals
- Automate complaint categorization.
- Identify urgent infrastructure or safety issues automatically.
- Detect potential duplicate reports in the same location.

## User Stories
- As a Citizen, I want my voice note to be transcribed and analyzed so I don't have to fill out long forms.
- As an Admin, I want issues to be pre-sorted by department so I can focus on resolution.

## Functional Requirements
- Transcribe audio files using STT providers.
- Classify complaints into categories (e.g., Waste, Roads, Water).
- Extract location landmarks and entities.
- Assign a priority level (Critical, High, Medium, Low).

## Data and Privacy
- PII is extracted for contact purposes but protected in storage.
- Audio files are stored securely in `/uploads`.

## AI Behavior
- Inputs: Description text or Voice Note.
- Outputs: JSON with category, department, priority, and summary.
- Failure modes: Defaults to "Other" category and "Low" priority if analysis fails.

## Acceptance Criteria
- AI classifies a "pothole" report into the "Roads" category with High priority.
- AI detects location landmarks from the description.
