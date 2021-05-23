#include<bits/stdc++.h>
using namespace std;
#define v vector<int>
#define pb push_back
#define pob pop_back

int main(){

    v inp={0,1,0,1,0,0,1,1,1,0};
    v out;
    int count0=0;
    int count1=0;

    for(int i=0;i<inp.size();i++){
        if(inp[i]==0){
            count0+=1;
        }else{
            count1+=1;
        }
    }

    for(int i=0;i<count0;i++){
        out.pb(0);
    }

    for(int i=0;i<count1;i++){
        out.pb(1);
    }


    for(int i=0 ; i<out.size() ; i++){
        cout<<out[i]<<" ";
    }

    // cout<<10;

    return 0;
}