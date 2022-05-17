SELECT
    u.user_id AS user_id,
    GETDATE() AS current_date,
    u.timestamp_registered AS created_at,
    CASE
        WHEN u.timestamp_registered  >= current_date - 30 then 'last_30d'
        WHEN u.timestamp_registered  >= current_date - 90 and u.timestamp_registered  < current_date - 30 then 'last_90d'
        WHEN u.timestamp_registered  >= current_date - 180 and u.timestamp_registered  < current_date - 90 then 'last_180d'
        WHEN u.timestamp_registered  >= current_date - 365 and u.timestamp_registered  < current_date - 180 then 'last_360d'
        ELSE 'last_360d_more'
    END AS group_user,
    u.status AS user_status,
    u.email AS user_email
FROM data_market_staging.stg_marketplace__users u




SELECT
    stableton_deal_id AS activity_id,
    added_timestamp AS ts,
    NULL as anonymous_customer_id, -- used in identity resolution
    person_id AS customer,
   'deal_created' AS activity, -- ex. 'viewed_page'
    product_name AS feature_1,
    units AS feature_2,
    deal_channel AS feature_3,
    NULL AS revenue_impact,
    url::TEXT AS link
FROM data_market.dim_deals
WHERE pipeline_id = 1 -- investor pipeline





WITH docsend_clicks AS (
    SELECT
        *,
        ROW_NUMBER () OVER (ORDER BY visit_timestamp ASC) AS id
    FROM data_market_staging.stg_stableton_user_activity__docsend
)
SELECT
    id AS activity_id,
    visit_timestamp AS ts,
    visitor_email as anonymous_customer_id, -- used in identity resolution
    NULL AS customer,
   'click_docsend' AS activity, -- ex. 'viewed_page'
    p.name AS feature_1,
    document_category AS feature_2,
    NULL AS feature_3,
    NULL AS revenue_impact,
    NULL AS link
FROM docsend_clicks c
LEFT JOIN data_market.dim_products p ON c.product_id_numeric = p.crm_product_id
