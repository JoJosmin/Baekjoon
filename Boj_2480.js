const input = require('fs').readFileSync('/dev/stdin').toString().split(" ").map(Number);

const [dice1, dice2, dice3] = [input[0], input[1], input[2]];
const answer = (dice1, dice2, dice3) => { 
    if(dice1 === dice2 && dice1 === dice3 && dice2 === dice3) return console.log(10000+(dice1*1000)); 
    if(dice1 !== dice2 || dice1 !== dice3 || dice2 !== dice3) { 
        if(dice1 === dice2 || dice1 === dice3) return console.log(1000+(dice1*100)); 
        if(dice2 === dice3) return console.log(1000+(dice2*100)); 
    } 
    if(dice1 !== dice2 && dice1 !== dice3 && dice2 !== dice3) { 
        const sort = [dice1, dice2, dice3].sort(); 
        return console.log(sort.pop() * 100); 
    } 
} 
answer(dice1, dice2, dice3);

