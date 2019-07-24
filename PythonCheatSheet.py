1. DataFrame.applymap(self, func)[source]
  Apply a function to a Dataframe elementwise.

  This method applies a function that accepts and returns a scalar to every element of a DataFrame.

#----Check whether all elements are real or not
tmp = pd.DataFrame({"ID":[1,2,3],"Name":["a","b","c"]})
tmp.applymap(np.isreal).all()
