let Myname: string = "Shivam Mishra";
let Myage = 20;
let Mycity: string = "Kanpur";

console.log(typeof Myname, Myage, Mycity);

//function
function add(a: number, b: number): number {
    return a + b;
}

console.log(add(3, 4))


// arrow function
let add1 = (a: number, b: number): number => {
    return a + b;
}

console.log(add1(3, 4))

// default parameter
function greet(name: string = "No is There") {
    console.log(`Hello ${name}`);
}
greet("Shivam")
greet()


// function return type
function add2(a: number, b: number): void {
    console.log(a + b);
}
add2(3, 4)

// never 



// function add3(msg:string):never{
//     throw new Error(msg);

// }

// add3("This is error")
// // add3() // this will give error

// function  neverreturn(): never{
//     while(true){
//         console.log("This will run infinite")
//         }
//         }
// let x :never ;
// x =neverreturn() // this will give error

//Arrays
let arr: number[] = [1, 2, 3, 4, 5];
console.log(arr)
let arr1: Array<number> = [1, 2, 3, 4]//more not using any more
//multi dimension
let arr2: number[][] = [[1, 2], [3, 4]]
console.log(arr2)
//tuple
let arr3: [number, number, number] = [1, 2, 3 ]
console.log(arr3)
// 3 dimensional
let arr4: number[][][] = [[[1, 2], [3, 4]],[[5, 6], [7, 8]] ]
console.log(arr4)



type user  = {
    name: string,
    age: number,
    email? : string

}

let user1: user = {
    name: "Rahul",
    age : 25,
    // email: "rahul@gmail.com"
}
console.log(user1)

