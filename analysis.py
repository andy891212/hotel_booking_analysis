import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 讀取資料
df = pd.read_csv("hotel_bookings.csv")

# 選擇欄位 + 處理類別變數
features = ['lead_time', 'adr', 'market_segment', 'is_repeated_guest', 'booking_changes']
df = df[features + ['is_canceled']]
df = pd.get_dummies(df, drop_first=True)

# 分割訓練集與測試集
X = df.drop("is_canceled", axis=1)
y = df["is_canceled"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建模
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 評估
print(classification_report(y_test, y_pred))
# precision    recall  f1-score   support
#
#           0       0.81      0.86      0.84     14907
#          1       0.74      0.67      0.71      8971
#
#    accuracy                           0.79     23878
#   macro avg       0.78      0.77      0.77     23878
#   weighted avg       0.79      0.79      0.79     23878

import pandas as pd
import calendar
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取原始資料
df = pd.read_csv('hotel_bookings.csv')

# 將 arrival_date_month 轉成有順序的類別型別，方便月份排序
df['arrival_date_month'] = pd.Categorical(
    df['arrival_date_month'],
    categories=list(calendar.month_name)[1:],  # January ~ December
    ordered=True
)

# 計算每筆訂單營收 = adr × 住宿晚數 (stays_in_weekend_nights + stays_in_week_nights)
df['total_revenue'] = df['adr'] * (df['stays_in_weekend_nights'] + df['stays_in_week_nights'])

# 1. 各月份總營收趨勢
monthly_revenue = df.groupby('arrival_date_month')['total_revenue'].sum().sort_index()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_revenue.index, y=monthly_revenue.values)
plt.title('Monthly total revenue trend')
plt.ylabel('Total revenue')
plt.xlabel('month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. 不同市場來源（market_segment）在不同月份的營收
monthly_market_revenue = df.groupby(['arrival_date_month', 'market_segment'])['total_revenue'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_market_revenue, x='arrival_date_month', y='total_revenue', hue='market_segment', marker='o')
plt.title('Monthly revenue changes by market source')
plt.ylabel('Total revenue')
plt.xlabel('month')
plt.xticks(rotation=45)
plt.legend(title='Market Source')
plt.tight_layout()
plt.show()

# 3. 城市飯店與渡假飯店不同月份營收比較
hotel_monthly_revenue = df.groupby(['arrival_date_month', 'hotel'])['total_revenue'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=hotel_monthly_revenue, x='arrival_date_month', y='total_revenue', hue='hotel', marker='o')
plt.title('Comparison of monthly revenue between city hotels and resort hotels')
plt.ylabel('Total revenue')
plt.xlabel('month')
plt.xticks(rotation=45)
plt.legend(title='Hotel Type')
plt.tight_layout()
plt.show()







