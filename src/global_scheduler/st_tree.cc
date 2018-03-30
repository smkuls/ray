#include "st_tree.h"
#include <algorithm>

unsigned int upper_power_of_two(unsigned int v){
    v--;
    v |= v >> 1;
    v |= v >> 2;
    v |= v >> 4;
    v |= v >> 8;
    v |= v >> 16;
    v++;
    return v;
}

template <class T>
void StTree<T>::init(unsigned int _size_){
    size = upper_power_of_two(_size_); 
    arr.resize(2*size);
    fill(arr.begin(), arr.begin()+2*size, 0);
}

template <class T>
void StTree<T>::update(int ind, T val){
    ind += size;
    arr[ind] = val;
    ind >>= 1;
    while(ind > 0){
        arr[ind] = arr[ind<<1] + arr[(ind<<1)+1];
        ind >>= 1; 
    }
}

template <class T>
void StTree<T>::getVal(int ind){
    return arr[ind+size]; 
}

template <class T>
T StTree<T>::getTotalVal(){
    return arr[1];
}

template <class T>
int StTree<T>::getLowerBound(T val){
    int it = 1;
    while(it < size){
       if(val <= arr[it<<1]){
            it <<= 1;
       }
       else{
            val -= arr[it<<1];
            it = (it<<1) + 1;
       }
    }
    return it-size;
}




