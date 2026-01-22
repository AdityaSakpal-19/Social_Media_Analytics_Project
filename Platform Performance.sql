select platform, count(*), AVG(impressions) as avg_impressions, avg(engagement_rate) as avg_enagement_rate from social_media_analytics_dataset_cleaned
group by platform
order by avg_enagement_rate DESC;