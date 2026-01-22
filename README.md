# 📊 Social Media Performance & Content Analytics

## Overview

This project analyzes social media performance across **Instagram, LinkedIn, and Twitter** to improve **content strategy, engagement efficiency, and platform optimization** using an end-to-end analytics workflow with **Python, SQL Server, and Power BI**.

---

## Business Problem

Marketing teams often track likes and impressions, but lack visibility into:

- Which content formats perform best by platform  
- How quickly engagement decays after posting  
- Whether performance depends too heavily on a few top posts  

This project addresses these gaps using **performance, efficiency, and risk-based analytics**.

---

## What Was Built

- Built a full analytics pipeline for **post-level performance analysis**  
- Engineered advanced KPIs including:
  - Engagements per 1,000 Impressions  
  - Weighted Engagement Score  
  - Engagement Decay Percentage  
  - Top-Post Dependency Ratio  
- Designed an interactive **Power BI dashboard** with:
  - Platform performance overview  
  - Content longevity & decay analysis  
  - Platform–content fit heatmap  
  - Concentration risk view  

---

## Impact & Key Outcomes

- Identified **best platform–content combinations** to guide content allocation  
- Quantified **~20% engagement decay** after the initial posting window to support reposting strategy  
- Highlighted **high-performing content formats** driving quality engagement  
- Measured **moderate dependence on top 10% posts**, supporting performance diversification planning  

These insights directly support **content optimization, platform strategy, and growth planning**.

---

## Dataset

The dataset contains post-level social media data across:

- Instagram  
- LinkedIn  
- Twitter  

Key fields include:

- Post date  
- Platform  
- Content type  
- Impressions and reach  
- Likes, comments, shares, saves  
- Derived engagement and efficiency metrics  

---

## Key KPIs

- Total Impressions  
- Total Engagements  
- Average Engagement Rate  
- Engagements per 1,000 Impressions  
- Weighted Engagement Score  
- Engagement Decay Percentage  
- Top-Post Dependency Ratio  

---

## Methodology

### Data Preparation (Python)

- Cleaned missing and duplicate records  
- Standardized date and categorical fields  
- Engineered engagement and efficiency metrics  
- Created time-based features for decay analysis  

### Analytical Modeling (SQL Server)

- Built analytical views for:
  - Platform performance  
  - Content performance  
  - Efficiency analysis  
  - Top-post dependency segmentation  
- Performed aggregations and NTILE-based segmentation  

### Visualization (Power BI)

Built an interactive multi-page dashboard including:

- Executive performance overview  
- Engagement efficiency analysis  
- Content longevity & decay  
- Platform–content fit heatmap  
- Dependency & concentration risk view  

---

## Tools & Technologies

- **Python** – Data cleaning and feature engineering  
- **SQL Server** – KPI modeling and analytical queries  
- **Power BI** – Interactive dashboards and executive reporting  

Libraries and tools used:

- pandas  
- numpy  
- SQL Server Management Studio  
- Power BI Desktop 
