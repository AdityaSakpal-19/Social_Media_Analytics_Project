select month, count(*) as total_posts, round(avg(engagement_rate),3) as avg_engagement_rate from social_media_analytics_dataset_cleaned
group by month
order by month;