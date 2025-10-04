# Methodology Report: Analysis of AI Readiness in the Canadian Job Market

**Report Version:** 1.0  
**Compilation Date:** 2025-10-01

## 1. Introduction

This report outlines the methodology used to assess AI readiness in the Canadian job market. The analysis synthesizes data from national sources to create a dataset mapping occupations to industries, enriched with metrics on income, employment, and AI preparedness. The dataset supports network visualization to illustrate relationships within Canada's labour landscape.

## 2. Data Sourcing and Aggregation

Data was aggregated from authoritative Canadian sources (retrieved October 1, 2025):

### 2.1 Primary Data Sources

- **Statistics Canada – Labour Force Survey (2023-2024):**
   - Table 14-10-0416-01: Labour force characteristics by occupation
   - Table 14-10-0417-01: Employee wages by occupation
   - Table 14-10-0064-01: Employee wages by industry
- **Job Bank Canada – Wage Data (2024):**
   - 2024 Open Data Wage File (NOC-based occupation wages by region)
- **AI Exposure and Adoption Studies (2024-2025):**
   - Statistics Canada AI Occupational Exposure Index (2024)
   - IBM Canada AI Adoption Survey (2024)
   - Microsoft/Accenture Generative AI Study (2024)
   - IRPP Labour Market AI Impact Analysis (2025)
- **Canadian Survey on Business Conditions (Q2 2025):**
   - Industry-specific AI adoption data (Statistics Canada Analysis 11-621-m2025008)

## 3. Data Pre-processing and Standardization

- **Occupation Standardization:** All data mapped to NOC 2021 (5-digit codes). Occupations with <100 national employment excluded.
- **Industry Mapping:** Industries classified by NAICS 2-digit codes; occupation-to-industry links based on employment distribution.
- **Missing Data Imputation:** Provincial averages used for missing wage data; industry-level averages for missing AI metrics. Imputed data flagged.
- **Outlier Treatment:** Wages capped at 99th percentile; AI readiness components normalized to 0–1 scale.

## 4. Analytical Framework

### 4.1 AI Readiness Index Construction

A composite AI Readiness Score (0–1 scale) is calculated as a weighted average of four normalized components:

- **Automation Risk (30%)**: Complementarity-adjusted AI occupational exposure (C-AIOE), inverted so lower risk = higher readiness.
- **Digital Skill Share (35%)**: Proportion of job tasks requiring digital skills (O*NET task analysis mapped to NOC).
- **Vacancy AI-Skill Growth (20%)**: Year-over-year growth in AI-related job postings (Job Bank data).
- **Industry Digital Adoption (15%)**: Industry-level AI adoption rates (Canadian Survey on Business Conditions).

**Formula:**  
`AI_Readiness = (0.30 × (1 - Automation_Risk)) + (0.35 × Digital_Skill_Share) + (0.20 × Vacancy_AI_Growth) + (0.15 × Industry_Adoption)`

### 4.2 Income Level Classification

Based on 2023 national income distribution (T1 Family File preliminary data):

- **Low Income:** ≤ 25th percentile (≤ $35,000)
- **Medium Income:** 26th–74th percentile ($35,001–$75,000)
- **High Income:** ≥ 75th percentile (> $75,000)

## 5. Network Visualization with Flourish

The dataset is structured for network graph visualization using Flourish.

### 5.1 Points Table (Nodes)

- **Structure:** Unique ID, label (occupation/industry), attributes for visual encoding.
- **Application:** Node size = employment count; node color = AI Readiness Score.

### 5.2 Links Table (Edges)

- **Structure:** Source/target columns (unique IDs from Points Table).
- **Application:** Links connect occupations to industries; thickness = number of workers in occupation-industry pairing.

## 6. Data Validation and Integrity

- Wage data cross-referenced between Job Bank and Statistics Canada.
- AI adoption rates compared across independent surveys.
- Occupation/industry distributions validated against census and business registries.

## 7. Summary of Analytical Findings

- **High-Readiness Industries:** Information & Cultural Industries (0.78), Professional, Scientific & Technical Services (0.75), Finance & Insurance (0.72).
- **Low-Readiness Industries:** Accommodation & Food Services (0.28), Agriculture/Forestry/Fishing (0.31), Transportation & Warehousing (0.35).
- **Employment Impact:** 31% of workers in high-exposure, low-complementarity roles; 89.4% of businesses report no net employment change post-AI adoption.

## 8. Limitations and Considerations

- Metrics reflect current technology and may change.
- Wage data may lag market conditions.
- Rural/urban differences not fully captured.
- Self-employed individuals excluded.

## 9. Maintenance and Update Protocol

- **Annually (December):** Wage data refresh
- **Quarterly:** Employment count updates
- **Semi-Annually:** AI metric recalibration
- **Annually (Q1):** Full dataset and report update

## 10. Contact and Support

For methodology or data inquiries:

- **Statistics Canada:** infostats@statcan.gc.ca
- **Job Bank Canada:** NC-LMI-IMT-GD@hrsdc-rhdcc.gc.ca
