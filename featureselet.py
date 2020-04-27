import numpy
import heapq
def personselect(dict):
        trainset = dict["trainset"]
        #print(trainset)
        ylist = dict["y"]
        #print(ylist)
        index = dict["index"]
        result= []
        result_ = numpy.cov(trainset,ylist,True)
        for d in result_:
                result.append(d[-1])
        index_ = list(map(result.index,heapq.nlargest(6,result)))
        retu = []
        for ind in index_:
                if ind != 19:
                        retu.append(index[ind])
        print(retu)
        return  retu
