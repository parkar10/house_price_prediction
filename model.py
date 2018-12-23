from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from feature_scaling import FeatureScaling

if __name__ == "__main__":
    fc = FeatureScaling()
    train_data, test_data = fc.getFeaturedDataframe()
    x_train , x_test , Y_train , Y_test = train_test_split(train_data , test_data , random_state = 2 ,test_size = 0.10 , )
    reg = LinearRegression()
    reg.fit(x_train , Y_train)
    print(reg.score(x_test, Y_test))

    