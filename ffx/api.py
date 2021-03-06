from sklearn.base import BaseEstimator, RegressorMixin
from . import core

"""api.py defines user interfaces to FFX. run() runs the complete method.
FFXRegressor is a Scikit-learn style regressor."""

def run(train_X, train_y, test_X, test_y, varnames=None, verbose=False):
    return core.MultiFFXModelFactory().build(train_X, train_y, test_X, test_y, varnames, verbose)

class FFXRegressor(BaseEstimator, RegressorMixin):
    """This class provides a Scikit-learn style estimator."""
    def __init__(self):
        super().__init__()
    def fit(self, X, y):
        # if X is a Pandas DataFrame, we don't have to pass in varnames.
        # otherwise we make up placeholders.        
        if hasattr(X, 'columns'):
            varnames = None
        else:
            varnames = ["X%d" % i for i in range(len(X))]
        self.models_ = run(X, y, X, y, varnames=varnames)
        self.model_ = self.models_[-1]
    def predict(self, X):
        return self.model_.predict(X)
    def complexity(self):
        return self.model_.complexity()
