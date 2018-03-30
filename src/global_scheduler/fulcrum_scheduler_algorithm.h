#ifndef FULCRUM_SCHEDULER_ALGORITHM_H
#define FULCRUM_SCHEDULER_ALGORITHM_H

#include <random>
#include <bits/stdc++.h>

using namespace std;

/// The class encapsulates state information for Falcon global scheduler
class FalconSchedulerAlgorithm {
public:
    unordered_map<id, int> localMap;


private:

};

/**
 * Create the state of the global scheduler policy. This state must be freed by
 * the caller.
 *
 * @return The state of the scheduling policy.
 */
GlobalSchedulerPolicyState *GlobalSchedulerPolicyState_init(void);


#endif /* FULCRUM_SCHEDULER_ALGORITHM_H */
