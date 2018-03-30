#ifndef FULCRUM_SCHEDULER_ALGORITHM_H
#define FULCRUM_SCHEDULER_ALGORITHM_H

#include <random>
#include <map>
#include <vector>

using namespace std;

const LOAD_DECAY_RATE = 0.5;

/// The class encapsulates state information for Falcon global scheduler
class FulcrumSchedulerAlgorithm {
public:
    unordered_map<DBClientID, int> lsLoadMap;
    vector<DBClientID> reverseLsLoadMap;
    StTree<int> lsLoadStTree;

    void refreshLsLoadMap();
    void updateLsLoadMap(DBClientID id);
    DBClientID findLsByWeightedLoad();
private:

} fulcrumSchdAlgo;

#endif /* FULCRUM_SCHEDULER_ALGORITHM_H */
