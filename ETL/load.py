import psycopg2
import csv
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    dbname="defaultdb",
    user="user",
    password=DB_PASSWORD,
    host="pg-27827a4c-job-analysis38129.h.aivencloud.com",
    port="14694",
    sslmode="require"
)
cursor = conn.cursor()

def load_data_category():
    with open("../data/processed/category.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề nếu có

        for row in reader:
            category = row[1]
            category_id = int(row[2])
            parent_category = row[3]

            cursor.execute("""
                INSERT INTO "DimCategory" (category, category_id, parent_category)
                VALUES (%s, %s, %s)
                ON CONFLICT (category_id) DO NOTHING;
            """, (category, category_id, parent_category))

def load_data_gender():
    with open("../data/processed/gender.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề nếu có

        for row in reader:
            gender_id = row[0]
            gender = row[1]

            cursor.execute("""
                INSERT INTO "DimGender" (gender_id, gender)
                VALUES (%s, %s)
                ON CONFLICT (gender_id) DO NOTHING;
            """, (gender_id, gender))

def load_data_brand():
    with open("../data/processed/brand.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề nếu có

        for row in reader:
            brand_id = row[2]
            brand = row[1]

            cursor.execute("""
                INSERT INTO "DimBrand" (brand_id, brand)
                VALUES (%s, %s)
                ON CONFLICT (brand_id) DO NOTHING;
            """, (brand_id, brand))
            
def load_data_seller():
    with open("../data/processed/seller.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề nếu có

        for row in reader:
            seller_id = row[2]
            seller_name = row[1]

            cursor.execute("""
                INSERT INTO "DimSeller" (seller_id,seller_name)
                VALUES (%s, %s)
                ON CONFLICT (seller_id) DO NOTHING;
            """, (seller_id,seller_name))

def load_data_product():
    with open("../data/processed/product.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề nếu có

            for row in reader:
                product_id = int(row[1])
                name = row[2]
                description = row[3] if row[3] else None
                original_price = int(row[4]) if row[4] else None
                fulfillment_type = row[5] if row[5] else None
                review_count = int(row[6]) if row[6] else 0
                rating_average = float(row[7]) if row[7] else None
                favourite_count = int(row[8]) if row[8] else 0
                number_of_images = int(row[9]) if row[9] else 0
                has_video = row[10].lower() == "true"  # Chuyển đổi sang Boolean
                date_created = int(row[11]) if row[11] else None

                # Thực thi câu lệnh INSERT
                cursor.execute("""
                    INSERT INTO "DimProduct" (
                        product_id, name, description, original_price, 
                        fulfillment_type, review_count, rating_average, 
                        favourite_count, number_of_images, has_video, date_created
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (product_id) DO NOTHING;
                """, (product_id, name, description, original_price, 
                      fulfillment_type, review_count, rating_average, 
                      favourite_count, number_of_images, has_video, date_created))

# load_data_category()
# load_data_gender()
# load_data_brand()
# load_data_seller()
load_data_product()


conn.commit()

