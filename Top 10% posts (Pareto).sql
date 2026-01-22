with ranked_post as (select engagement_rate, 
IIF(NTILE(10) over (order by engagement_rate desc) = 1, 'Top 10%', 'Bottom 90%') as post_group
from social_media_analytics_dataset_cleaned
)
Select
post_group,
round(avg(engagement_rate),3) as avg_engagement_rate
from ranked_post
group by post_group
order by avg_engagement_rate desc;