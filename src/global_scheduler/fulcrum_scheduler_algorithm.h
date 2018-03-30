#ifndef FULCRUM_SCHEDULER_ALGORITHM_H
#define FULCRUM_SCHEDULER_ALGORITHM_H

#include <random>
#include <map>
#include <vector>

using namespace std;

const double LOAD_DECAY_RATE = 0.5;

/// The class encapsulates state information for Falcon global scheduler
class FulcrumSchedulerAlgorithm {
public:
    unordered_map<DBClientID, int> lsIndexMap;
    vector<DBClientID> reverseLsIndexMap;
    StTree<int> lsLoadStTree;

    void refreshLsLoad();
    void updateLsLoad(DBClientID id);
    DBClientID findLsByWeightedLoad();
private:

} fulcrumSchdAlgo;

#endif /* FULCRUM_SCHEDULER_ALGORITHM_H */
