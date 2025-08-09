const numero1 = 1
const numero2 = 2
const numero3 = 3

if ((numero1 > numero2) && (numero1 > numero3)) {
    console.log(`O número ${numero1} é o número maior`);
} else if ((numero2 > numero1) && (numero2 > numero3)) {
    console.log(`O número ${numero2} é o número maior`);
} else {
    console.log(`O número ${numero3} é o número maior`);
}