# 자바스크립트 

> 아래의 문제를 자바스크립트로 풀이하세요.

## 문제 1. 

var, let, const의 차이점을 작성하시오.

```
var : 재선언 및 재할당 모두 가능 / 호이스팅되는 특성으로 인해 예기치 못한 문제 발생 가능
let : 재할당 할 예정인 변수 / 변수 재선언 불가능
const : 재할당 예정이 없는 변수 / 변수 재선언 불가능
```

## 문제 2.

주어진 학생 점수 score의 값에 따라 다른 결과를 출력하는 코드를 작성하세요.

* 90점이상 100점 이하 : 'A'
* 80점이상 90점 미만 : 'B'
* 70점이상 80점 미만 : 'C'
* 60점이상 70점 미만: 'D'
* 60점 미만 : '과락'

```javascript
let score = 100
```

```javascript
// 코드 작성
if (90 <= score && score <= 100) {
    console.log('A')
}else if (80 <= score) {
    console.log('B')
}else if (70 <= score) {
    console.log('C')
}else if (60 <= score) {
    console.log('D')
}else {
    console.log('과락')
}
```

## 문제 3.

주어진 username인 경우 ''관리자입니다.'를 출력하고, 나머지 경우는 모두 username을 출력하는 코드를 작성하세요.

```javascript
let username = 'admin'
```

```javascript
// 코드 작성
if (username === 'admin') {
    console.log('관리자입니다.')
}else{
    console.log(username)
}
```

## 문제 4.

numbers의 숫자의 합을 출력하는 코드를 작성하세요.

기본 for문과 for...of를 활용하여 각각 작성합니다.

```javascript
let numbers = [1, 2, 3]
```

```javascript
// 기본 for 
let sumResult = 0
for (let i = 0; i < 3; i++) {
    sumResult += numbers[i]
}
console.log(sumResult)
```

```javascript
// for..of
let sumResult = 0
for (let num of numbers){
    sumResult ++ num
}
console.log(sumResult)
```
