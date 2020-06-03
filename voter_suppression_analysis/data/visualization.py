import altair as alt
from vega_datasets import data
import requests
import geopandas as gpd
import json
import re

# A dropdown filter
categories_age = ['Total', '18 to 44', '45 to 65', '65+']
catage_dropdown = alt.binding_select(options=categories_age)
cat_select_age = alt.selection_single(fields=['group'],
                                  bind=catage_dropdown,
                                  name="Demographic",
                                  init={'group':'Total'})
categories_demo = ['Total', 'Male', 'Female', 'White', 'Black',
                     'Asian & Pacific Islander','Hispanic']
catdemo_dropdown = alt.binding_select(options=categories_demo)
cat_select_demo = alt.selection_single(fields=['group'],
                                  bind=catdemo_dropdown,
                                  name="Demographic",
                                  init={'group':'Total'})


# A slider filter
slider = alt.binding_range(min=2000, max=2018, step=2, name='Election Year')
select_yr = alt.selection_single(name='SelectorName', fields=['yr'],
                                   bind=slider, init={'yr': 2000})



def us_map_chart(df_in, map_value, map_title,selection_link=select_yr):
    df = df_in.copy()
    PIVOT_COLUMNS = ['state','id','group','yr']
    columns_keep = PIVOT_COLUMNS + [map_value]
    year_columns = [str(year) for year in range(2000, 2019, 2)]

    df_pivot = df[columns_keep].pivot_table(index=['id','state','group'],
                                                                             columns='yr', values=map_value)
    mapdf = df_pivot.reset_index()
    mapdf.columns = mapdf.columns.astype(str)

    states = alt.topo_feature(data.us_10m.url, 'states')
    states['url'] = 'https://raw.githubusercontent.com/vega/vega/master/docs/data/us-10m.json'

    map_chart=alt.Chart(states).mark_geoshape(
    stroke='black',
    strokeWidth=0.05
    ).project(
        type='albersUsa'
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(mapdf.loc[mapdf.group=='Total'], 'id', ['state']+year_columns)
    ).transform_fold(
        year_columns, as_=['yr', 'Percent']
    ).transform_calculate(
        yr='parseInt(datum.yr)',
        Percent='isValid(datum.Percent) ? datum.Percent : -1'
    ).encode(
        tooltip=['state:N','Percent:Q'],
        color = alt.condition(
            'datum.Percent > 0',
            alt.Color('Percent:Q', scale=alt.Scale(domain=[0.2,.9],scheme='yellowgreenblue', type='linear')),
            alt.value('#dbe9f6')
        )).add_selection(
        selection_link
    ).properties(
        title=map_title,
        width=300,
        height=200
    ).transform_filter(
        selection_link
    )

    return map_chart

def scatter_turnout(df_in, x_value, y_value, color_variable, title, x_title, y_title,
                    select_slider, select_dropdown):

    # A selection for interval highlighing on charts
    highlight = alt.selection_interval(encodings=['x'])
    color = alt.Color(color_variable)
    click = alt.selection_multi(encodings=['color'])

    df = df_in.copy()

    scatter = alt.Chart().mark_point().encode(
        x=alt.X(x_value, title=x_title,
               scale=alt.Scale(domain=[.15, .96])),
        y=alt.Y(y_value, title=y_title,
               scale=alt.Scale(domain=[.15, .93])),
        size=alt.Size('total:Q', title='Total Eligible Voters'),
        color=alt.condition(highlight, color_variable, alt.value('lightgray'), legend=None),
        tooltip=[alt.Tooltip('state:N', title='State'),
                 alt.Tooltip('total:Q', title='Total Eligible Voters'),
                 alt.Tooltip('total_reg:Q', title='Percent Registered Voters'),
                 alt.Tooltip('total_voted:Q', title='Percent Voted')]
    ).add_selection(
        select_slider
    ).transform_filter(
        select_slider
    ).add_selection(
        select_dropdown
    ).transform_filter(
        select_dropdown
    ).add_selection(
        highlight
    ).transform_filter(
        click
    ).properties(
        width=500,
        height=275
    )

    bars = alt.Chart().mark_bar().encode(
        x='count()',
        y=alt.Y(color_variable, title='Restrictive Laws'),
        color=alt.condition(click, color, alt.value('lightgray'))
    ).transform_filter(
        highlight
    ).transform_filter(
        select_yr
    ).transform_filter(
        select_dropdown
    ).properties(
        width=500,
        height=100
    ).add_selection(
        click
    )

    return alt.vconcat(scatter, bars, data=df, title=title)
