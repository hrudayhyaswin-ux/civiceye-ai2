Contributing to CivicEye
First off, thank you for considering contributing to CivicEye 🎉
CivicEye aims to improve civic issue reporting and resolution through AI-powered workflows, and contributions from the community help make the platform better, more reliable, and more impactful.


Table of Contents

Getting Started
Project Setup
How to Contribute
Development Guidelines
Commit Guidelines
Reporting Issues
Pull Request Process
Code of Conduct



Getting Started
Before contributing, ensure you have:

Git installed
Python 3.10+ installed
Node.js and npm installed
Basic understanding of the project architecture



Project Setup

1. Fork and Clone Repository

git clone https://github.com/yourusername/civiceye.git
cd civiceye



2. Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate



macOS / Linux

python3 -m venv venv
source venv/bin/activate



3. Install Backend Dependencies

pip install -r requirements.txt



4. Install Frontend Dependencies

cd frontend
npm install



5. Run Development Environment
Backend:

python app.py


Frontend:

npm run dev




How to Contribute


Fork the repository


Create a new branch



git checkout -b feature/your-feature-name




Make your changes


Commit your changes



git commit -m "Add: meaningful description"



Push changes


git push origin feature/your-feature-name



Open a Pull Request



Development Guidelines

Code Quality

Follow PEP 8 for Python code
Write clean, modular code
Maintain consistent naming conventions
Keep functions small and reusable
Add comments where necessary


Frontend Guidelines

Keep components reusable
Follow existing folder structure
Use Tailwind utility classes consistently


Backend Guidelines

Keep APIs RESTful
Validate all inputs
Handle errors properly
Write reusable services


AI Guidelines

Maintain structured outputs
Document prompt changes
Ensure fallback mechanisms work correctly



Commit Guidelines
Use clear commit messages.
Examples:

feat: add complaint classification endpoint

fix: resolve duplicate complaint detection bug

docs: update setup instructions


Avoid:

update stuff

changes

fixed issue




Reporting Issues
When creating issues:

Provide clear descriptions
Include reproduction steps
Mention expected behavior
Mention actual behavior
Add screenshots/logs when helpful



Pull Request Process
Before submitting:

Ensure code builds successfully
Test your changes
Update documentation if required
Resolve merge conflicts

Pull Requests should include:

Description of changes
Screenshots (if UI changes)
Testing details



Security Guidelines
Please do not commit:

API keys
Secrets
Environment files
Credentials

Use:

.env
.env.local
.env.production


inside .gitignore


Code of Conduct
Please maintain a respectful environment.

Be professional
Be constructive
Respect differing opinions
Avoid harassment or abusive behavior


Thank you for contributing to CivicEye 🚀
