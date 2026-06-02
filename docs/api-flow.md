## Complaint Management API Flow

### 1. Create Complaint (Citizen)

**Endpoint:**
`POST /api/complaints`

**Process:**

* Citizen submits complaint details
* Backend validates incoming data
* Complaint is stored in the database
* Backend sends complaint data to AI services for analysis via:

`POST /ai/classify` *(along with related AI processing steps)*

**AI Response Includes:**

* Complaint category

* Extracted entities

* Priority score / priority label

* Potential duplicate complaints *(optional)*

* Backend updates the complaint record with AI-generated insights

---

### 2. Track Complaint Status

**Endpoint:**
`GET /api/complaints/:id`

**Purpose:**

* Retrieve complaint details
* Track complaint progress and current status

---

### 3. Admin Operations

#### Get All Complaints

**Endpoint:**
`GET /api/admin/complaints`

**Purpose:**

* Retrieve all complaints for review and management

#### Update Complaint Status

**Endpoint:**
`PATCH /api/admin/complaints/:id/status`

**Purpose:**

* Modify complaint status
* Update workflow progress (Open, In Progress, Resolved, etc.)

