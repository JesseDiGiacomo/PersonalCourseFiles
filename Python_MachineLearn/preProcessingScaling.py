import numpy

#Scaling using sklearn MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

weights = numpy.array([[115.],[140.],[175.]])
scaler = MinMaxScaler()
rescaled_weights = scaler.fit_transform(weights)
print rescaled_weights

#Scaling "by hand"
def featureScaling(arr):
    xMax = max(data)
    xMin = min(data)
    scale_factor = (140. - xMin)/(xMax - xMin)
    if scale_factor != 0:
        return scale_factor
    else:
        print "Not Valid Factor!"

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print "Scale factor for 140: ",featureScaling(data)
