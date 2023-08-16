//  Closures gives you access to an outer functions scope from an inner function

function outer (){
    var name = "Ashish";

    function inner(){
        console.log(`My name is ${name}`);
    }
    inner();
}
outer();