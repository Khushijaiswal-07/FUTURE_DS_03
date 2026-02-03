import pandas as pd
import plotly.express as px

# 1. Clean and Structure Funnel Data (Professional E-commerce dataset structure)
data = {
    'Stage': ['Website Visits', 'Product Views', 'Added to Cart', 'Checkout', 'Successful Purchase'],
    'User_Count': [125000, 68000, 22000, 9500, 4100],
    'Channel': ['Direct', 'Social Media', 'Organic Search', 'Referral', 'Paid Ads']
}
df = pd.DataFrame(data)

# 2. Analyze: Traffic-to-Lead & Lead-to-Customer conversion
# Calculating Conversion Rate per stage
df['Conversion_Rate (%)'] = (df['User_Count'] / df['User_Count'].shift(1).fillna(df['User_Count'][0]) * 100).round(2)

# Calculating Drop-off Rate at each stage
df['Drop_off_Rate (%)'] = (100 - df['Conversion_Rate (%)']).round(2)

# 3. Funnel Analysis Dashboard (Visualization)
fig = px.funnel(
    df, 
    x='User_Count', 
    y='Stage', 
    title='Marketing Funnel Performance - Future Interns Task 3',
    color='Stage',
    color_discrete_sequence=px.colors.sequential.Teal_r
)

# Showing interactive percentages
fig.update_traces(textinfo="value+percent initial")
fig.show()

# Display results for the report
print(df[['Stage', 'User_Count', 'Conversion_Rate (%)', 'Drop_off_Rate (%)']])

# Professional Comparison between Two Channels
comp_data = {
    'Stage': ['Visits', 'Views', 'Cart', 'Purchase'] * 2,
    'Users': [10000, 4500, 1200, 500,  # Channel A: Social Media
              10000, 6000, 2500, 1200], # Channel B: Paid Search
    'Channel': ['Social Media']*4 + ['Paid Search']*4
}
df_comp = pd.DataFrame(comp_data)

fig_comp = px.funnel(df_comp, x='Users', y='Stage', color='Channel', 
                     title='Channel-wise Funnel Comparison (Task 3)')
fig_comp.show()


