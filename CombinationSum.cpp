#include <alogrithm>

class Solution {
public:
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    sort(candidates.begin(),candidates.end());
    vector<int> cur_process;
    vector<vector<int>> result;
    
    combinationSumByDFS(candidates,0,target,cur_process,result); 
    return result;  
  }

  void combinationSumByDFS(vector<int> &candidates,size_t start_pos,
			   int target,
                           vector<int> &cur_process,
                           vector<vector<int>> &result) {
     if(target < 0) return;
     else if(target == 0) result.push_back(cur_process);
     else{
	for(size_t i = start_pos ;  i < candidates.size() ; i ++){
          cur_process.push_back(candidates[i]);
          combinationSumByDFS(candidates,i,target - candidates[i],cur_process,result);
          cur_process.pop_back();
        }
     }
   }
};
