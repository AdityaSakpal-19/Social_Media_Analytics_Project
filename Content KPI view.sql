CREATE VIEW vw_content_performance AS
SELECT
    content_type,
    COUNT(*) AS total_posts,
    AVG(engagement_rate) AS avg_engagement_rate,
    AVG(saves) AS avg_saves
FROM social_media_analytics_dataset_cleaned
GROUP BY content_type;
