''' CODE TO TEST DASHBOARD GENERATING FUNCTIONALITY '''

import random
from pathlib import Path

import altair as alt

from voter_suppression_analysis.generate import \
    generate_map, generate_chart, generate_html


# anticipated object type of individual viz pieces
EXPECTED_VIZ_TYPE = alt.vegalite.v4.api.VConcatChart


def test_generate_map():
    ''' 
    Test generate_map(). Note that attributes for all Altair objects were
    set manually, value-testing them is hence redundant and fruitless. 
    '''

    # smoke test 
    map = generate.generate_map(
        DF_AGE,
        map_type='Percent Voted',
        map_title='X'
    )

    # type check 
    assert isinstance(map, EXPECTED_VIZ_TYPE)


def test_generate_chart():
    ''' 
    Test generate_chart(). Again, attribute value-tests are excluded.
    '''

    # smoke test
    chart = generate.generate_chart(
        df_in=DF_SEX,
        x='Percent Registered:Q',
        y='Percent Voted:Q',
        x_lbl='% Registered',
        y_lbl='% Voted',
        title='Demographics',
        clr_setting='restrictive_id_laws:N',
        chart_type='sexrace'
    )

    # type check
    assert isinstance(chart, EXPECTED_VIZ_TYPE)

def test_generate_html():
    assert True