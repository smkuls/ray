#include "fulcrum_scheduler_algorithm.h"
#include <stdlib.h> 
#include <assert.h>


/**
 * Function to register a DBClientID of a local scheduler 
 *
 * @param id = DBClientID of the local scheduler being registered
 * @return void
 */
void FulcrumSchedulerAlgorithm::registerLs(DBClientID id) {
    if(lsLoadMap.find(id) == lsLoadMap.end()){
        lsLoadMap[id] = 0;
    }
}

/**
 * Function goes through the local scheduler load map and exponentially decays the load values
 *
 * @param
 * @return void
 */
void FulcrumSchedulerAlgorithm::refreshLsLoad() {
    for(auto x : lsLoadMap){
        lsLoadMap[x.first] = (int)(x.second * LOAD_DECAY_RATE);
    }
}

/**
 * Function updates the load map with latest local scheduler load value
 *
 * @param
 * @return void
 */
void FulcrumSchedulerAlgorithm::updateLsLoad(DBClientID localSchdID) {
    lsLoadMap[localSchdID] += 1;
}

/**
 * Function finds the local scheduler node based on weighted load value
 *
 * @param
 * @return DBClientID
 */
DBClientID FulcrumSchedulerAlgorithm::findLsByWeightedLoad(vector<DBClientID> &candidates) {
    int totalWt = 0, maxWt = 1;
    for(DBClientID id : candidates){
        int load = lsLoadMap[id];
        totalWt += load;
        maxWt = std::max(maxWt, load+1);
    }
    totalWt = maxWt * candidates.size() - totalWt;
    int randval = rand() % totalWt;
    int cumsum = 0, ind = 0;
    while((unsigned int)ind < candidates.size() && cumsum <= randval){
        cumsum += (maxWt - lsLoadMap[candidates[ind]]);
        ind++; 
    }
    return candidates[ind-1];
}


/**
 * Function prints the weights of all local schedulers, weight = max_wt + 1 - load
 *
 * @param
 * @return void
 */
void FulcrumSchedulerAlgorithm::printWeights() {
    int maxWt = 1;
    for(auto x: lsLoadMap)
        maxWt = std::max(maxWt, x.second+1);
    for(auto x: lsLoadMap)
        std::cout<<x.first<<"->"<<maxWt - x.second<<" ";
    std::cout<<std::endl;
}

