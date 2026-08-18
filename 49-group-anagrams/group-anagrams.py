class Solution:
    #Brute
    """
    tot_ana = {}
    for i in range:
        sorted_v = sorted(strs[i])
        if sorted_v in tot_ana.keys():
            dict[sorted_v].append(strs[i])
        else:
            dict[sorted_v]=strs[i]
    total_list = []
    for key in tot_ana keys:
        total_list.append([all values])
    return total_lsit
    """
    #Optimal
    """
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total_ana = {}
        for i in range(len(strs)):
            sorted_v = "".join(sorted(strs[i]))
            if sorted_v in total_ana.keys():
                total_ana[sorted_v].append(strs[i])
            else:
                total_ana[sorted_v]=[strs[i]]
        
        total_list = []

        for i in total_ana.keys():
            total_list.append(total_ana[i])

        return total_list
        