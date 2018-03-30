#ifndef ST_TREE_H
#define ST_TREE_H

template <class T>
class StTree{
    vector<T> arr;
public:
    void init(int size);
    void initialize(int ind, T val);
    void update(int ind, T val);
    void get(int ind);
};

#endif
