with current_plots as( 
select field_id,  
        plot_type::varchar,
        boundary
from public.plots
where valid_end is null)

select * 
from current_plots
join analytics_base.stg_farms_and_fields using(field_id)
where field_id = {field_id}