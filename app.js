// filter
// scenario -> youngFolks (under 21), grownFolks (21 and over)
const ages = [23, 17, 21, 20, 19, 34, 40, 41, 22, 25, 27]

const youngFolks = ages.filter((personAge, idx) => {
    if (personAge < 21) {
        return true;
    } else {
        return false;
    }
}); // [17, 20, 19]

console.log('Young Folks', youngFolks);


const grownFolks = ages.filter((personAge) => {
    if (personAge >= 21) {
        return true;
    } else {
        return false;
    }
});
console.log('Person Ages', ages);
console.log('Grown Folks', grownFolks);

function isNot21(personAge) {
    if (personAge < 21) {
        return true;
    } else {
        return false;
    }
}

function is21(personAge) {
    if (personAge >= 21) {
        return true;
    } else {
        return false;
    }
}

const youngPeople = ages.filter(isNot21);
const grownPeople = ages.filter(is21);

console.log('Young Folks', youngFolks);
console.log('Young People', youngPeople);
console.log('----');
console.log('Grown Folks', grownFolks);
console.log('Grown People', grownPeople);