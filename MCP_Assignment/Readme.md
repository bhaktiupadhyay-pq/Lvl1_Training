# Bug Trend Analysis Using Atlassian MCP

## Overview

This project demonstrates how to use the Atlassian Remote MCP (Model Context Protocol) integration with Claude Desktop to retrieve, analyze, and categorize Jira bug data.

The assignment focuses on:

* Connecting Claude Desktop with Atlassian MCP
* Retrieving Jira bug issues
* Performing bug trend analysis
* Categorizing root causes of missed defects
* Generating actionable recommendations

---

# Technologies Used

* Claude Desktop
* Atlassian Remote MCP Server
* Jira Cloud
* Node.js
* MCP (Model Context Protocol)

---

# Project Structure

```text
.
├── README.md
├── screenshots/
│   ├── jira-projects.png
│   ├── bug-analysis.png
│   └── root-cause-analysis.png
└── reports/
    └── final-analysis-report.md
```

---

# Step 1: Install Prerequisites

## Install Node.js

Download and install Node.js:

[https://nodejs.org/](https://nodejs.org/)

Verify installation:

```bash
node -v
npm -v
```

---

# Step 2: Install Claude Desktop

Download Claude Desktop:

[https://claude.ai/download](https://claude.ai/download)

Login with your Claude account.

---

# Step 3: Create Atlassian API Token

Generate API token:

[https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)

Save:

* Atlassian Email
* API Token
* Jira Base URL

Example:

```text
https://productsquads-l1.atlassian.net
```

---

# Step 4: Configure Claude Desktop MCP

## Open Claude Config Folder

### Windows

```text
%APPDATA%\Claude
```

### macOS

```text
~/Library/Application Support/Claude
```

---

# Atlassian MCP Configuration Code

Use the following configuration inside:

```text
claude_desktop_config.json
```

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": [
        "-y",
        "@atlassian/remote-mcp"
      ],
       "env": {
        "ATLASSIAN_BASE_URL": "https://productsquads-l1.atlassian.net",
        "ATLASSIAN_EMAIL": "bhakti.upadhyay@productsquads.co",
        "ATLASSIAN_API_TOKEN": "ATATT3xFfGF0MgeTpJTUwq_9F9MFmsyqS0dyEmcyQpQ_7lWiQ_3rmWdKJeujPa2kXzAAD3qghDnfyw-ZAeldh59YvQdGti_RzuAJIyLHZzlhAyTQXVm4RE7PwOSidljf3Ujc0QTxN3MtmSwrH_Y1Ygl8lahetaP5rHRhEGZULAxjN8cZv6R5VfQ=B7FCC1B2"
      }
    }
  }
}
```

---

# Step 5: Create Config File

Create:

```text
claude_desktop_config.json
```

Add the following configuration:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": [
        "-y",
        "@atlassian/remote-mcp"
      ],
      "env": {
        "ATLASSIAN_BASE_URL": "https://productsquads-l1.atlassian.net",
        "ATLASSIAN_EMAIL": "your-email@example.com",
        "ATLASSIAN_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

Restart Claude Desktop after saving the file.

---

# Step 6: Verify MCP Connection

Prompt used:

```text
Show available Jira projects
```

## Output

The MCP connection successfully retrieved Jira projects.

### Screenshot

Add your screenshot here:

```markdown
![Jira Projects](screenshots/jira-projects.png)
```

---

# Step 7: Retrieve Bug Data

Prompt used:

```text
Retrieve all Bug issues from project KAN from the last 6 months.

Include:
- issue key
- summary
- status
- priority
- created date
- resolved date
- assignee
- reporter
- labels
- components
```

---

# Step 8: Analyze Bug Trends

Prompt used:

```text
Analyze bug trends in project KAN over the last 6 months.
```

## Analysis Goals

* Bug frequency over time
* Severity distribution
* Module-wise defects
* Resolution trends

### Screenshot

```markdown
![Bug Trend Analysis](screenshots/bug-analysis.png)
```

---

# Step 9: Root Cause Categorization

Prompt used:

```text
Review all bug issues in project KAN and categorize root causes into:

- Requirement Gaps
- Design or Architecture Issues
- Coding Defects
- Testing Gaps
- Process or Tooling Issues
- Human Factors
```

## Root Cause Categories

| Category         | Description                         |
| ---------------- | ----------------------------------- |
| Requirement Gaps | Missing or unclear requirements     |
| Design Issues    | Poor architecture or design flaws   |
| Coding Defects   | Logic or implementation errors      |
| Testing Gaps     | Missing test cases or weak coverage |
| Process Issues   | Workflow or tooling inefficiencies  |
| Human Factors    | Communication gaps or oversight     |

### Screenshot

```markdown
![Root Cause Analysis](screenshots/root-cause-analysis.png)
```

---

# Step 10: Findings

## Key Observations

* Several bugs were detected during QA and staging phases.
* High severity defects were concentrated in core modules.
* Some defects escaped development due to insufficient testing coverage.
* Delayed resolution times indicated process bottlenecks.

---

# Recommendations

## Improve Requirement Validation

* Conduct requirement review meetings
* Improve acceptance criteria documentation

## Strengthen Testing

* Increase regression automation
* Add edge-case test coverage
* Perform integration testing earlier

## Improve Code Quality

* Strengthen peer code reviews
* Use static analysis tools

## Enhance Process Automation

* Improve CI/CD validation checks
* Add release readiness gates

---

# Conclusion

This assignment demonstrated how Atlassian MCP can be integrated with Claude Desktop to analyze Jira defects efficiently.

Using MCP-enabled workflows made it easier to:

* Retrieve Jira data
* Analyze defect trends
* Categorize root causes
* Generate actionable quality insights

The project also highlighted how AI-assisted analysis can support software quality improvement initiatives.

---

# Final Deliverables

* MCP Configuration
* Jira Bug Analysis
* Trend Analysis
* Root Cause Categorization
* Recommendations
* Screenshots
* README Documentation

---

# Author

Bhakti
