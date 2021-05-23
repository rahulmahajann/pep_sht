#include<bits/stdc++.h>
using namespace std;
#define v vector<int>

int main(){
    
    v n={3,1,2,4};

    v even,odd;
    for(int i=0;i<n.size();i++){
        if(n[i]%2==0){
            even.push_back(n[i]);
        }else{
            odd.push_back(n[i]);
        }
    }

    even.insert(even.end(),odd.begin(),odd.end());

    for(int i=0;i<even.size();i++){
        cout<<even[i]<<" ";
    }

    return 0;
}