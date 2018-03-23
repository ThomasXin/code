package sort;


/**
 * 此类为排序算法
 * @author 邪公子
 *
 */
public class Sort {
	public static void main(String[] args) {
		int[] nums = new int[10];
		for (int i = 0; i < nums.length; i++) {
			nums[i] =(int) (Math.random()*101);
			
		}
		System.out.println("冒泡排序==" + showNumbers(bubbleSort(nums)));
		System.out.println("选择排序==" + showNumbers(selectionSort(nums)));
		System.out.println("插入排序==" + showNumbers(insertSort(nums)));
	}
	
	/**
	 * 冒泡排序
	 * @param nums	传入的待排序数组
	 * @return
	 */
	public static int[] bubbleSort(int[] nums){
		
		
		for (int i = 0; i < nums.length-1; i++) {//轮数
			for (int j = 0; j < nums.length-1-i; j++) {//次数
				if (nums[j]>nums[j+1]) {
					int team = nums[j];
					nums[j] = nums[j+1];
					nums[j+1] = team;
					
				}
			}
		}
	
		return nums;
	}
	
	/**
	 * 选择排序:每一趟从待排序的数据元素中选出最小（或最大）的一个元素，
	 * 		   顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完
	 * @param nums
	 * @return
	 */
	public static int[] selectionSort(int[] nums){
		int size = nums.length, temp;
		for (int i = 0; i < size; i++) {
			int k=i;
			for (int j = size-1; j >i; j--) {
				if (nums[j]<nums[k]) 
					k=j;	
			}
			temp = nums[i];
			nums[i] = nums[k];
			nums[k] = temp;  
		}
		
		
		return nums;
		
	}
	/**
	 * 插入排序:该排序算法初学者理解起来比较困难。优点是较为稳定和效率高。
	 * 		缺点是比较次数不一定，比较次数越少，插入点后的数据移动越多。
	 * 插入排序由两个for循环实现，把当前待排序的元素插入到一个已经排好序的列表里面。
	 * 每次循环都会给temp赋值为当前循环到的数值，然后做逻辑比较，插入到对应的位置。
	 * @param nums
	 * @return
	 */
	public static int[] insertSort(int[] nums){
		
		int size =nums.length,temp,j;
		for (int i = 1; i < size; i++) {
			temp=nums[i];
			for (j = i; j > 0 && temp < nums[j-1]; j--)
				nums[j] = nums[j-1];
			nums[j]=temp;
		}
		return nums;
	}
	/**
	 * 基本思想:归并（Merge）排序法是将两个（或两个以上）有序表合并成一个新的有序表，
	 * 即把待排序序列分为若干个子序列，每个子序列是有序的。
	 * 然后再把有序子序列合并为整体有序序列。
	 * @param nums
	 * @return
	 */
	public static int[] mergeSout(int[] nums){
		
		
		
		return null;
		
	}
	/**
	 * 二分查找又称折半查找，它是一种效率较高的查找方法。
	 * 【二分查找要求】：1.必须采用顺序存储结构 2.必须按关键字大小有序排列。 
	 * @param nums	有序数组
	 * @param des	查找元素
	 * @return des的数组下标，没找到返回-1
	 */
	public static int binarySearch(int[] nums, int des){
		int low = 0;
		int high = nums.length -1;
		while (low<=high) {
			int middle =(low+high)/2;
			if (des==nums[middle]) {
				return middle;
			}else if (des<nums[middle]) {
				high = middle -1;
			}else {
				low = middle +1;
			}
				
		}
			
		return -1;
	}
	/**
	 * 二分查找特定整数在整型数组中的位置(递归) 
	 * @param dataset
	 * @param data
	 * @param beginIndex
	 * @param endIndex
	 * @return
	 */
    public static int binarySearch(int[] dataset,int data,int beginIndex,int endIndex){    
       int midIndex = (beginIndex+endIndex)/2;    
       if(data <dataset[beginIndex]||data>dataset[endIndex]||beginIndex>endIndex){  
           return -1;    
       }  
       if(data <dataset[midIndex]){    
           return binarySearch(dataset,data,beginIndex,midIndex-1);    
       }else if(data>dataset[midIndex]){    
           return binarySearch(dataset,data,midIndex+1,endIndex);    
       }else {    
           return midIndex;    
       }    
   }   
	
	/**
	 * 将数组转化成为字符串，便于查看结果
	 * @param nums
	 * @return
	 */
	public static String showNumbers(int[] nums ){
		String strs = "";
		for (int i = 0; i < nums.length; i++) {
			strs += nums[i] +"\t";
		}
		System.out.println();
		return strs;
		
	}
	

}
