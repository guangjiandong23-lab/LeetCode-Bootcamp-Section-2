public class Main {
    class Solution {

        //167. Two Sum II - Input Array Is Sorted
        public int[] twoSum(int[] numbers, int target) {

            int left = 0;
            int right = numbers.length-1;

            while(left < right){

                int sum = numbers[left] + numbers[right];

                if (sum == target){
                    return new int[]{left+1,right+1};
                }else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
            return new int[0];
        }

        //238. Product of Array Except Self
        public int[] productExceptSelf(int[] nums) {

            int n = nums.length;
            int[] answer = new int[n];

            answer[0] = 1;
            for (int i = 1; i < n; i++) {
                answer[i] = nums[i - 1] * answer[i - 1];
            }
            int suffix = 1;
            for (int i = n - 1; i >= 0; i--) {
                answer[i] = answer[i] * suffix;
                suffix *= nums[i];
            }

            return answer;
        }

        //75. Sort Colors
        public void sortColors(int[] nums) {
            int p0 = 0;
            int current = 0;
            int p2 = nums.length - 1;

            while (current <= p2) {
                if (nums[current] == 0) {

                    int temp = nums[p0];
                    nums[p0] = nums[current];
                    nums[current] = temp;
                    p0++;
                    current++;
                } else if (nums[current] == 2) {

                    int temp = nums[current];
                    nums[current] = nums[p2];
                    nums[p2] = temp;
                    p2--;
                } else {

                    current++;
                }
            }
        }

    }
}