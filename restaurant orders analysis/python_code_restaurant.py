# importing the orders file
import pandas as pd
orders_df = pd.read_csv(r"/Users/hubertkrajewski/Desktop/Restaurant+Orders+CSV/order_details.csv")
orders_df.head(10)

import pandas as pd
orders_df = pd.read_csv(r"/Users/hubertkrajewski/Desktop/Restaurant+Orders+CSV/order_details.csv")
orders_df.tail(10)

# dataframe orders info
orders_df.info()

# droping the missing values
orders_df.dropna()

# importing second dataset
menu_df = pd.read_csv(r"/Users/hubertkrajewski/Desktop/Restaurant+Orders+CSV/menu_items.csv")
menu_df.head()

# dataframe menu info
menu_df.info()

# merging the two dataframes on left join
order_items_df = orders_df.merge(menu_df, how = 'left', left_on = 'item_id', right_on = 'menu_item_id').drop('menu_item_id', axis = 1)
order_items_df.head()

# adding sales tax and total price columns
order_items_df['sales_tax'] = (order_items_df.price * 0.08).round(2)
order_items_df['total_revenue'] = order_items_df.price + order_items_df.sales_tax
order_items_df.head()

# joined dataframes info
order_items_df.info()

# changing the order_date column data type to datetime
orders_items_df = pd.read_csv(r"/Users/hubertkrajewski/Desktop/Restaurant+Orders+CSV/order_details.csv", parse_dates = ['order_date'])
orders_items_df['order_date'] = pd.to_datetime(orders_items_df['order_date'])

# table of numerical statistics
order_items_df.describe()

# horizontal bar chart of total revenue by item name 
(order_items_df
 .groupby('item_name')
 .agg({'total_revenue': 'sum'})
 .sort_values('total_revenue')
 .plot
 .barh()
 )

# horizontal bar chart of total revenue by item name for Italian category
(order_items_df
 .query("category == 'Italian'")
 .groupby('item_name')
 .agg({'total_revenue': 'sum'})
 .sort_values('total_revenue')
 .plot
 .barh()
 )

# analysing trends in total revenue based on order date day
order_items_df.set_index("order_date").resample("D")["total_revenue"].sum().plot(ylim=0)

# analysing trends in total revenue based on order date month
order_items_df.set_index("order_date").resample("M")["total_revenue"].sum().plot(ylim=0)

# adding new columns to the dataframe extracting the day of the week and hour of the order
order_items_df['dayofweek'] = order_items_df.order_time.dt.dayofweek
order_items_df['hour'] = order_items_df.order_time.dt.hour
