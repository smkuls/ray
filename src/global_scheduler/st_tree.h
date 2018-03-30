#ifndef ST_TREE_H
#define ST_TREE_H

template <class T>
class StTree{
    vector<T> arr;
    unsigned int size;
public:
    void init(unsigned int _size_);
    void update(int ind, T val);
    void getVal(int ind);
    T getTotalval();
    int getLowerBound(T val);
};

#endif
