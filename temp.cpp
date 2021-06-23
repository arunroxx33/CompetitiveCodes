#include<bits/stdc++.h>
using namespace std;
#define int long long
set < int > s1, s2, s3;
int su1 = 0, su2 = 0, su3 = 0, n;

signed main(){

    ios :: sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    int tp, power;
    for(int i = 0;i < n;++i){
        cin >> tp >> power;
        if(tp){
            if(power > 0){
                s2.insert(power);
                su2 += power;
                s3.insert(power);
                su3 += power;
            }
            else{
                auto it = s2.find(-power);
                s2.erase(it);
                su2 += power;
            }
        }
        else{
            if(power > 0){
                s1.insert(-power);
                su1 += power;
            }
            else{
                auto it = s1.find(power);
                s1.erase(it);
                su1 += power;
            }
        }

        int ans;
        if(s1.size() > 0 && s2.size() > 0){
            ans = su3 + su2 + su1;
            if(*s1.begin() > -(*s2.begin())) ans += -(*s2.begin()) -(*s1.begin());
            
        }
        else if(s2.size() > 0){
            ans = su2 * 2 - *(s2.begin());
        }
        else if(s1.size() > 0){
            ans = su1;
        }
        else ans = 0;


        cout << ans << endl;
    }
}


 