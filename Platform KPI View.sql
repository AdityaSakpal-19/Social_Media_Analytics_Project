CREATE VIEW vw_platform_performance AS
SELECT
    platform,
    COUNT(*) AS total_posts,
    AVG(impressions) AS avg_impressions,
    AVG(engagement_rate) AS avg_engagement_rate
FROM social_media_analytics_dataset_cleaned
GROUP BY platform;