let number1 = [1, 2, 4];
let sortedNumber1 = [];

for (let index1 = 0; index1 < number1.length; index1++) {
    let smallestIndex = index1;

    for (let index2 = index1 + 1; index2 < number1.length; index2++) {
        if (number1[index2] < number1[smallestIndex]) {
            smallestIndex = index2;
        }
    }

    let number = number1[index1];
    number1[index1] = number1[smallestIndex];
    number1[smallestIndex] = number;

    sortedNumber1[index1] = number1[index1];
}

let number2 = [1, 3, 4];
let sortedNumber2 = [];

for (let index1 = 0; index1 < number2.length; index1++) {
    let smallestIndex = index1;

    for (let index2 = index1 + 1; index2 < number2.length; index2++) {
        if (number2[index2] < number2[smallestIndex]) {
            smallestIndex = index2;
        }
    }

    let number = number2[index1];
    number2[index1] = number2[smallestIndex];
    number2[smallestIndex] = number;

    sortedNumber2[index1] = number2[index1];
}

let result = [];
let count1 = 0;
let count2 = 0;
let index = 0;

while (count1 < sortedNumber1.length &&
       count2 < sortedNumber2.length) {

    if (sortedNumber1[count1] <= sortedNumber2[count2]) {
        result[index] = sortedNumber1[count1];
        count1++;
    } else {
        result[index] = sortedNumber2[count2];
        count2++;
    }

    index++;
}

while (count1 < sortedNumber1.length) {
    result[index] = sortedNumber1[count1];
    count1++;
    index++;
}

while (count2 < sortedNumber2.length) {
    result[index] = sortedNumber2[count2];
    count2++;
    index++;
}

console.log(sortedNumber1);
console.log(sortedNumber2);
console.log(result);
