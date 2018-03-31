#ifndef ST_TREE_H
#define ST_TREE_H

#include <iostream>
#include <vector>

typedef int DBClientID;

template <class T>
class StTree{
    std::vector<T> arr;
    unsigned int size;
public:
    void init(unsigned int _size_);
    void update(int ind, T val);
    T getVal(int ind);
    T getTotalVal();
    int getLowerBound(T val);
    void printTree();
};

template class StTree<DBClientID>;

#endif
