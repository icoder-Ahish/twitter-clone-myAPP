

// let has a block scope
for (let i = 0; i <= 5; i++) {
    setTimeout(()=>console.log(i),5000);     // 0 1 2 3 4 5 
}

// var has a function  scope
for (var i = 0; i <=5; i++) {
    setTimeout(()=>console.log(`var ${i}`),1000);    // 6 6 6 6 6  6 
}