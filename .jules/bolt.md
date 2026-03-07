## 2024-03-07 - [Eliminate N+1 query in cxp campaign list]
**Learning:** Found an N+1 query pattern in `cxp` CLI where `list_results` was called for each campaign in a loop to get the result counts. This would become a major performance bottleneck for large datasets in SQLite.
**Action:** Implemented a new function `get_campaign_result_counts` that executes a single `GROUP BY` query to fetch result counts for all campaigns at once, then retrieved the counts from the dictionary inside the loop. This reduces database overhead significantly and maintains performance as history grows.
