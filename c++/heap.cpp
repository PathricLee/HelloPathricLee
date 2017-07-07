#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
void print_ivec(vector<int>::iterator begin, vector<int>::iterator end)
{
    for(;begin != end; ++begin)
        cout << *begin << '\t';
    cout << endl;
}
int main(int argc, char* argv[])
{
    int a[] = {1, 12, 15, 40, 30};
    vector<int> ivec(a, a + sizeof(a) / sizeof(a[0]));
    print_ivec(ivec.begin(), ivec.end());
    make_heap(ivec.begin(), ivec.end());
    print_ivec(ivec.begin(), ivec.end());
    pop_heap(ivec.begin(), ivec.end());
    std::cout << "tail em: " << ivec.back() << "\n";
    ivec.pop_back();
    print_ivec(ivec.begin(), ivec.end());
    pop_heap(ivec.begin(), ivec.end());
    std::cout << "tail em: " << ivec.back() << "\n";
    print_ivec(ivec.begin(), ivec.end());
    push_heap(ivec.begin(), ivec.end());
    print_ivec(ivec.begin(), ivec.end());
    /*
    print_ivec(ivec.begin(), ivec.end());
    ivec.push_back(99);
    push_heap(ivec.begin(), ivec.end());
    print_ivec(ivec.begin(), ivec.end());
    sort_heap(ivec.begin(), ivec.end());
    print_ivec(ivec.begin(), ivec.end());
    */
    return 0;
}
