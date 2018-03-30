#include "fulcrum_scheduler_algorithm.h"
#include "st_tree.h"
#include <stdlib.h> 

/**
 * Function goes through the local scheduler load map and exponentially decays the load values
 *
 * @param
 * @return void
 */
void refreshLsLoad() {
    for(auto x : fulcrumSchdAlgo.lsIndexMap){
        fulcrumSchdAlgo.lsLoadStTree.update(x->second, (int)(lsLoadStTree.getVal(x->second) * LOAD_DECAY_RATE));
    }
}

/**
 * Function updates the load map with latest local scheduler load value
 *
 * @param
 * @return void
 */
void updateLsLoad(DBClientID localSchdID) {
    int ind = fulcrumSchdAlgo.lsIndexMap[localSchdID];
    fulcrumSchdAlgo.lsLoadStTree.update(ind, lsLoadStTree.getVal(ind) + 1);
}

/**
 * Function finds the local scheduler node based on weighted load value
 *
 * @param
 * @return DBClientID
 */
DBClientID findLsByWeightedLoad() {
    int rand = rand() % (fulcrumSchdAlgo.lsLoadStTree.getTotalVal()+1);
    return fulcrumSchdAlgo.reverseLsIndexMap[fulcrumSchdAlgo.lsLoadStTree.getLowerBound(rand)];
}


