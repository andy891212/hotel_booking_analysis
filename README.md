# 🏨 Hotel Booking Demand Analysis

本專案使用來自 [Kaggle: Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) 的資料集，進行以下兩大主題的數據分析：

1. **預測訂單是否會被取消**（分類模型）
2. **分析不同月份、不同市場來源的營收變化趨勢**

---

## 📂 專案內容說明

### 🔍 主題一：預測取消訂單（Classification）

在飯店產業中，預訂取消率對營收與資源調度有很大的影響，特別是在旅遊旺季，若能預測哪些訂單有可能被取消，飯店可以提早調整價格、重新開放房間，提高住房率與營收，因此我選擇以機器學習模型來預測訂單是否會被取消。

資料集裡面包含了顧客的預訂時間、房價、是否是回頭客、訂單修改次數、來自的市場來源等等，在前處理階段，我挑選了與取消行為可能有關的特徵。

使用 `RandomForestClassifier` 預測哪些預訂會被取消，幫助飯店提前預測潛在損失與資源調度：

- 選取特徵：
  - `lead_time`：提前訂房的天數
  - `adr`：平均每日房價
  - `market_segment`：市場來源
  - `is_repeated_guest`：是否為回訪旅客
  - `booking_changes`：訂單變更次數
    
- 模型評估結果（accuracy: **79%**）：

|  | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.81      | 0.86   | 0.84     | 14907   |
| 1     | 0.74      | 0.67   | 0.71     | 8971    |
| **Accuracy** |        |        | **0.79** | 23878   |

 整體準確率約為 79%，而且對於正類（被取消）也有 74% 的 precision 和 67% 的 recall，代表模型在實務上已有一定的參考價值。

| 指標名稱               | 說明                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| **Precision（精確率）** | 預測為「取消」的訂單中，有多少是真的取消。<br>→ 準不準？預測為取消的正確率。<br>**公式：** `Precision = TP / (TP + FP)`                   |
| **Recall（召回率）**    | 實際「取消」的訂單中，有多少被模型正確預測出來。<br>→ 有沒有漏？抓取消的能力。<br>**公式：** `Recall = TP / (TP + FN)`                     |
| **F1-score**       | 精確率與召回率的加權平均，反映兩者的平衡性。<br>→ 準且全面。<br>**公式：** `F1 = 2 * (Precision * Recall) / (Precision + Recall)` |
| **Support（樣本數）**   | 測試集中該類別的實際樣本數。                                                                                      |
| **Accuracy（準確率）**  | 所有正確預測佔全部樣本的比例。<br>→ 整體模型的準確表現。                                                                     |


---

### 📈 主題二：每月營收趨勢分析

分析飯店在不同月份、不同市場來源、不同類型（城市/渡假）之營收表現變化：

#### 📊 每月總營收變化

![Monthly Revenue](figure/monthly_revenue.png)

---

#### 🛫 各市場來源每月營收變化

![Revenue by Market Segment](figure/revenue_by_market_segment.png)

---

#### 🏨 城市飯店 vs 渡假飯店 營收比較

![Revenue by Hotel Type](figure/revenue_by_hotel_type.png)

---

## 🛠 使用套件（requirements.txt）

- pandas  
- matplotlib  
- seaborn  
- scikit-learn  

---

## 🚀 如何執行本專案

1. 確保已安裝 Python (建議版本 >=3.8)
2. 安裝必要套件：
    ```bash
    pip install -r requirements.txt
    ```
3. 放置 `hotel_bookings.csv` 到專案根目錄下
4. 執行 `analysis.py` 即可：

    ```bash
    python analysis.py
    ```

---

## 📎 資料來源

- Kaggle Dataset: [Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
