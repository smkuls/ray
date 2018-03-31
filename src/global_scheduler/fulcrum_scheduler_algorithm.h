#ifndef FULCRUM_SCHEDULER_ALGORITHM_H
#define FULCRUM_SCHEDULER_ALGORITHM_H

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unordered_map>
#include <vector>

using namespace std;

typedef int DBClientID;

const double LOAD_DECAY_RATE = 0.5;

/// The class encapsulates state information for Falcon global scheduler
class FulcrumSchedulerAlgorithm {
public:
    unordered_map<DBClientID, int> lsLoadMap;
    void registerLs(DBClientID id);
    void refreshLsLoad();
    void updateLsLoad(DBClientID id);
    DBClientID findLsByWeightedLoad(vector<DBClientID> &candidates);
    void printWeights();
private:
};

#endif /* FULCRUM_SCHEDULER_ALGORITHM_H */
