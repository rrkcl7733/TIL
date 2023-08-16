const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim();

const arr = input.split(' ');
console.log(arr[0] - arr[1]);
