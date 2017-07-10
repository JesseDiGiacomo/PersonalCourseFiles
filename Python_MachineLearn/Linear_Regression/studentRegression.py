def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg

    ### your code goes here!
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit(ages_train, net_worths_train)

    reg.coef_
    '''
    print "Katie's Networth prediction: ", reg.predict([27])
    print "Slope: ", reg.coef_
    print "Intercept: ", reg.intercept_
    print "\n ### Stats on test dataset ### \n"
    print "r-squared score: ", reg.score(age_test, networth_test)
    print "\n ### Stats on training dataset ### \n"
    print "r-squared score: ", reg.score(age_train, networth_train)
    '''
    return reg
