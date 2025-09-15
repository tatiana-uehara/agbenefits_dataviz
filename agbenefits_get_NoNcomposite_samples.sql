WITH results AS (
        SELECT 
            lower(replace(cas.hga_code, ' ', '')) AS hga_code_cleaned, 
            cas.hga_code, 
            cas.report_id, 
            cas.matrix, 
            cas.last_update AS sample_last_updated_at, 
            cas.sample_number AS campo_sample_number, 
            cas.so_start_date, 
            car.*
        FROM postgres.lab_results.campo_integ__analysis_result car
        JOIN postgres.lab_results.campo_integ__analysis_sample cas 
            ON car.analysis_sample_id = cas.id
    )

    SELECT 
        ss.point_id, 
        results.hga_code_cleaned, 
        ss.plot_type, 
        ss.sample_long_lat,
        ss.point_long_lat,
        ss.sampling_plan_campaign_number, 
        ss.sampling_plan_purpose, 
        ss.depth_range_top_m, 
        ss.depth_range_bottom_m, 
        ss.plot_name_from_overlap,
        results.campo_sample_number, 
        results.translated_standard_parameter, 
        results.numeric_result, 
        results.unit_pad
    FROM postgres.analytics_marts_v2.soil_samples ss
    JOIN results 
        ON lower(replace(ss.label, ' ', '')) = results.hga_code_cleaned
    WHERE ss.field_id = {field_id}