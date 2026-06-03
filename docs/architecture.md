# System Architecture

## High-Level Components

### Citizen Application

Responsible for collecting complaint information from users, including:

* Complaint description (text input)
* Optional voice recordings
* Location information
* Images or supporting media uploads

### Admin Dashboard

Provides management and monitoring capabilities:

* Review and triage complaints
* Update complaint status and workflow stages
* Generate analytics and export reports

### Backend API

Handles core application logic and services:

* Authentication and authorization
* Complaint workflow management
* Data persistence and storage
* Communication between services

### AI Service

Processes complaints to provide intelligent insights:

* Complaint classification
* Entity extraction
* Priority prediction
* Duplicate complaint detection

---

# Typical Workflow

### Step 1: Complaint Submission

Citizen submits complaint details through the application.

### Step 2: Data Storage

Backend validates and stores complaint data along with uploaded media metadata.

### Step 3: AI Processing

Backend sends complaint data to AI services for enrichment and analysis.

### Step 4: Complaint Enhancement

AI returns:

* Category classification
* Extracted entities
* Priority score / label
* Duplicate detection results

### Step 5: Persistence

Backend stores enriched complaint information and updates priority details.

### Step 6: Tracking & Resolution

Citizens and administrators track complaint status throughout the resolution lifecycle.

