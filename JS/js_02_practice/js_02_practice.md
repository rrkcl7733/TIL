# 02_practice

## practice_01

```javascript
// 1
console.log(`Hi, my name is ${name}`)

// 2
const add2 = (x, y) => {return x + y}

// 3
const tom = {
      name: 'Tom',
      introduce: name => {return `Hi, my name is ${tom.name}`}
    }

// 4
const request = {url, data}
```



## practice_02

```javascript
// 1
users.forEach(x => {console.log(x.name)})

// 2
const marriedUsers = users.filter(x => {return x.isMarried})

// 3
const tom = users.find(x => {return x.name === 'Tom'})

// 4
const newUsers = users.map(x => {return x.isAlive = true})

// 5
const totalBalance = users.reduce((acc, x) => {return acc + x.balance}, 0)
```



## practice_03

```javascript
// 1-1
const { name, extension, size } = savedFile
console.log(`The file ${name}.${extension} is size of ${size} bytes.`)

// 1-2
const { username, password, email } = data
console.log(username, password, email)

// 2
function addNumbers(...numbers) {
    return numbers.reduce((sum, number) => {
        return sum + number
    }, 0) 
}

// 3-1
const defaultColors = ['red', 'green', 'blue']
const palette = ['navy', 'black', 'gold', 'white', ...defaultColors]

// 3-2
const info = { name: 'Tom', age: 30 }
const fullinfo = {isMarried: true, balance: 3000, ...info}
```



## practice_04

```javascript
const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  let now = 0
  let cnt = 0
  let flag = true
  for (let idx = 0; idx < M-1; idx++) {
    if (chargers[idx+1] - chargers[idx] > K) {
      flag = false
      break
    }
  }		// for, else 문이 안 돼서 미리 else 문 처리 하는 작업을 거침

  if (flag) {
    while (now + K < N) {
      for (let i = K; i > 0; i--) {
        let tmp = now + i
        if (chargers.includes(tmp)) {
          now += i
          cnt += 1
          break
        }
      }

    }
    console.log(cnt)
  } else {
    console.log(0)
  }
  
}

for (const input of inputs) {
  solution(...input)
}
```
