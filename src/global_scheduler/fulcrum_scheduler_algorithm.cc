#include "fulcrum_scheduler_algorithm.h"
#include "st_tree.h"
#include <stdlib.h> 
#include <assert.h>

/**
 * Function initializes the data structures for given number of machines
 *
 * @param size = number of local scheduler nodes
 * @return void
 */
void FulcrumSchedulerAlgorithm::init_size(int size) {
    reverseLsIndexMap.resize(size);
    lsLoadStTree.init(size);
}

/**
 * Function to register a DBClientID of a local scheduler 
 *
 * @param id = DBClientID of the local scheduler being registered
 * @return void
 */
void FulcrumSchedulerAlgorithm::registerLs(DBClientID id) {
    if(lsIndexMap.find(id) == lsIndexMap.end()){
        int nid = lsIndexMap.size();
        lsIndexMap[id] = nid;
        assert(reverseLsIndexMap.size() > nid);
        reverseLsIndexMap[nid] = id;
    }
}

/**
 * Function goes through the local scheduler load map and exponentially decays the load values
 *
 * @param
 * @return void
 */
void FulcrumSchedulerAlgorithm::refreshLsLoad() {
    for(auto x : lsIndexMap){
        lsLoadStTree.update(x.second, (int)(lsLoadStTree.getVal(x.second) * LOAD_DECAY_RATE));
    }
}

/**
 * Function updates the load map with latest local scheduler load value
 *
 * @param
 * @return void
 */
void FulcrumSchedulerAlgorithm::updateLsLoad(DBClientID localSchdID) {
    int ind = lsIndexMap[localSchdID];
    lsLoadStTree.update(ind, lsLoadStTree.getVal(ind) + 1);
}

/**
 * Function finds the local scheduler node based on weighted load value
 *
 * @param
 * @return DBClientID
 */
DBClientID FulcrumSchedulerAlgorithm::findLsByWeightedLoad() {
    int randind = rand() % (lsLoadStTree.getTotalVal()+1);
    return reverseLsIndexMap[lsLoadStTree.getLowerBound(randind)];
}


