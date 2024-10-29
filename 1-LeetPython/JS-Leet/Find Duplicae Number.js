function findDuplicates(nums) {
  const seen = new Set();
  const duplicates = [];

  for (let num of nums) {
    // Check if we've already seen the number
    if (seen.has(num)) {
      // If it's a duplicate and not already in duplicates, add it
      duplicates.push(num);
    } else {
      // If not seen, add it to the `seen` set
      seen.add(num);
    }
  }

  return duplicates;
}

// Example usage
const nums = [1, 2, 3, 4, 2, 5, 3];
console.log(findDuplicates(nums)); // Output: [2, 3]
