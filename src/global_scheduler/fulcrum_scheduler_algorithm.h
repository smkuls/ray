#ifndef FULCRUM_SCHEDULER_ALGORITHM_H
#define FULCRUM_SCHEDULER_ALGORITHM_H

#include <stdio.h>
#include <stdlib.h>
#include <unordered_map>
#include <vector>
#include "st_tree.h"

using namespace std;

const double LOAD_DECAY_RATE = 0.5;

/// The class encapsulates state information for Falcon global scheduler
class FulcrumSchedulerAlgorithm {
public:
    unordered_map<DBClientID, int> lsIndexMap;
    vector<DBClientID> reverseLsIndexMap;
    StTree<int> lsLoadStTree;

    void init_size(int size);
    void registerLs(DBClientID id);
    void refreshLsLoad();
    void updateLsLoad(DBClientID id);
    DBClientID findLsByWeightedLoad();
private:
};

#endif /* FULCRUM_SCHEDULER_ALGORITHM_H */
