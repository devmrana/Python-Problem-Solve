// let numbers = [45,23,65,97,73,44]
// let max = numbers[0]
// for (var i = 0; i < numbers.length; i++) {
// 	let element = numbers[i]
// 	if (element>max) {
// 		max=element
// 	}
// }
// console.log(max)



let user = ['Karim','Bantu','Afzal','Rahim','Bantu','Karim','Musa','Farhad','Afzal']
console.log(user.length);
let uniqueUser = [];
for (let i = 0; i < user.length; i++) {
	let element = user[i];
	let index = uniqueUser.indexOf(element);
	if (index == -1){
		uniqueUser.push(element);
	}
}
console.log(uniqueUser);


