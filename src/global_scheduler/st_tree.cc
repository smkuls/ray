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
    std::cout<<_size_<<" : "<<size<<std::endl;
    arr.resize(2*size);
    fill(arr.begin(), arr.end(), 0);
}

template <class T>
void StTree<T>::update(int ind, T val){
    //std::cout<<"Update : "<<ind<<" :: "<<arr[ind + size]<<"/"<<val<<std::endl;
    ind += size;
    arr[ind] = val;
    ind >>= 1;
    while(ind > 0){
        arr[ind] = arr[ind<<1] + arr[(ind<<1)+1];
        ind >>= 1; 
    }
}

template <class T>
T StTree<T>::getVal(int ind){
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


template <class T>
void StTree<T>::printTree(){
    for(int i=1; i<2*size; i++)
        std::cout<<arr[i]<<" ";
    std::cout<<std::endl;
}


