import pandas as pd
from datetime import datetime

# Step 1: Load the data
df = pd.read_csv('device_usage_log.csv', parse_dates=['timestamp'])

# Step 2: Extract hour from timestamp
df['date'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour




# Step 3: Group by hour and sum power consumption
hourly_usage = df.groupby(['date', 'hour'])['power_consumption'].sum().reset_index()

# Step 4: Identify peak hour
for date in df['date']:
    daily_usage=hourly_usage[hourly_usage['date']==date]
    peak_row = daily_usage.loc[daily_usage['power_consumption'].idxmax()]
    peak_hour = int(peak_row['hour'])
    peak_value = peak_row['power_consumption']

    # Step 5: Output the result
    print(f"✅ for Date:{date} Peak Hour: {peak_hour}:00")
    print(f"⚡ Total Power Consumed: {peak_value} kWh")

# Optional: show hourly usage
print("\n📊 Hourly Usage Breakdown:")
print(hourly_usage)
