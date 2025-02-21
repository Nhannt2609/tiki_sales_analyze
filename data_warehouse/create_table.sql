CREATE TABLE IF NOT EXISTS public."DimBrand"
(
    brand_id integer NOT NULL,
    brand character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "DimBrand_pkey" PRIMARY KEY (brand_id)
) TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public."DimCategory"
(
    category_id integer NOT NULL,
    category character varying(255) COLLATE pg_catalog."default",
    parent_category character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT "DimCategory_pkey" PRIMARY KEY (category_id)
) TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public."DimGender"
(
    gender_id character(1) COLLATE pg_catalog."default" NOT NULL,
    gender character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "DimGender_pkey" PRIMARY KEY (gender_id)
) TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public."DimProduct"
(
    product_id integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    original_price bigint,
    fulfillment_type character varying(50) COLLATE pg_catalog."default",
    review_count integer,
    rating_average numeric(3,2),
    favourite_count integer,
    number_of_images integer,
    has_video boolean,
    date_created integer,
    CONSTRAINT "DimProduct_pkey" PRIMARY KEY (product_id)
) TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public."DimSeller"
(
    seller_id integer NOT NULL,
    seller_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "DimSeller_pkey" PRIMARY KEY (seller_id)
) TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public."FactSales"
(
    product_id bigint NOT NULL,
    price bigint NOT NULL,
    pay_later boolean NOT NULL,
    vnd_cashback bigint NOT NULL,
    quantity_sold integer NOT NULL,
    brand_id integer NOT NULL,
    category_id integer NOT NULL,
    seller_id integer NOT NULL,
    gender_id character(1) COLLATE pg_catalog."default" NOT NULL,
    sales_id bigint NOT NULL,
    revenue bigint NOT NULL,
    CONSTRAINT "FactSales_pkey" PRIMARY KEY (sales_id),
    CONSTRAINT fk_factsales_brand FOREIGN KEY (brand_id)
        REFERENCES public."DimBrand" (brand_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_factsales_category FOREIGN KEY (category_id)
        REFERENCES public."DimCategory" (category_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_factsales_gender FOREIGN KEY (gender_id)
        REFERENCES public."DimGender" (gender_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_factsales_product FOREIGN KEY (product_id)
        REFERENCES public."DimProduct" (product_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_factsales_seller FOREIGN KEY (seller_id)
        REFERENCES public."DimSeller" (seller_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
) TABLESPACE pg_default;


