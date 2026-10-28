function rearrangeArray(numbers) {
    result = [];
    for (let row = 0; row < numbers.length; row++) {
        innerList = [];
        for (let column = 0; column < numbers[row].length; column++) {
        
            innerList.push(numbers[row][numbers[row].length - 1 - column]);
        
        }
        result.push(innerList);
    }
    return result;
}

console.log (rearrangeArray([[1,2,3],[4,5,6],[7,8,9]]))
console.log (rearrangeArray([[8,6],[2,4,5],[3],[1,4,2,8]])) 
