'''
GLM 3-Point prediction
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib

from predictions.feature_sets import clean_df
from predictions.metrics import linear_regression_accuracy, linear_regression_accuracy_greater_or_equal_than

from sklearn.preprocessing import StandardScaler

from predictions.utils import sort_coef


def find_best_model(features, label, df_train, df_eval, verbose=False, scale=False):
    df_train_clean = clean_df(df_train, features + [label])
    df_eval_clean = clean_df(df_eval, features + [label])

    df_train_clean_data = df_train_clean[features]
    df_eval_clean_data = df_eval_clean[features]
    if scale:
        scaler = StandardScaler()
        scaler.fit(df_train_clean_data)
        df_train_clean_data = scaler.transform(df_train_clean_data)
        df_eval_clean_data = scaler.transform(df_eval_clean_data)

    normalize = False
    # normalize_options = [False,
    #                      # True # Doesn't seem to make any difference
    #                      ]
    #
    # for normalize in normalize_options:
    regr = linear_model.LinearRegression(normalize=normalize)
    regr.fit(df_train_clean_data, df_train_clean[[label]].values.ravel())
    print('**************************************************************************')
    print('Ordinary Least Squares: normalize = ' + str(normalize) + ' Eval R2: '
          + str(regr.score(df_eval_clean_data, df_eval_clean[[label]].values.ravel())))
    print('\tTraining R2: ' + str(
        regr.score(df_train_clean_data, df_train_clean[[label]].values.ravel())))
    print('\tEvaluation R2: ' + str(
        regr.score(df_eval_clean_data, df_eval_clean[[label]].values.ravel())))

    y_pred = regr.predict(df_eval_clean_data)
    if verbose:
        print("Mean squared error: %.7f" %
              mean_squared_error(df_eval_clean[[label]].values.ravel(), y_pred))
        print('Variance score: %.7f' % r2_score(df_eval_clean[[label]].values.ravel(), y_pred))
        for e in range(1, 6):
            print('Accuracy (error = ' + str(e) + '): %.7f' % linear_regression_accuracy(
                df_eval_clean[[label]].values.ravel(), y_pred, error_threshold=e))
        for e in range(0, 8):
            print('Accuracy (greater or equal than, error = ' + str(
                e) + '): %.7f' % linear_regression_accuracy_greater_or_equal_than(
                df_eval_clean[[label]].values.ravel(), y_pred, error_threshold=e))

    return [
        regr,
        regr.score(df_eval_clean_data, df_eval_clean[[label]].values.ravel()),
        linear_regression_accuracy_greater_or_equal_than(
            df_eval_clean[[label]].values.ravel(), y_pred, error_threshold=3)
    ]

def select_error(errors):
    selected = None

    for e in errors:
        if e[1] >= .7 and e[1] < .8:
            if selected is None or (e[1] > selected[1] and e[0] < 4):
                selected = e

    if selected is None:
        for e in errors:
            if e[1] >= .8 and e[1] < .9:
                if selected is None or (e[1] > selected[1] and e[0] < 4):
                    selected = e

    if selected is None:
        for e in errors:
            if e[1] >= .9 and e[1] < .95:
                if selected is None or (e[1] > selected[1] and e[0] < 4):
                    selected = e

    if selected is None:
        selected = errors[len(errors)-1]
    return selected

def score_on_test_set(features, label, df_train_eval, df_test, normalize=False, path=None):
    detailed_score = {'label': label, 'r2': -1,
                      'gt_err': -1, 'gt_acc': 0,
                      'rg_err': -1, 'rg_acc': 0,
                      '25th_perc_acc': 0, '75th_perc_acc': 0}

    df_train_eval_clean = clean_df(df_train_eval, features + [label])
    df_test_clean = clean_df(df_test, features + [label])

    regr = linear_model.LinearRegression(normalize=normalize)
    regr.fit(df_train_eval_clean[features], df_train_eval_clean[[label]].values.ravel())

    if path is not None:
        joblib.dump(regr, path)

    detailed_score['r2'] = regr.score(df_test_clean[features], df_test_clean[[label]].values.ravel())
    print('**************************************************************************')
    print('Ordinary Least Squares: normalize = ' + str(normalize) + ' Test R2: ' + str(detailed_score['r2']))
    print('\tTraining + Eval R2: ' + str(
        regr.score(df_train_eval_clean[features], df_train_eval_clean[[label]].values.ravel())))
    print('\tTest R2: ' + str(detailed_score['r2']))

    y_pred = regr.predict(df_test_clean[features])
    print("Mean squared error: %.7f" %
          mean_squared_error(df_test_clean[[label]].values.ravel(), y_pred))
    print('Variance score: %.7f' % r2_score(df_test_clean[[label]].values.ravel(), y_pred))
    rg_errors = []
    for e in range(1, 6):
        acc = linear_regression_accuracy(df_test_clean[[label]].values.ravel(), y_pred, error_threshold=e)
        rg_errors.append((e, acc))
        print('Accuracy (error = ' + str(e) + '): %.7f' % acc)
    selected_rg_error = select_error(rg_errors)
    detailed_score['rg_err'] = selected_rg_error[0]
    detailed_score['rg_acc'] = selected_rg_error[1]

    gt_errors = []
    for e in range(0, 8):
        acc = linear_regression_accuracy_greater_or_equal_than(df_test_clean[[label]].values.ravel(), y_pred, error_threshold=e)
        gt_errors.append((e, acc))
        print('Accuracy (greater or equal than, error = ' + str(e) + '): %.7f' % acc)
    selected_gt_error = select_error(gt_errors)
    detailed_score['gt_err'] = selected_gt_error[0]
    detailed_score['gt_acc'] = selected_gt_error[1]

    print('**************************************************************************')
    print('COEFFICIENTS')
    print('**************************************************************************')
    print('Intercept: ' + str(regr.intercept_))
    sorted_coefs = sort_coef(features, regr.coef_)
    for k in sorted_coefs:
        print(k[0] + '\t' + str(k[1]))

    return detailed_score
