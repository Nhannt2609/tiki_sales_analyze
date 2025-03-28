﻿# 📊 Tiki Sales Analysis – Data Warehouse & ETL Pipeline

## 📌 Mô tả dự án
Dự án xây dựng hệ thống **Data Warehouse** cho dữ liệu bán hàng từ Tiki, sử dụng quy trình **Batching ETL** để trích xuất, biến đổi và tải dữ liệu từ file CSV vào PostgreSQL, sau đó phân tích & trực quan hóa trên Power BI.

## 🛠️ Công nghệ sử dụng
- **PostgreSQL**: Data Warehouse lưu trữ dữ liệu bán hàng
- **Python (Pandas, psycopg2)**: Xử lý ETL từ CSV → PostgreSQL
- **Power BI**: Trực quan hóa dữ liệu

## 🏗️ Kiến trúc hệ thống 

```mermaid
graph TD
    A["CSV Files (Kaggle)"] -->|Extract| B["Python ETL"]
    B -->|Transform| C["PostgreSQL Data Warehouse"]
    C -->|Load| D["Power BI Dashboard"]
```

## 🌟 Star schema
![](data_warehouse/star_schema.png)

## 📊 Biểu đồ
![](dashboard/page1.png)
![](dashboard/page2.png)
![](dashboard/page3.png)
