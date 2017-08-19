from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkContext
from pprint import pprint as pp

sc = SparkContext()
try:
    model = MatrixFactorizationModel.load(sc, "CF.model")
except Excetion:
    model = None
def main():
    data = load_file("training_data")
    model = train(data)
    # Evaluate the model on training data
    '''
    testdata = ratings.map(lambda p: (p[0], p[1]))
    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
    MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
    print("Mean Squared Error = " + str(MSE))
    '''
    pp(get_rec(int_hash(76561198067457280)))

def train(data):
    '''
    insert documentation
    '''
    global model
    # Build the recommendation model using Alternating Least Squares
    rank = 10
    numIterations = 10
    model = ALS.train(data, rank, numIterations)
    # model.save(sc, "CF.model")

    return model

def get_rec(user, num_rec=10):
    global model
    return model.recommendProducts(user, num_rec)

def load_file(filename):
    global sc
    return sc.textFile(filename).map(lambda l: l.split(',')).map(lambda l: Rating(int_hash(int(l[0])), int(l[1]), float(l[2])))

def int_hash(s):
    return hash(s) % 2147483647

main()