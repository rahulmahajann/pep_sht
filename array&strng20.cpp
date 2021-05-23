// class Solution {
// public:
//     void sortColors(vector<int>& m) {
//         int count0=0;
//         int count1=0;
//         int count2=0;
//         for(int i=0;i<m.size();i++){
//             if(m[i]==0){
//                 count0+=1;
//             }else if(m[i]==1){
//                 count1+=1;
//             }else{
//                 count2+=1;
//             }
//         }
        
//         m.clear();
        
//         for(int i=0;i<count0;i++){
//             m.push_back(0);
//         }
//         for(int i=0;i<count1;i++){
//             m.push_back(1);
//         }
//         for(int i=0;i<count2;i++){
//             m.push_back(2);
//         }
        
    
//     }
// };