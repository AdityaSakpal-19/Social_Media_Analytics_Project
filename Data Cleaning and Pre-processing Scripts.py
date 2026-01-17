# %%
pip install pandas numpy matplotlib seaborn scikit-learn

# %%
import pandas as pd;
df = pd.read_csv(r'C:/Users/Aditya Sakpal/OneDrive/Documents/Social Media Analytics Project/Social_Media_Analytics_Project/social_media_analytics_dataset.csv');
print(df.head());

# %%
#Checking null values in the dataset
print(df.isnull().sum());

# %%
#checking duplicate values in the dataset
print(df.duplicated().sum());

# %%
#Sanity check of the dataset
df.info()

# %%
#Sanity check of the dataset
df.describe()

# %%
#converting post_date to datetime format
df['post_date'] = pd.to_datetime(df['post_date'], format='mixed', dayfirst=True);

# %%
#checking the info after conversion
df.info()

# %%
''' CREATE DERIVED METRICS (CORE KPIs)'''
#A Enagements
df['engagement'] = df['likes'] + df['comments'] + df['shares'];

# %%
#B Engagement Rate
df['engagement_rate'] = (df['engagement'] / df['impressions']) * 100;

# %%
#C Individual Rates
df['like_rate'] = df['likes'] / df['impressions']
df['comment_rate'] = df['comments'] / df['impressions']
df['share_rate'] = df['shares'] / df['impressions']
df['save_rate'] = df['saves'] / df['impressions']

# %%
#QUICK KPI VALIDATION
df[['engagement_rate', 'like_rate', 'comment_rate', 'share_rate', 'save_rate']].describe()

# %%
#Platform Level Performance
platform_summary = (
    df.groupby('platform')
      .agg(
          posts=('post_id', 'count'),
          avg_impressions=('impressions', 'mean'),
          avg_engagement_rate=('engagement_rate', 'mean')
      )
      .reset_index()
)

platform_summary


# %%
#Content Type Performance
content_summary = (
    df.groupby('content_type')
      .agg(
          posts=('post_id', 'count'),
          avg_engagement_rate=('engagement_rate', 'mean'),
          avg_saves=('saves', 'mean')
      )
      .reset_index()
)

content_summary.sort_values('avg_engagement_rate', ascending=False)

# %%
#Time Based Trend
df['month'] = df['post_date'].dt.to_period('M')
monthly_trends = (
    df.groupby('month')
      .agg(
          total_posts=('post_id', 'count'),
          avg_engagement_rate=('engagement_rate', 'mean')
      )
      .reset_index()
)
monthly_trends

# %%
df.to_csv('social_media_analytics_dataset_cleaned.csv', index=False);


