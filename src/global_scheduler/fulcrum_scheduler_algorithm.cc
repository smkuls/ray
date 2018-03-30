#include "fulcrum_scheduler_algorithm.h"
#include "st_tree.h"

/**
 * Function goes through the local scheduler load map and exponentially decays the load values
 *
 * @param
 * @return void
 */
void refreshLsLoadMap() {
    for(auto x : fulcrumSchdAlgo.lsLoadMap){
        fulcrumSchdAlgo.lsLoadMap[x->first] = x->second*LOAD_DECAY_RATE;
    }
}

/**
 * Function updates the load map with latest local scheduler load value
 *
 * @param
 * @return void
 */
void updateLsLoadMap(DBClientID localSchdID) {
    fulcrumSchdAlgo.lsLoadMap[localSchdID] = fulcrumSchdAlgo.lsLoadMap[localSchdID] + 1;
}

/**
 * Function finds the local scheduler node based on weighted load value
 *
 * @param
 * @return void
 */
DBClientID findLsByWeightedLoad() {
    int rand = rand() % fulcrumSchdAlgo.lsLoadStTree.getTotalVal();
    return fulcrumSchdAlgo.reverseLsLoadMap(fulcrumSchdAlgo.lsLoadStTree.getVal(rand));
}


