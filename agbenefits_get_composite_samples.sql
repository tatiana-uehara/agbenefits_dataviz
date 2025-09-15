WITH results AS (
    SELECT
        car.*,
        car.id as analysis_id,
        cas.hga_code,
        cas.report_id,
        cas.matrix,
        cas.last_update AS sample_last_updated_at,
        cas.sample_number AS campo_sample_number,
        cas.so_start_date,
        -- join key is necessary to isolate the unique part of the composite key scientific label
        -- this is a scientific label: FARM-FIELD-CAMPAIGN_NUMBER-BOTTOM_DEPTH-POINT_ID-CS1
        -- this is the unique part being isolated: -CAMPAIGN_NUMBER-BOTTOM_DEPTH-POINT_ID-CS
        REGEXP_SUBSTR(cas.hga_code, '(-[0-9]+-[0-9]+-[0-9]+-CS)') AS join_key,
        lower(replace(cas.hga_code, ' ', '')) AS hga_code_cleaned
    FROM postgres.lab_results.campo_integ__analysis_result AS car
    INNER JOIN
        postgres.lab_results.campo_integ__analysis_sample AS cas
        ON (car.analysis_sample_id = cas.id)
),
composite_sample_data AS (
    SELECT DISTINCT
        css.id,
        css.label AS composite_soil_sample_label,
        -- 2. Adicionamos a mesma 'join_key' aqui, extraindo o padrão do label.
        REGEXP_SUBSTR(css.label, '(-[0-9]+-[0-9]+-[0-9]+-CS)') AS join_key,
        ss.sample_taken_timestamp,
        ss.sample_is_bulk_density,
        ss.sampling_plan_name,
        ss.sampling_plan_purpose,
        ss.sampling_plan_campaign_number,
        ss.sampling_plan_date_generated,
        ss.sample_long_lat,
        ss.field_id,
        ss.field_name,
        ss.plot_type,
        ss.plot_id,
        ss.farm_id,
        ss.farm_name,
        ss.point_id,
        ss.depth_range_bottom_m,
        ss.depth_range_top_m,
        ss.point_long_lat,
        ss.point_valid_end,
        ss.point_valid_start,
        ss.sampling_plan_id,
        ss.sampling_plan_field_id,
        ss.sampling_plan_field_name,
        ss.sampling_plan_farm_id,
        ss.sampling_plan_farm_name,
        ss.field_id_from_overlap,
        ss.field_name_from_overlap,
        ss.farm_id_from_overlap,
        ss.farm_name_from_overlap,
        ss.plot_area_ha,
        ss.farm_and_field,
        ss.field_sampling_plan,
        ss.plot_name_from_overlap
    FROM postgres.analytics_marts_v2.soil_samples AS ss
    INNER JOIN
        postgres.public.composite_soil_sample_to_soil_sample AS csstss
        ON (ss.sample_id = csstss.soil_sample_id)
    INNER JOIN
        postgres.public.composite_soil_samples AS css
        ON (csstss.composite_soil_sample_id = css.id)
),
final AS (
    SELECT 
        csd.point_id, 
        r.hga_code_cleaned, 
        csd.plot_type, 
        csd.sample_long_lat,
        csd.point_long_lat,
        csd.sampling_plan_campaign_number, 
        csd.sampling_plan_purpose, 
        csd.depth_range_top_m, 
        csd.depth_range_bottom_m, 
        csd.plot_name_from_overlap,
        r.campo_sample_number, 
        r.translated_standard_parameter, 
        r.numeric_result, 
        r.unit_pad
        -- csd.point_id,
        -- csd.plot_type,
        -- csd.sampling_plan_campaign_number,
        -- csd.sampling_plan_purpose,
        -- csd.depth_range_top_m,
        -- csd.depth_range_bottom_m,
        -- csd.sample_long_lat,
        -- csd.point_long_lat, -- tati add aqui
        -- r.campo_sample_number,
        -- r.translated_standard_parameter,
        -- r.numeric_result,
        -- r.unit_pad
    FROM composite_sample_data AS csd
    INNER JOIN results AS r
        ON csd.join_key = r.join_key
    WHERE csd.field_id = {field_id}
)
SELECT 
   -- point_id,  
   -- plot_type, 
   -- sample_long_lat,
   -- point_long_lat, -- tati add aqui
   -- sampling_plan_campaign_number, 
   -- sampling_plan_purpose, 
   -- depth_range_top_m, 
   -- depth_range_bottom_m, 
   -- campo_sample_number, 
   -- translated_standard_parameter, 
   -- numeric_result, 
   -- unit_pad
   point_id, 
   hga_code_cleaned, 
   plot_type, 
   sample_long_lat,
   point_long_lat,
   sampling_plan_campaign_number, 
   sampling_plan_purpose, 
   depth_range_top_m, 
   depth_range_bottom_m, 
   plot_name_from_overlap,
   campo_sample_number, 
   translated_standard_parameter, 
   numeric_result, 
   unit_pad
FROM final;