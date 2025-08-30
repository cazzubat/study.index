numeros = [1,2,3,4,5,6,7,8];
const maior = numeros.reduce((acc,cur) => Math.max(acc,cur));
console.log(maior);