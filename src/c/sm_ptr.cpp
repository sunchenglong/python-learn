/*************************************************************************
	> File Name: sm_ptr.cpp
	> Author: 
	> Mail: 
	> Created Time: 三  4/12 14:44:12 2017
 ************************************************************************/

#include<iostream>
using namespace std;
int main(){
    unique_ptr<int> up1(new int(11));
    unique_ptr<int> up2 = up1;
    
    cout << *up1 << endl;
    unique_ptr<int> up3 = move(up1);
    cout << *up3 << endl;
    if (up1)
        cout << *up1 <<endl;

    up3.reset();
    up1.reset();

}
