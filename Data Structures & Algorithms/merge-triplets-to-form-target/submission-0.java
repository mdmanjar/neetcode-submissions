class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int[]max=new int[3];

        for(var t:triplets){

            if(t[0]<=target[0]&&t[1]<=target[1]&&t[2]<=target[2]){
                max[0]=Math.max(max[0],t[0]);
                max[1]=Math.max(max[1],t[1]);
                max[2]=Math.max(max[2],t[2]);
            }
        }

        return max[0]==target[0]&& max[1]==target[1]&& max[2]==target[2];
    }
}