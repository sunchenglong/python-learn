/*************************************************************************
	> File Name: ex_swig.c
	> Author: 
	> Mail: 
	> Created Time: 三  4/12 22:48:47 2017
 ************************************************************************/

#include<stdio.h>
#include<time.h>
double My_variable = 3.0;

int fact(int n) {
    if(n <= 1) return 1;
    else return n*fact(n-1);
}

int my_mod(int x, int y) {
    return (x%y);
}

char *get_time() {
    time_t ltime;
    time(&ltime);
    return ctime(&ltime);
}
