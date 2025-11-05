import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st 
import plotly.express as px
st.title("SALES ANALYSIS APP")
@st.cache_data
def load_data():
    df=pd.read_csv("product_sales_dataset_final.csv")
    date_col=pd.DatetimeIndex(df["Order_Date"])
    df["Year"]=date_col.year
    df["Month"]=date_col.month
    df["Date"]=date_col.day
    df.columns
    return df

df=load_data()
filtered_df=df.copy()
st.sidebar.header("filter options")

# region slicer
selected_region=st.sidebar.multiselect(
    "secect region",
    options=filtered_df["Region"].unique()
)
if selected_region:
    filtered_df=filtered_df[filtered_df["Region"].isin(selected_region)]

# state slicer
selected_states=st.sidebar.multiselect(
    "select states",
    options=filtered_df["State"].unique()
)
if selected_states:
    filtered_df=filtered_df[filtered_df["State"].isin(selected_states)]

# city slicer
selected_cities=st.sidebar.multiselect(
    "select city",
    options=filtered_df["City"].unique()
)
if selected_cities:
    filtered_df=filtered_df[filtered_df["City"].idin(selected_cities)]

# category slicer
selected_category=st.sidebar.multiselect(
    "select category",
    options=filtered_df["Category"].unique()
)
if selected_category:
    filtered_df=filtered_df[filtered_df["Category"].isin(selected_category)]

# sub category slicer
selected_subcategory=st.sidebar.multiselect(
    "select sub category",
    options=filtered_df["Sub_Category"].unique()
)
if selected_subcategory:
    filtered_df=filtered_df[filtered_df["Sub_Category"].isin(selected_subcategory)]
    
# year slicer
selected_year=st.sidebar.multiselect(
    "select the year",
    options=filtered_df["Year"].unique()
)   
if selected_year:
    filtered_df=filtered_df[filtered_df["Year"].isin(selected_year)] 
    
# month slicer
selected_month=st.sidebar.multiselect(
    "select the month",
    options=filtered_df["Month"].unique()
)   
if selected_month:
    filtered_df=filtered_df[filtered_df["Month"].isin(selected_month)] 
    
st.write("### filtered data")
st.dataframe(filtered_df)



# charts start from here
revenue_by_region=df.groupby("Region")[" Revenue "].sum().reset_index()
fig=px.pie(
    revenue_by_region,
    values=' Revenue ',
    names="Region",
    title="TOTAL REVENUE BY REGION",
    hole=0.4
)
st.plotly_chart(fig,use_container_width=True)

# bar chart
revenue_by_state=df.groupby("State")[" Revenue "].sum().reset_index()
fig=px.bar(
    revenue_by_state,
    x="State",
    y=" Revenue ",
    title="TOTAL REVENUE BY STATES"
)
st.plotly_chart(fig,use_container_width=True)
  
# barchart for city
revenue_by_city=df.groupby("City")[" Revenue "].sum().reset_index()
fig=px.bar(
    revenue_by_city,
    x="City",
    y=" Revenue ",
    title="TOTAL REVENUE BY CITY"
) 
st.plotly_chart(fig,use_container_width=True)

# piechart for revenue
revenue_by_category=df.groupby("Category")[" Revenue "].sum().reset_index()
fig=px.bar(
    revenue_by_category,
    x="Category",
    y=" Revenue ",
    title="TOTAL REVENUE BY CATEGORY"
)
st.plotly_chart(fig,use_container_width=True)

#bar chart for category
revenue_by_subcategory=df.groupby("Sub_Category")[" Revenue "].sum().reset_index()
fig=px.bar(
    revenue_by_subcategory,
    x="Sub_Category",
    y=" Revenue ",
    title="TOTAL REVENUE BY SUBCATEGORY"
) 
st.plotly_chart(fig,use_container_width=True)

# barchart for customer
customer_revenue=df.groupby("Customer_Name")[" Revenue "].sum().nlargest(10).reset_index()
fig=px.bar(
    customer_revenue,
    x="Customer_Name",
    y=" Revenue ",
    title="TOP CUSTOMER BY REVENUE"
)
st.plotly_chart(fig,use_container_width=True)

# yearly,monthly trend
st.header("YEARLY REVENUE TREND")
yearly_revenue=df.groupby("Year")[" Revenue "].sum()
fig1,ax1=plt.subplots()
yearly_revenue.plot(kind="line",marker="o",ax=ax1)
ax1.set_title("yearly revenue trend")
ax1.set_xlabel("Year")
ax1.set_ylabel("Total revenue")
st.pyplot(fig1)

# monthly revenue trends
st.header("MONTHLY REVENUE TREND")
monthly_revenue=df.groupby("Month")[" Revenue "].sum()
fig2,ax2=plt.subplots()
yearly_revenue.plot(kind="line",marker="o",ax=ax2)
ax1.set_title("monthly revenue trend")
ax1.set_xlabel("month")
ax1.set_ylabel("Total revenue")
st.pyplot(fig2)

# monthly trend across different years
st.header("MONTHLY TREND BY YEAR")
monthly_sales_by_year=df.pivot_table(index="Month",columns="Year",values=" Revenue ",aggfunc="sum")
fig3,ax3=plt.subplots()
monthly_sales_by_year.plot(kind="line",marker="o",ax=ax3)
ax3.set_title("monthly revenue trends by year")
ax3.set_xlabel("Month")
ax3.set_ylabel("total_revenue")
ax3.legend(title="Year")
st.pyplot(fig3)









