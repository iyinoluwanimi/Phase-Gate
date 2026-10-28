import java.util.Arrays;
public class RearrangeArray {

	public static void main(String... args){

  int [][] input1 = {{1,2,3},{4,5,6},{7,8,9}};
  int [][] input2 = {{8,6},{2,4,5},{3},{1,4,2,8}};
  
  System.out.println(rearrangeArray(input1));
  System.out.println(rearrangeArray(input2));
	}

	public static String rearrangeArray(int [][]numbers) {
	  		String result  = "[\n";
		for (int row = 0; row < numbers.length; row++) {
      result  += "[";
      for(int column = 0; column < numbers[row].length; column++) {
        if(column != numbers[row].length -1){
 			  result  += numbers[row][numbers[row].length - 1 - column] + ",";       
        } else {
			  result  += numbers[row][numbers[row].length - 1 - column];        
        }			  
			
			}
			result  += "],\n";
		}
		result  += "]";
		return result;
	
	}

}
