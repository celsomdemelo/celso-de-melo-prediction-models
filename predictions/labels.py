'''
Adds numerical and classification labels
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"


def add_numerical_label(df):
    df['total_three_points'] = 0

    for index, row in df.iterrows():
        if row['h_h1_three'] == -1 or row['h_h2_three'] == -1 or row['a_h1_three'] == -1 or row['a_h2_three'] == -1:
            df.set_value(index, 'total_three_points', -1)
        else:
            df.set_value(index, 'total_three_points',
                         row['h_h1_three'] + row['h_h2_three'] + row['a_h1_three'] + row['a_h2_three'])


def add_classification_labels(df):
    ranks = df.total_three_points.rank(pct=True)

    percentiles = [15, 20, 25, 30]

    for p in percentiles:
        label = 'total_3pts_' + str(p) + '_80_' + str(p)
        df[label] = '02_Normal'
        label_le = 'total_3pts_le_' + str(p)
        df[label_le] = 'No'
        label_ge = 'total_3pts_ge_' + str(p)
        df[label_ge] = 'No'

        fr = p / 100.0
        for index, row in df.iterrows():
            if ranks[index] <= fr:
                df.set_value(index, label, '01_Low')
                df.set_value(index, label_le, 'Yes')
            elif ranks[index] >= (1.0 - fr):
                df.set_value(index, label, '03_High')
                df.set_value(index, label_ge, 'Yes')
