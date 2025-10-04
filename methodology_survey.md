# Methodology Report: Canadian AI Impact Vulnerability Index

**Report Version:** 1.0  
**Compilation Date:** October 4, 2025  
**Reference Period:** Q3 2025

## 1. Introduction

This report outlines the methodology for constructing the Canadian AI Impact Vulnerability Index (AIVI), a composite metric based on a national survey assessing perceived risk and impact of AI on the Canadian workforce. The AIVI incorporates demographic, professional, and educational data to profile AI vulnerability across population segments. Results are visualized using a multi-axis polygon (radar) chart for comparative analysis.

## 2. Data Collection: Canadian AI Sentiment Survey (CAISS)

Primary data was collected via the Canadian AI Sentiment Survey (CAISS), designed to measure public and professional sentiment regarding AI-driven economic change.

- **Survey Period:** July 15, 2025 – September 30, 2025  
- **Sampling Method:** Stratified random sampling by province, industry sector, and age cohort  
- **Sample Size:** n = 2,412 completed responses

**Data Collected:**
- Province of residence
- Primary industry of employment
- Highest educational attainment
- Gender identity
- Racial identity

## 3. Analytical Framework: AI Vulnerability Index (AIVI)

AIVI quantifies individual vulnerability to AI-related workforce disruption. It is a weighted composite of three factors: Industry Risk, Educational Resilience, and Provincial Economic Modifier.

### 3.1 Component Factor Mapping

Survey responses were mapped to quantitative scores:

**Industry Risk Score (IRS):**  
Risk of automation by industry (0.1 = low risk, 1.0 = high risk):

| Industry            | IRS  |
|---------------------|------|
| Public Admin.       | 0.2  |
| Prof. & Tech.       | 0.3  |
| Healthcare          | 0.4  |
| Finance & Ins.      | 0.5  |
| Agriculture         | 0.6  |
| Natural Resources   | 0.7  |
| Manufacturing       | 0.8  |
| Transportation      | 0.85 |
| Retail              | 0.9  |

**Educational Resilience Score (ERS):**  
Resilience by education level (0.1 = low, 1.0 = high):

| Education Level      | ERS  |
|----------------------|------|
| < High School        | 0.1  |
| High School          | 0.3  |
| College/Trade        | 0.5  |
| Bachelor's           | 0.7  |
| Master's             | 0.9  |
| Doctorate/Prof.      | 1.0  |

**Provincial Economic Factor (PEF):**  
Modifier by province:

| Province           | PEF  |
|--------------------|------|
| Ontario            | 0.3  |
| British Columbia   | 0.4  |
| Quebec             | 0.5  |
| Alberta            | 0.6  |
| Manitoba           | 0.6  |
| Saskatchewan       | 0.7  |

### 3.2 AIVI Calculation Formula

AIVI is calculated as:

```
AIVI = (IRS × 0.60) + ((1 - ERS) × 0.35) + (PEF × 0.05)
```

- **IRS:** Weighted at 60%
- **(1 - ERS):** Inverted resilience, weighted at 35%
- **PEF:** Regional adjustment, weighted at 5%

## 4. Data Visualization: Multi-Axis Polygon Graph

A radar chart (via Flourish) visualizes AIVI dimensions for demographic cohorts.

### 4.1 Chart Structure

- **Axes:**  
 - Industry Risk (IRS)  
 - Educational Vulnerability (1 - ERS)  
 - Overall AIVI Score  
 - Perceived AI Risk (self-reported)  
 - Perceived AI Benefit (self-reported)

- **Polygons:**  
 Each polygon represents an aggregated group (e.g., "Manufacturing workers in Ontario with College Diplomas"), with vertices showing average scores per axis. The shape highlights the group's vulnerability profile.

## 5. Data Integrity and Limitations

- **Anonymization:** All PII removed; analysis on anonymized data.
- **Weighting Subjectivity:** Formula weights are expert-assessed and open to interpretation.
- **Survey Bias:** Potential for non-response or self-selection bias.
- **Static Analysis:** Snapshot for Q3 2025; does not reflect ongoing AI evolution.
