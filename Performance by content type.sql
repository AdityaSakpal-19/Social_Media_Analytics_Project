select content_type, count(*), round(avg(engagement_rate), 3) as avg_engagement_rate, avg(likes) as avg_likes, avg(comments) as avg_comments,
avg(saves) as avg_saves, avg(shares) as avg_shares
from social_media_analytics_dataset_cleaned
group by content_type
order by avg_engagement_rate Desc;