class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here
        a=length
        arr=[]
        for _ in range(a):
            arr.append(0)

        update=updates

        # start = update[_][0]


        for _ in range(len(update)):
            start=update[_][0]
            end=update[_][1]
            incr=update[_][2]
            if(start>=0 and start<a):
                arr[start]+=incr
            if(end+1>=0 and end+1<a):
                arr[end+1]-=incr
        
        for _ in range(1,a):
            arr[_]+=arr[_-1]

        return (arr)