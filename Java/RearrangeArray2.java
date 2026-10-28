import java.util.Arrays;
public class RearrangeArray2 {

	public static void main(String... args){

  int [][] input1 = {{1,2,3},{4,5,6},{7,8,9}};
  int [][] input2 = {{8,6},{2,4,5},{3},{1,4,2,8}};
  
  System.out.println(Arrays.deepToString(rearrangeMultidimentionalArray(input1)));
  System.out.println(Arrays.deepToString(rearrangeMultidimentionalArray(input2)));
	}

      public static int[] rearrangeSingleArray(int[] numbers) {

        for (int column = 0; column < numbers.length / 2; column++) {

            int number = numbers[column];

            numbers[column] = numbers[numbers.length - 1 - column];

            numbers[numbers.length - 1 - column] = number;
        }

        return numbers;
    }



	public static int [][] rearrangeMultidimentionalArray(int [][]numbers) {
		for (int row = 0; row < numbers.length; row++) {
       numbers[row] =  rearrangeSingleArray (numbers[row]);   
		}
		return numbers;
	
	}

}
