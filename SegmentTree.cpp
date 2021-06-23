#include <bits/stdc++.h>

using namespace std;


#define int long long
#define endl "\n"


const int MAXN = 2e6 + 20;

int t[4*MAXN], arr[MAXN];

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = 0;
    }
}

void update(int v, int tl, int tr, int l, int r, int add) {
    if (l > r)
        return;
    if (l == tl && r == tr) {
        t[v] += add;
    } else {
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), add);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, add);
    }
}

int get(int v, int tl, int tr, int pos) {
    if (tl == tr)
        return t[v];
    int tm = (tl + tr) / 2;
    if (pos <= tm)
        return t[v] + get(v*2, tl, tm, pos);
    else
        return t[v] + get(v*2+1, tm+1, tr, pos);
}


signed main(){

    ios :: sync_with_stdio(false);
    cout.tie(0); cin.tie(0);

    int n = 2000010;
    for(int i = 0;i < n;++i) arr[i] = i * i;

    build(arr, 1, 0, n - 1);

    // cout << get(1, 0, )

    for(int i = 0;i < n;++i){
        cout << get(1, 0, n - 1, i) << " ";
    }
    cout << endl;


    update(1, 0, n - 1, 0, n - 1, 1);

    for(int i = 0;i < n;++i){
        cout << get(1, 0, n - 1, i) << " ";
    }
    cout << endl;
    

    update(1, 0, n - 1, 0, n - 1, -1);

    for(int i = 0;i < n;++i){
        cout << get(1, 0, n - 1, i) << " ";
    }
    cout << endl;
}