# Data Dictionary

## fund_master

| Column | Data Type | Description |
|----------|----------|----------|
| scheme_code | INTEGER | AMFI Scheme Code |
| scheme_name | TEXT | Mutual Fund Name |
| fund_house | TEXT | Fund House |
| scheme_type | TEXT | Scheme Type |
| scheme_category | TEXT | Scheme Category |

## nav_history

| Column | Data Type | Description |
|----------|----------|----------|
| date | DATE | NAV Date |
| nav | FLOAT | Net Asset Value |

## fact_nav

| Column | Data Type | Description |
|----------|----------|----------|
| nav_id | INTEGER | Primary Key |
| fund_id | INTEGER | Fund Identifier |
| date_id | INTEGER | Date Identifier |
| nav | FLOAT | Net Asset Value |