import altair as alt
from vega_datasets import data

# A dropdown filter
categories_age = ['Total', '18 to 44', '45 to 65', '65+']
catage_dropdown = alt.binding_select(options=categories_age)
cat_select_age = alt.selection_single(fields=['Group'],
                                  bind=catage_dropdown,
                                  name="Age",
                                  init={'Group':'Total'})
categories_demo = ['Total', 'Male', 'Female', 'White', 'Black',
                     'Asian & Pacific Islander','Hispanic']
catdemo_dropdown = alt.binding_select(options=categories_demo)
cat_select_demo = alt.selection_single(fields=['Group'],
                                  bind=catdemo_dropdown,
                                  name="Demographic",
                                  init={'Group':'Total'})


# A slider filter
slider = alt.binding_range(min=2000, max=2018, step=2, name='Election Year')
select_yr = alt.selection_single(name='SelectorName', fields=['Year'],
                                   bind=slider, init={'Year': 2000})



def us_map_chart(df_in, map_value, map_title,selection_link=select_yr):
    df = df_in.copy()
    PIVOT_COLUMNS = ['STATE','id','Group','Year']
    columns_keep = PIVOT_COLUMNS + [map_value]
    year_columns = [str(year) for year in range(2000, 2019, 2)]
    
    df_pivot = df[columns_keep].pivot_table(index=['id','STATE','Group'], 
                                                                             columns='Year', values=map_value)
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
        from_=alt.LookupData(mapdf.loc[mapdf.Group=='Total'], 'id', ['STATE']+year_columns)
    ).transform_fold(
        year_columns, as_=['Year', 'Percent']
    ).transform_calculate(
        Year='parseInt(datum.Year)',
        Percent='isValid(datum.Percent) ? datum.Percent : -1'  
    ).encode(
        tooltip=['STATE:N','Percent:Q'],
        color = alt.condition(
            'datum.Percent > 0',
            alt.Color('Percent:Q', scale=alt.Scale(domain=[0.2,.9],scheme='yellowgreenblue', type='linear')),
            alt.value('#dbe9f6')
        )).add_selection(
        selection_link
    ).properties(
        title=map_title,
        width=415,
        height=200
    ).transform_filter(
        selection_link
    )
    
    return map_chart

def scatter_bar_turnout(df_in, x_value, y_value, color_variable, title, x_title, y_title,
                    select_slider=select_yr, select_dropdown='age'):
    
    if select_dropdown == 'age':
        dropdown_box = cat_select_age
    elif select_dropdown == 'sexrace':
        dropdown_box = cat_select_demo
    else:
        return print('Please set "select_dropdown = `age` or `sexrace`".')
        
    
    # A selection for interval highlighing on charts
    highlight = alt.selection_interval(encodings=['x'])
    color = alt.Color(color_variable)
    click = alt.selection_multi(encodings=['color'])
    
    df = df_in.copy()
    df = df.loc[df.STATE!='NATIONAL']
    
    scatter = alt.Chart().mark_point().encode(
        x=alt.X(x_value, title=x_title,
               scale=alt.Scale(domain=[.05, .96])),
        y=alt.Y(y_value, title=y_title,
               scale=alt.Scale(domain=[.05, .93])),
        size=alt.Size('Total:Q', title='Total Eligible Voters'),
        color=alt.condition(highlight, color_variable, alt.value('lightgray'), legend=None),
        tooltip=[alt.Tooltip('STATE:N', title='State'),
                 alt.Tooltip('Total:Q', title='Total Eligible Voters'),
                 alt.Tooltip('Total Registered:Q', title='Percent Registered Voters'),
                 alt.Tooltip('Total Voted:Q', title='Percent Voted')]
    ).add_selection(
        select_slider
    ).transform_filter(
        select_slider
    ).add_selection(
        dropdown_box
    ).transform_filter(
        dropdown_box
    ).add_selection(
        highlight
    ).transform_filter(
        click
    ).properties(
        title=title,
        width=400,
        height=200
    )
    
    
    bars = alt.Chart().mark_bar().encode(
        x=alt.X('count()', title='Number of States with Restrictive Laws'),
        y=alt.Y(color_variable, title='Restrictive Laws'),
        color=alt.condition(click, color, alt.value('lightgray'))
    ).transform_filter(
        highlight
    ).transform_filter(
        select_slider
    ).transform_filter(
        dropdown_box
    ).properties(
        width=400,
        height=80
    ).add_selection(
        click
    )

    return alt.vconcat(scatter, bars, data=df)
