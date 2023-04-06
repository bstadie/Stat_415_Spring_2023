import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt


def get_linear_data():
    # Toy dataset
    x = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168],
                        [9.779], [6.182], [7.59], [2.167], [7.042],
                        [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)

    eps = np.random.randn(15, 1)



    x += eps


    y = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573],
                        [3.366], [2.596], [2.53], [1.221], [2.827],
                        [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)

    return x, y


def get_student_data():
    path_to_file = '/Users/lectures/Desktop/student_scores.csv'
    df = pd.read_csv(path_to_file)
    y = df['Scores'].values.reshape(-1, 1)
    x = df['Hours'].values.reshape(-1, 1)
    return x, y


def make_plot(x_test, y_test, y_pred):
    plt.scatter(x_test, y_test, color="black")
    plt.plot(x_test, y_pred, color="blue", linewidth=3)
    plt.show()


def main():
    #x, y = get_linear_data()
    x, y = get_student_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)
    regr = linear_model.LinearRegression()
    regr.fit(x, y)
    y_pred = regr.predict(x_test)
    print(F"Coefficients: {regr.coef_}")
    print(F"Mean squared error: {mean_squared_error(y_test, y_pred)}")
    make_plot(x_test, y_test, y_pred)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
