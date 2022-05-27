exports.sumPairs = function(arr, target) {
    let pairs = [];

    for(let i=0; i<arr.length; i++) {
        for(let j=1; j<arr.length; j++) {
            if(i < j) {
                if((arr[i] + arr[j] === target)) {
                    pairs.push([arr[i],arr[j]])
                }
            }
        }
    }
    
    if(pairs.length != 0){
        return pairs
    } else {
        return ('unable to find pairs')
    }
};

// console.log(exports.sumPairs([1,2,3,4,5], 9));  // [[4,5]]
// console.log(exports.sumPairs([1,2,3,4,5], 7));  // [[2,5], [3,4]]
// console.log(exports.sumPairs([3, 1, 5, 8, 2], 27)); // 'unable to find pairs'

let test = exports.sumPairs([1,2,3,4,5], 9);
console.log('Function answer:', test, '->', typeof test);
console.log('Expected answer:', [[4,5]], '->', typeof ([[4,5]]));

if(test === [[4,5]]) {
    console.log('True');
} else {
    console.log('False');
}