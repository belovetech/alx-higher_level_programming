#!/usr/bin/node

const argv = process.argv;

// Extract only numbers
let nums = argv.filter(cur => !isNaN(cur));

if (!nums[0] || nums.length === 1) {
  console.log(0);
  return 0;
}

// Convert them to integers
nums = nums.map(cur => parseInt(cur));

// find max in array
const findMax = function (nums) {
  let max = nums[0];
  for (const num of nums) {
    if (max > num) max = max;
    else max = num;
  }
  return max;
};

// Remove the first biggest
const newArr = nums.filter((cur, _, arr) => cur !== findMax(arr));

// find second biggest
console.log(findMax(newArr));
